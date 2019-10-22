# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver

class TrademarkSpider(scrapy.Spider):
    headers = {
        'Host': 'www.qixin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    }
    name = 'trademark'

    def start_requests(self):
        url = 'https://www.qixin.com/ability/60214084-2b87-4ea3-9131-e4c313deacf0'
        drive = webdriver.Chrome()
        drive.get("https://www.qixin.com/ability/60214084-2b87-4ea3-9131-e4c313deacf0")
        drive.find_element_by_xpath('//td[@class="text-center nowrap"]').click()
        yield scrapy.Request(url=url,headers=self.headers,callback=self.gettrademark)

    def gettrademark(self, response):
        time.sleep(30)

        self.drive.close()


    def parse(self, response):
        pass


