import sys  
import os  
import time  
from scrapy.cmdline import execute  
import os  
os.system("scrapy crawl scholar")  
time.sleep(20)  
os.system("scrapy crawl copinfo")
time.sleep(20)
os.system("scrapy crawl copinfo2")
time.sleep(20)
os.system("scrapy crawl copinfo3")