# import scrapy
# import time
# from selenium import webdriver
# from QXB.items import QxbItem
#
# class TrademarkSpider(scrapy.Spider):
#     name = 'QXB_risk'
#     start_urls={'https://www.qixin.com/risk/9836f314-4dee-41bf-b1de-22e866c62fed'}
#     def parse(self, response):
#         driver=webdriver.Firefox()
#         driver.get(response.url)
#         time.sleep(2)
#         item = QxbItem()
#         sml={}
#         # tr_list = response.xpath('//*[@id="lawSuits"]/table/tbody/tr')
#         # i=1
#         # a=[]
#         # for tr in tr_list:
#         #     sml['判决时间']=tr.xpath('./td[2]/text()').extract()
#         #     sml['身份']=tr.xpath('./td[3]/text()').extract()
#         #     sml['裁决书']=tr.xpath('./td[4]/h5/a/@href').extract()
#         #     sml['判决结果']=tr.xpath('./td[4]/div/text()').extract()
#         #     a.append({i:[sml['判决时间'],sml['身份'],sml['裁决书'],sml['判决结果']]})
#         #     i+=1
#         # item['裁判文书']=a
#         #
#         #
#         # tr_list = response.xpath('//*[@id="courtNotice"]/table/tbody/tr')
#         # i=1
#         # b=[]
#         # for tr in tr_list:
#         #     sml['开庭日期']=tr.xpath('./td[2]/text()').extract()
#         #     sml['案由']=tr.xpath('./td[3]/text()').extract()
#         #     sml['原告或上诉人']=tr.xpath('./td[4]/text()').extract()
#         #     sml['被告或被上诉人']=tr.xpath('./td[5]/text()').extract()
#         #     b.append({i:[sml['开庭日期'],sml['案由'],sml['原告或上诉人'],sml['被告或被上诉人']]})
#         #     i+=1
#         # item['开庭公告']=b
#         # i=1
#         # b=[]
#         # tr_list = response.xpath('//*[@id="equity"]/table/tbody/tr')
#         # for tr in tr_list:
#         #     a = driver.find_element_by_xpath('//*[@id="equity"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#         #     driver.execute_script('arguments[0].click()',a)
#         #     time.sleep(2)
#         #     sml['登记日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#         #     sml['状态']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#         #     sml['出质人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('textContent')
#         #     sml['出质股权数']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#         #     sml['出质人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#         #     sml['登记编号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#         #     sml['标的方']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('textContent')
#         #     sml['质权人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('textContent')
#         #     sml['质权人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#         #     sml['备注']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#         #     b.append({i:[sml['登记日期'],sml['状态'],sml['出质人'],sml['出质股权数'],sml['出质人证件号码'],sml['登记编号'],sml['标的方'],sml['质权人'],sml['质权人证件号码'],sml['备注']]})
#         #     i+=1
#         #     print(sml['登记日期'])
#         #     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#         # item['股权出质']=b
#
#
#         tr_list = response.xpath('//*[@id="lawSuits"]/table/tbody/tr')
#         i=1
#         a=[]
#         for tr in tr_list:
#             sml['发布时间']=tr.xpath('./td[2]/text()').extract()
#             sml['公告类型']=tr.xpath('./td[3]/text()').extract()
#             sml['裁决书']=tr.xpath('./td[4]/h5/a/@href').extract()
#             sml['公告内容']=tr.xpath('./td[4]/div/text()').extract()
#             a.append({i:[sml['判决时间'],sml['身份'],sml['裁决书'],sml['判决结果']]})
#             i+=1
#         item['法院公告']=a
#
#         driver.close()
#         yield item