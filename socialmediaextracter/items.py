# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class SocialmediaextracterItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class UserItem(scrapy.Item):
    _id = scrapy.Field()
    user_id = scrapy.Field()
    nick_name = scrapy.Field()
    verified = scrapy.Field()
    province = scrapy.Field()
    city = scrapy.Field()
    followers_count = scrapy.Field()
    friends_count = scrapy.Field()
    gender = scrapy.Field()
    source = scrapy.Field()
    created_at = scrapy.Field()

class CommentItem(scrapy.Item):
    _id = scrapy.Field()
    user_id = scrapy.Field()
    comment_id = scrapy.Field()
    nick_name = scrapy.Field()
    reply_count = scrapy.Field()
    like_count = scrapy.Field()
    location = scrapy.Field()
    comment_time = scrapy.Field()
    content = scrapy.Field()
    created_at = scrapy.Field()
    root_comment_id = scrapy.Field()
