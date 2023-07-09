import scrapy
import pymongo
import datetime
# import time
# import random
from socialmediaextracter.spiders import textClean
from socialmediaextracter.items import UserItem, CommentItem
from socialmediaextracter.lastScrapyRecord import ScrapyRecord
from socialmediaextracter import timeformatter

class CaixukunSpider(scrapy.Spider):

    name = "caixukun"

    allowed_domains = ["weibo.com"]

    already_process_ids = []

    duplicate_count = 0

    turn_around_flag = False

    current_handled_reply_comment_id = 0

    params = {'id': '4919379877957385', 'is_mix': '0', 'uid': '1776448504', 'fetch_level': '0'}
    
    another_param = {'id': '4919404834324822', 'is_mix': '1', 'uid': '1776448504', 'fetch_level': '1'}
    
    third_param = {'id': '4921516346837915', 'is_mix': '0', 'uid': '2487453031', 'fetch_level': '0'}

    start_urls = ["https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id={}&count=20&is_show_bulletin=2&is_mix={}&uid={}&fetch_level={}"]
    # is_first_time = True

    def __init__(self):
        super().__init__()
        self.scrapy_record = ScrapyRecord()
        self.client = pymongo.MongoClient('mongodb://nick_2014:nick_2088_21@localhost:32774/?authMechanism=DEFAULT')
        self.db = self.client['mydatabase']

    def start_requests(self):
        for url in self.start_urls:
            # if self.is_first_time:
            final_url = url.format(self.third_param['id'], self.third_param['is_mix'], self.third_param['uid'], self.third_param['fetch_level'])
            result = self.scrapy_record.get_last_scrapy_comment_id_and_total_numbers()
            if result is not None and result[0] is not None and result[0] > 0:
                final_url += f"&max_id={str(result[0])}"
            yield scrapy.Request(final_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        data = response.json().get('data')
        total_number = response.json().get('total_number')
        max_id = response.json().get('max_id')
        users = []
        comments = []
        for comment in data:
            user_data = comment.get('user')
            users.append(self.populate_user_item(user_data, comment.get('source')))
            comments.append(self.populate_comment_item(comment, user_data.get('id'), user_data.get('screen_name'), user_data.get('location')))
        
        if users:
            self.logger.info("users size %s", len(users))
            self.save_to_mongo_for_users(users)

        if comments:
            self.logger.info("comments size %s", len(comments))
            self.save_to_mongo_for_comments(comments)
            for comment in comments:
                if comment['comment_id'] != comment['root_comment_id']:
                    self.current_handled_reply_comment_id = comment['root_comment_id']
                    break

        self.scrapy_record.save_last_scrapy_comment(max_id, total_number)
        # if (max_id == 0 and total_number == 0) or (max_id == 0 and len(data) == 0):
        #    self.already_process_ids.append(self.third_param['id'])
        if max_id and max_id != 0 and len(data) > 0 and not self.turn_around_flag:
            id = self.third_param['id']
            is_mix = self.third_param['is_mix']
            uid = self.third_param['uid']
            fetch_level = self.third_param['fetch_level']
            next_page_url = f"https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id={id}&count=20&is_show_bulletin=2&is_mix={is_mix}&uid={uid}&fetch_level={fetch_level}&max_id={str(max_id)}"
            # pause_time = random.uniform(2, 4)
            # time.sleep(pause_time)
            # 递归调用自身处理下一页响应
            yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)
        else:
            self.logger.info("start to query the replys >>>>>>>>>>>>>>>")
            self.already_process_ids.append(self.third_param['id'])
            if self.current_handled_reply_comment_id != 0 and self.current_handled_reply_comment_id not in self.already_process_ids:
                self.already_process_ids.append(self.current_handled_reply_comment_id)
            self.duplicate_count = 0
            self.turn_around_flag = False
            collection = self.db['comments']
            replyed_comment_records = collection.find({'reply_count': {'$gt': 10}})
            reply_url = None
            replied_records = [record for record in replyed_comment_records]
            all_replied_comment_ids = set(record['comment_id'] for record in replied_records)
            not_yet_process_comment_ids = all_replied_comment_ids.difference(set(self.already_process_ids))
            need_process_comment = [record for record in replied_records if record['comment_id'] in not_yet_process_comment_ids]
            if need_process_comment and len(need_process_comment) > 0:
                for record in need_process_comment:
                    self.third_param['id'] = record['comment_id']
                    self.third_param['is_mix'] = 1
                    self.third_param['uid'] = record['user_id']
                    self.third_param['fetch_level'] = 1
                    reply_url = f"https://weibo.com/ajax/statuses/buildComments?flow=0&is_reload=1&id={record['comment_id']}&is_show_bulletin=2&is_mix=1&fetch_level=1&count=20&uid={record['user_id']}"
                    break
                if reply_url:
                    self.logger.info("reply_url %s", reply_url)
                    yield scrapy.Request(reply_url, callback=self.parse, dont_filter=True)

    """
    this is a field value populate
    """
    def populate_user_item(self, user, source=None):
        user_item = UserItem()
        user_item['verified'] = user.get('verified')
        user_item['user_id'] = user.get('id')
        user_item['nick_name'] = user.get('screen_name')
        user_item['gender'] = 1 if user.get('gender') == 'm' else (0 if user.get('gender') == 'f' else 2)
        array = user.get('location').split(" ")
        if len(array) == 2:
            user_item['province'] = array[0]
            user_item['city'] = array[1]
        else:
            user_item['province'] = array[0]

        user_item['followers_count'] = user.get('followers_count')
        user_item['friends_count'] = user.get('friends_count')
        user_item['source'] = source
        user_item['created_at'] = datetime.datetime.now()
        return user_item


    def populate_comment_item(self, data, user_id, nick_name, location=None):
        comment_item = CommentItem()
        comment_item['user_id'] = user_id
        comment_item['comment_id'] = data.get('id')
        comment_item['nick_name'] = nick_name
        comment_item['reply_count'] = data.get('total_number')
        comment_item['like_count'] = data.get('like_counts')
        comment_item['location'] = location
        comment_item['root_comment_id'] = data.get('rootid')
        comment_item['comment_time'] = timeformatter.time_formatter(data.get('created_at'))
        text_content = data.get('text_raw')
        comment_item['content'] = textClean.clean_text(text_content)
        comment_item['created_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return comment_item

    def save_to_mongo_for_users(self, users):
        collection = self.db['users']
        existing_records = collection.find({'user_id': {'$in': [data['user_id'] for data in users]}})
        existing_user_ids = set(record['user_id'] for record in existing_records)
        for user in users:
            if user['user_id'] in existing_user_ids:
                # print(f"Skipping duplicate data: {user}")
                continue
            collection.insert_one(user)

    def save_to_mongo_for_comments(self, comments):
        collection = self.db['comments']
        comment_ids = [item['comment_id'] for item in comments]
        existing_records = collection.find({'comment_id': {'$in': comment_ids}})
    
        existing_comment_ids = set(record['comment_id'] for record in existing_records)
        for comment in comments:
            if comment['comment_id'] in existing_comment_ids or comment['content'].startswith("图片评论"):
                # print(f"Skipping duplicate data: {comment}")
                self.duplicate_count += 1
                if self.duplicate_count > 220:
                    self.logger.info("duplicate count is %s", self.duplicate_count)
                    self.duplicate_count = 0
                    self.turn_around_flag = True
                continue
            collection.insert_one(comment)
