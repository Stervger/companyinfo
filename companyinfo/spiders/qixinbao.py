# -*- coding: utf-8 -*-
import codecs
from selenium import webdriver
import time
import scrapy
import re

class QixinbaoSpider(scrapy.Spider):
    cookie = 'acw_tc=2f624a5815717107809494134e0454956bde8fdbcc0c1368190122d159d980; channel=%2Bbaidusem17; cookieShowLoginTip=3; Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71=1571882386,1571966085,1571992694,1571994259; acw_sc__v2=5db2ba998709f844b8f9ed3c7809e0149ca525e3; sid=s%3ABFXg0UgU7QMjQRfEsH8ciwXdYc57XzDN.WXP4OtjBJ9lVAV29GfEUOguzn95fe99velAlXHrtn1U; Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71=1571994290'
    headers = {
        'Host': 'www.qixin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36',
        'Cookie': cookie
    }

    name = 'qixinbao'

    def start_requests(self):
        f = open('./2.txt','r',encoding='utf-8').readlines()
        for a2 in f:
            urls = ['https://www.qixin.com/search?from=baidusem24&key=重庆'+str(a2)[:-1]+'&page={0}'.format(i) for i in range(1,4)]
            for url in urls:
                yield scrapy.Request(url=str(url),headers=self.headers,callback=self.parse)
                print(url)
    def parse(self, response):
        driver = webdriver.Firefox()
        driver.get(response.url)
        time.sleep(30)
        driver.close()
        urls = re.findall(r'keyId="(.*?)"',response.text,re.M)
        print(urls)
        file = codecs.open('company.txt', 'a+', encoding='utf-8')
        for url in urls:
            file.write(url+'\n')
        file.close()


































