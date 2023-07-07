import pymongo
import datetime

class ScrapyRecord(object):
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://nick_2014:nick_2088_21@localhost:32774/?authMechanism=DEFAULT')
        self.db = self.client['mydatabase']
        self.collection = self.db['scrapy_record']

    def save_last_scrapy_comment(self, comment_id, total_number):
        current_time = datetime.datetime.now()
        data = {
            'last_scraped_time': current_time,
            'last_comment_id': comment_id,
            'total_number': total_number
        }
        self.collection.replace_one({}, data, upsert=True)

    def get_last_scrapy_comment_id_and_total_numbers(self):
        data = self.collection.find_one({})
        if not data:
            return None
        return [data['last_comment_id'], data['total_comments']]
    
    def get_latest_comment(self):
        comment_collection = self.db['comments']
        comment = comment_collection.find_one({}, sort=[('created_at', -1)])
        if not comment:
            return None
        return comment['comment_id']



