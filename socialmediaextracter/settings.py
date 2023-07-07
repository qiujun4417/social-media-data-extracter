# Scrapy settings for socialmediaextracter project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "socialmediaextracter"

SPIDER_MODULES = ["socialmediaextracter.spiders"]
NEWSPIDER_MODULE = "socialmediaextracter.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "socialmediaextracter (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "en",
   "Cookie": "XSRF-TOKEN=-zJRebRiG4jVld3y4EO0IbF0; PC_TOKEN=ace62a276e; SUB=_2AkMT_xAQf8NxqwJRmPATzmjjbY9zywnEieKlo-HLJRMxHRl-yT9kql1btRB6OH8-_3Oohz4cz7htMb5azovZqy72vucl; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWhC0Or7a1RSgho-rTXQ3aT; login_sid_t=0cff2c51efbacbceddee2eb0f89a5fc8; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=passport.weibo.com; wb_view_log=2560*14401; Apache=7065432359410.706.1688444716619; SINAGLOBAL=7065432359410.706.1688444716619; ULV=1688444716621:1:1:1:7065432359410.706.1688444716619:; WBPSESS=durPiJxsbzq5XDaI2wW0N_ReaXVVRoGRwQMUJgtQxnPi7AK0WLCBnQ-McHGu-ouOmW8xf4Kt94IJfT51P8-MnLwSwhoUXXNG95Ot6nOqTIDumKfGPXGRiUfwAKBQrxA0tmAo0oYqceLVUBf8iuPRnqaojGUECu2UCAfxGHxKq6Y=",
   "X-Xsrf-Token": "-zJRebRiG4jVld3y4EO0IbF0",
   "Referer": "https://weibo.com/u/1776448504",
   "X-Requested-With": "XMLHttpRequest",
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
   "Traceparent": "00-0ad05afa89e6429bcdc855fd740bfda6-8cad83b8e3f6bb3d-00"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "socialmediaextracter.middlewares.SocialmediaextracterSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "socialmediaextracter.middlewares.SocialmediaextracterDownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "socialmediaextracter.pipelines.SocialmediaextracterPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
FAMEL=0
MALE=1
UNKNOWN=2
