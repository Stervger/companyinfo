import time

import scrapy
from companyinfo.items import CompanyinfoItem
import re
import json
import codecs
import scrapy.spidermiddlewares.httperror
from selenium import webdriver
# from Verification.DJ import unlock

class QXBSpider(scrapy.Spider):
    name = 'search_key'

    def start_requests(self):
        f = open('E:/python_work/companyinfo/companyinfo/key.txt','r',encoding='utf-8')
        for a2 in f:
            for a in a2[1:]:
                for i in range(1,5):
                    for j in range(1,5):
                        for k in range(1,4):
                            urls = ['https://www.qixin.com/search?capital='+str(i)+'&key=重庆'+a+'&page='+str(k)+'&year='+str(j)+'']
                            for url in urls:
                                yield scrapy.Request(url=str(url),callback=self.parse)
    def parse(self, response):
       if response.status == 200:  
            urls = re.findall(r'keyId="(.*?)"',response.text,re.M)
            print(urls)
            file = codecs.open('company.txt', 'a+', encoding='utf-8')
            for url in urls:
                file.write(url+'\n')
            file.close()
       else:
           driver = webdriver.Chrome()
           driver.get(response.url)
           totalnum = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[1]/div[4]/div[1]/div/div/div[1]/em').get_attribute('textContent')
           if totalnum == 10:
               totalpage = 1
           elif totalnum % 10 == 0:
               totalpage = totalnum // 10
               if totalpage > 4:
                   totalpage = 3
           else:
               totalpage = totalnum // 5 + 1
               if totalpage > 4:
                   totalpage = 3
           lastpagenum = totalnum % 10
           i = 1
           # print(totalpage)
           if totalpage > 1:
               for p in range(1, totalpage + 1):
                   page = driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[1]/div[5]/div/div/nav/ul/li[{0}]/a'.format(p + 1))
                   driver.execute_script('arguments[0].click()', page)
                   time.sleep(30)
                   driver.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[1]/div[4]/div[2]/div[{0}]/div[2]/div[1]/div[1]/a'.format(i) for i in range(lastpagenum)).get_attribute('textContent')