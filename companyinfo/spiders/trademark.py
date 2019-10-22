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
        drive = webdriver.Firefox()
        drive.get("https://www.qixin.com/ability/60214084-2b87-4ea3-9131-e4c313deacf0")
        # print(drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[1]/td[@class="text-center nowrap"]/a').get_attribute('href'))
        #控制tr[i]进行循环，现在无法循环(报错)
        drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[1]/td[@class="text-center nowrap"]').click()
        time.sleep(1)
        drive.find_element_by_xpath('//div[@class="modal-header modal-new-header"]/div[@class="close-div"]').click()
        time.sleep(1)
        drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[2]/td[@class="text-center nowrap"]').click()
        time.sleep(1)
        drive.find_element_by_xpath('//div[@class="modal-header modal-new-header"]/div[@class="close-div"]').click()
        #第2条过后开始无法点击详情（Message: Element <td class="text-center nowrap"> is not clickable at point (881,845) because another element <div class="container clear-fix"> obscures it）
        # time.sleep(10)
        # drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[3]/td[@class="text-center nowrap"]').click()
        # time.sleep(3)
        # drive.find_element_by_xpath('//div[@class="modal-header modal-new-header"]/div[@class="close-div"]').click()
        # time.sleep(3)
        # drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[4]/td[@class="text-center nowrap"]').click()
        # time.sleep(1)
        # drive.find_element_by_xpath('//div[@class="modal-header modal-new-header"]/div[@class="close-div"]').click()
        # time.sleep(1)
        # drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[5]/td[@class="text-center nowrap"]').click()
        # time.sleep(1)
        # drive.find_element_by_xpath('//div[@class="modal-header modal-new-header"]/div[@class="close-div"]').click()
        time.sleep(3)
        drive.close()
        yield scrapy.Request(url=url,headers=self.headers,callback=self.parse)

    def parse(self, response):
        pass


