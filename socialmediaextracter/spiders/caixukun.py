import scrapy
import pymongo
import datetime
import time
import random
from socialmediaextracter.spiders import textClean
from socialmediaextracter.items import UserItem, CommentItem
from socialmediaextracter.lastScrapyRecord import ScrapyRecord
from socialmediaextracter import timeformatter

class CaixukunSpider(scrapy.Spider):

    name = "caixukun"
    allowed_domains = ["weibo.com"]
    
    start_urls = ["https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4919379877957385&count=20&is_show_bulletin=2&is_mix=0&uid=1776448504&fetch_level=0"]

    def __init__(self):
        super().__init__()
        self.scrapy_record = ScrapyRecord()
        self.client = pymongo.MongoClient('mongodb://nick_2014:nick_2088_21@localhost:32774/?authMechanism=DEFAULT')
        self.db = self.client['mydatabase']

    def start_requests(self):
        for url in self.start_urls:
            result = self.scrapy_record.get_last_scrapy_comment_id_and_total_numbers()
            if result is not None and result[0] is not None and result[0] > 0:
                url += f"&max_id={str(result[0])}"
            elif result is not None and result[0] is not None and result[0] == 0:
                collection = self.db['comments']
                total_count = collection.count_documents({})
                total_comments = result[1]
                if total_comments > total_count:
                    last_comment_id = self.scrapy_record.get_latest_comment()
                    if last_comment_id:
                        url += f"&max_id={str(last_comment_id)}"
            yield scrapy.Request(url, callback=self.parse, dont_filter=True)

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

        self.scrapy_record.save_last_scrapy_comment(max_id, total_number)
        if max_id & max_id != 0:
            next_page_url = f"https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4919379877957385&count=20&is_show_bulletin=2&is_mix=0&uid=1776448504&fetch_level=0&max_id={str(max_id)}"
            pause_time = random.uniform(2, 4)
            time.sleep(pause_time)
        else:
            last_comment_id = self.scrapy_record.get_latest_comment()
            next_page_url = f"https://weibo.com/ajax/statuses/buildComments?is_reload=1&id=4919379877957385&count=20&is_show_bulletin=2&is_mix=0&uid=1776448504&fetch_level=0&max_id={str(last_comment_id)}"
        
        # 递归调用自身处理下一页响应
        yield scrapy.Request(next_page_url, callback=self.parse, dont_filter=True)

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
        existing_records = collection.find({'comment_id': {'$in': [data['comment_id'] for data in comments]}})
        existing_comment_ids = set(record['comment_id'] for record in existing_records)
        for comment in comments:
            if comment['comment_id'] in existing_comment_ids or comment['content'].startswith("图片评论"):
                # print(f"Skipping duplicate data: {comment}")
                continue
            collection.insert_one(comment)


            
