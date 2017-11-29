# -*- coding: utf-8 -*-

# Scrapy settings for getauthor project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'getauthor'

SPIDER_MODULES = ['getauthor.spiders']
NEWSPIDER_MODULE = 'getauthor.spiders'
# 其中Scrapy下载执行现有的最大请求数。
# CONCURRENT_REQUESTS=6
#禁用cookie
COOKIES_ENABLED=False
#有这个下载延时的话8个小时爬了3500条还没停止，没有这个的话，1200多就被ban了
#暂时认为，这种设置下能够一直爬，可以再研究一下换ip
DOWNLOAD_DELAY=1

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'getauthor (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS =30

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
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
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'getauthor.middlewares.GetauthorSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'getauthor.middlewares.UserAgentMiddleware': 543,
   # 'getauthor.middlewares.MyproxiesSpiderMiddleware':125
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'getauthor.pipelines.GetauthorPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
# IPPOOL=[
#     {"ipaddr":"189.96.210.98:8080"},
#     {"ipaddr":"190.199.64.25:8080"},
#     {"ipaddr":"27.254.220.4:8080"},
#     {"ipaddr":"201.217.217.26:8080"},
#     {"ipaddr":"52.174.89.111:80"},
#     # {"ipaddr":"121.232.146.169:8080"},
#     # {"ipaddr":"121.232.146.77"},
    # {"ipaddr":"121.232.147.144"},
    # {"ipaddr":"119.57.112.130"},
    # {"ipaddr":"121.232.148.65"},



# SCHEDULER = 'getauthor.scrapy_redis.scheduler.Scheduler'
# SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = 'getauthor.scrapy_redis.queue.SpiderSimpleQueue'
#
# # 种子队列的信息
# REDIE_URL = None
# REDIS_HOST = '127.0.0.1'
# REDIS_PORT = 6379
#
# # 去重队列的信息
# FILTER_URL = None
# FILTER_HOST = '127.0.0.1'
# FILTER_PORT = 6379
# FILTER_DB = 0
