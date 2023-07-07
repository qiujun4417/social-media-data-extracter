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
   "Cookie": "XSRF-TOKEN=bmAX3dftBsfJWqGoV5hQhlug; PC_TOKEN=ad047104dc; SUB=_2AkMT-3R5f8NxqwJRmfAQzGnrbYt0yArEieKlp4WiJRMxHRl-yT9kqh0stRB6OHtalR4DPFLha73kAsQfp2JfzPMOAeql; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Wh5GzCgIBk3v1r-BLemfpLR; login_sid_t=5a6a6a44bd5091a0181bc49371d56f79; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; _s_tentry=passport.weibo.com; wb_view_log=2560*14401; Apache=5241255125585.357.1688730453150; SINAGLOBAL=5241255125585.357.1688730453150; ULV=1688730453153:1:1:1:5241255125585.357.1688730453150:; WBPSESS=NcA3pTjBP9SOtpsXaAXWl2WjI8D_jaWPZdFgUTT1XIWOp1L_TH3PF0S9qEO4gv7ggPjfkh_qWwU2roC6V19FDGxxeeCcKLFRttKrCmzBGC6PJLaS_D-4Ra2IfThxzVnJhieqj1KKQfaZr4_UrVqW9XaIDruzx8uiRjtMSFgchUc=",
   "X-Xsrf-Token": "bmAX3dftBsfJWqGoV5hQhlug",
   "Referer": "https://weibo.com/u/1776448504",
   "X-Requested-With": "XMLHttpRequest",
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
   "Traceparent": "00-4a2a52ff8b32347ecf8a0d3c4e639ab0-623a5d4ef89dcdd8-00"
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
