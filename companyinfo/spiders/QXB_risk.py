# import scrapy
# import time
# from selenium import webdriver
# from QXB.risk_items import risk_items
#
# class TrademarkSpider(scrapy.Spider):
#     name = 'QXB_risk'
#     start_urls={'https://www.qixin.com/risk/68f908b5-3fe9-4e4d-ac8b-4577c5f3deb7'}
#     def parse(self, response):
#         driver=webdriver.Firefox()
#         driver.get(response.url)
#         time.sleep(2)
#         item = risk_items()
#         item['name'] = response.xpath('/html/body/div[2]/div/div/div/div/div[2]/div[1]/div[1]/h3/text()').extract()
#         item['metaModel']='公司背景'
#         item['source']='启信宝'
#         item['url']=response.url
#         item['data']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#         mid={}
#         sml={}
#         totalpage = int(driver.find_element_by_xpath('//*[@id="lawSuits"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="lawSuits"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 i = 1
#                 a = []
#                 tr_list = response.xpath('//*[@id="lawSuits"]/table/tbody/tr')
#                 for tr in tr_list:
#                     tr_list = response.xpath('//*[@id="lawSuits"]/table/tbody/tr')
#                     i=1
#                     a=[]
#                     for tr in tr_list:
#                         sml['判决时间']=tr.xpath('./td[2]/text()').extract()
#                         sml['身份']=tr.xpath('./td[3]/text()').extract()
#                         sml['裁决书']=tr.xpath('./td[4]/h5/a/@href').extract()
#                         sml['判决结果']=tr.xpath('./td[4]/div/text()').extract()
#                         a.append({i:{'判决时间':sml['判决时间'],'身份':sml['身份'],'裁决书':sml['裁决书'],'判决结果':sml['判决结果']}})
#                         i+=1
#                     mid['裁判文书']=a
#                 else:
#                     tr_list = response.xpath('//*[@id="lawSuits"]/table/tbody/tr')
#                     i=1
#                     a=[]
#                     for tr in tr_list:
#                         sml['判决时间']=tr.xpath('./td[2]/text()').extract()
#                         sml['身份']=tr.xpath('./td[3]/text()').extract()
#                         sml['裁决书']=tr.xpath('./td[4]/h5/a/@href').extract()
#                         sml['判决结果']=tr.xpath('./td[4]/div/text()').extract()
#                         a.append({i:{'判决时间':sml['判决时间'],'身份':sml['身份'],'裁决书':sml['裁决书'],'判决结果':sml['判决结果']}})
#                         i+=1
#                     mid['裁判文书']=a
#
#         totalpage = int(driver.find_element_by_xpath('//*[@id="courtNotice"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="courtNotice"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 i = 1
#                 a = []
#                 tr_list = response.xpath('//*[@id="courtNotice"]/table/tbody/tr')
#                 for tr in tr_list:
#                     tr_list = response.xpath('//*[@id="courtNotice"]/table/tbody/tr')
#                     i=1
#                     b=[]
#                     for tr in tr_list:
#                         sml['开庭日期']=tr.xpath('./td[2]/text()').extract()
#                         sml['案由']=tr.xpath('./td[3]/text()').extract()
#                         sml['原告或上诉人']=tr.xpath('./td[4]/text()').extract()
#                         sml['被告或被上诉人']=tr.xpath('./td[5]/text()').extract()
#                         b.append({i:{'开庭日期':sml['开庭日期'],'案由':sml['案由'],'原告或上诉人':sml['原告或上诉人'],'被告或被上诉人':sml['被告或被上诉人']}})
#                         i+=1
#                     mid['开庭公告']=b
#         else:
#                     tr_list = response.xpath('//*[@id="courtNotice"]/table/tbody/tr')
#                     i=1
#                     b=[]
#                     for tr in tr_list:
#                         sml['开庭日期']=tr.xpath('./td[2]/text()').extract()
#                         sml['案由']=tr.xpath('./td[3]/text()').extract()
#                         sml['原告或上诉人']=tr.xpath('./td[4]/text()').extract()
#                         sml['被告或被上诉人']=tr.xpath('./td[5]/text()').extract()
#                         b.append({i:{'开庭日期':sml['开庭日期'],'案由':sml['案由'],'原告或上诉人':sml['原告或上诉人'],'被告或被上诉人':sml['被告或被上诉人']}})
#                         i+=1
#                     mid['开庭公告']=b
#         totalpage = int(driver.find_element_by_xpath('//*[@id="equity"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="equity"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 i=1
#                 b=[]
#                 tr_list = response.xpath('//*[@id="equity"]/table/tbody/tr')
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="equity"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['登记日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['状态']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['出质人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('textContent')
#                     sml['出质股权数']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['出质人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['登记编号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['标的方']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('textContent')
#                     sml['质权人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('textContent')
#                     sml['质权人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                     sml['备注']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                     b.append({i:{'登记日期':sml['登记日期'],'状态':sml['状态'],'出质人':sml['出质人'],'出质股权数':sml['出质股权数'],'出质人证件号码':sml['出质人证件号码'],'登记编号':sml['登记编号'],'标的方':sml['标的方'],'质权人':sml['质权人'],'质权人证件号码':sml['质权人证件号码'],'备注':sml['备注']}})
#                     i+=1
#                     print(sml['登记日期'])
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['股权出质']=b
#         else:
#             i=1
#             b=[]
#             tr_list = response.xpath('//*[@id="equity"]/table/tbody/tr')
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="equity"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['登记日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['状态']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['出质人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('textContent')
#                 sml['出质股权数']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['出质人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['登记编号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['标的方']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('textContent')
#                 sml['质权人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('textContent')
#                 sml['质权人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                 sml['备注']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                 b.append({i:{'登记日期':sml['登记日期'],'状态':sml['状态'],'出质人':sml['出质人'],'出质股权数':sml['出质股权数'],'出质人证件号码':sml['出质人证件号码'],'登记编号':sml['登记编号'],'标的方':sml['标的方'],'质权人':sml['质权人'],'质权人证件号码':sml['质权人证件号码'],'备注':sml['备注']}})
#                 i+=1
#                 print(sml['登记日期'])
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['股权出质']=b
#
#         totalpage = int(driver.find_element_by_xpath('//*[@id="notices"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="notices"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="notices"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="notices"]/table/tbody/tr[{0}]/td[4]/h5/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['发布日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['公告类型']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['当事人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['公告法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['内容']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     b.append({i:{'发布日期':sml['发布日期'],'公告类型':sml['公告类型'],'当事人':sml['当事人'],'公告法院':sml['公告法院'],'内容':sml['内容']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 item['法院公告']=b
#         else:
#             tr_list = response.xpath('//*[@id="notices"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="notices"]/table/tbody/tr[{0}]/td[4]/h5/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['发布日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['公告类型']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['当事人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['公告法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['内容']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 b.append({i:{'发布日期':sml['发布日期'],'公告类型':sml['公告类型'],'当事人':sml['当事人'],'公告法院':sml['公告法院'],'内容':sml['内容']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             item['法院公告']=b
#
#         totalpage = int(driver.find_element_by_xpath('//*[@id="punishment"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="punishment"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="punishment"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="punishment"]/table/tbody/tr[{0}]/td[6]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['决定文书号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['处罚类型']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['处罚机关']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['处罚日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['公示日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                     sml['处罚内容']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                     sml['处罚依据']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[7]/td[2]').get_attribute('textContent')
#                     b.append({i:{'决定文书号':sml['决定文书号'],'处罚类型':sml['处罚类型'],'处罚机关':sml['处罚机关'],'处罚日期':sml['处罚日期'],'公示日期':sml['公示日期'],'处罚内容':sml['处罚内容'],'处罚依据':sml['处罚依据']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['行政处罚']=b
#         else:
#             tr_list = response.xpath('//*[@id="punishment"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="punishment"]/table/tbody/tr[{0}]/td[6]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['决定文书号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['处罚类型']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['处罚机关']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['处罚日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['公示日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                 sml['处罚内容']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                 sml['处罚依据']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[7]/td[2]').get_attribute('textContent')
#                 b.append({i:{'决定文书号':sml['决定文书号'],'处罚类型':sml['处罚类型'],'处罚机关':sml['处罚机关'],'处罚日期':sml['处罚日期'],'公示日期':sml['公示日期'],'处罚内容':sml['处罚内容'],'处罚依据':sml['处罚依据']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['行政处罚']=b
#
#         totalpage = int(driver.find_element_by_xpath('//*[@id="case"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="case"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="case"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="case"]/table/tbody/tr[{0}]/td[5]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['案号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['承办法官']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['法官助理']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['立案时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['开庭时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['结束时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['案件状态']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['被告']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                     sml['原告']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                     b.append({i:{'案号':sml['案号'],'承办法官':sml['承办法官'],'法官助理':sml['法官助理'],'立案时间':sml['立案时间'],'开庭时间':sml['开庭时间'],'结束时间':sml['结束时间'],'案件状态':sml['案件状态'],'被告':sml['被告'],'原告':sml['原告']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['立案信息']=b
#         else:
#             tr_list = response.xpath('//*[@id="case"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="case"]/table/tbody/tr[{0}]/td[5]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['案号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['承办法官']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['法官助理']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['立案时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['开庭时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['结束时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['案件状态']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['被告']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                 sml['原告']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                 b.append({i:{'案号':sml['案号'],'承办法官':sml['承办法官'],'法官助理':sml['法官助理'],'立案时间':sml['立案时间'],'开庭时间':sml['开庭时间'],'结束时间':sml['结束时间'],'案件状态':sml['案件状态'],'被告':sml['被告'],'原告':sml['原告']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['立案信息']=b
#
#         totalpage = int(driver.find_element_by_xpath('//*[@id="envPunishment"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="envPunishment"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="envPunishment"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="envPunishment"]/table/tbody/tr[{0}]/td[6]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['项目名称']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['生产状况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['开工建设时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['存在问题']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['清理措施']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['责任单位']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['拟完成时限']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['完成情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                     b.append({i:{'项目名称':sml['项目名称'],'生产状况':sml['生产状况'],'开工建设时间':sml['开工建设时间'],'存在问题':sml['存在问题'],'清理措施':sml['清理措施'],'责任单位':sml['责任单位'],'拟完成时限':sml['拟完成时限'],'完成情况':sml['完成情况']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['环保处罚']=b
#         else:
#             tr_list = response.xpath('//*[@id="envPunishment"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="envPunishment"]/table/tbody/tr[{0}]/td[6]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['项目名称']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['生产状况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['开工建设时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['存在问题']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['清理措施']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['责任单位']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['拟完成时限']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['完成情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                 b.append({i:{'项目名称':sml['项目名称'],'生产状况':sml['生产状况'],'开工建设时间':sml['开工建设时间'],'存在问题':sml['存在问题'],'清理措施':sml['清理措施'],'责任单位':sml['责任单位'],'拟完成时限':sml['拟完成时限'],'完成情况':sml['完成情况']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['环保处罚']=b
#         totalpage = int(driver.find_element_by_xpath('//*[@id="mortgages"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="mortgages"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="mortgages"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="mortgages"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['登记编号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['登记时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['登记机关']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['被担保债权数额']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['被担保债权种类']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['债务人履行债务的期限']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['担保范围']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['备注']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[5]/td[2]').get_attribute('textContent')
#                     b.append({i:{'登记编号':sml['登记编号'],'登记时间':sml['登记时间'],'登记机关':sml['登记机关'],'被担保债权数额':sml['被担保债权数额'],'被担保债权种类':sml['被担保债权种类'],'债务人履行债务的期限':sml['债务人履行债务的期限'],'担保范围':sml['担保范围'],'备注':sml['备注']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['动产抵押']=b
#         else:
#             tr_list = response.xpath('//*[@id="mortgages"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="mortgages"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['登记编号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['登记时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['登记机关']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['被担保债权数额']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['被担保债权种类']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['债务人履行债务的期限']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['担保范围']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['备注']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table[1]/tbody/tr[5]/td[2]').get_attribute('textContent')
#                 b.append({i:{'登记编号':sml['登记编号'],'登记时间':sml['登记时间'],'登记机关':sml['登记机关'],'被担保债权数额':sml['被担保债权数额'],'被担保债权种类':sml['被担保债权种类'],'债务人履行债务的期限':sml['债务人履行债务的期限'],'担保范围':sml['担保范围'],'备注':sml['备注']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['动产抵押']=b
#
#
#         totalpage = int(driver.find_element_by_xpath('//*[@id="equity"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="equity"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="equity"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="equity"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['登记日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['状态']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['出质人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['出质股权数']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['出质人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['登记编号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['标的方']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['质权人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                     sml['质权人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                     sml['备注']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                     b.append({i:{'登记日期':sml['登记日期'],'状态':sml['状态'],'出质人':sml['出质人'],'出质股权数':sml['出质股权数'],'出质人证件号码':sml['出质人证件号码'],'登记编号':sml['登记编号'],'标的方':sml['标的方'],'质权人':sml['质权人'],'质权人证件号码':sml['质权人证件号码'],'备注':sml['备注']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['股权出质']=b
#         else:
#             tr_list = response.xpath('//*[@id="equity"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="equity"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['登记日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['状态']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['出质人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['出质股权数']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['出质人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['登记编号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['标的方']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['质权人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                 sml['质权人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                 sml['备注']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                 b.append({i:{'登记日期':sml['登记日期'],'状态':sml['状态'],'出质人':sml['出质人'],'出质股权数':sml['出质股权数'],'出质人证件号码':sml['出质人证件号码'],'登记编号':sml['登记编号'],'标的方':sml['标的方'],'质权人':sml['质权人'],'质权人证件号码':sml['质权人证件号码'],'备注':sml['备注']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['股权出质']=b
#
#         totalpage = int(driver.find_element_by_xpath('//*[@id="equity"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="equity"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="executedPerson"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     sml['立案时间']=tr.xpath('./td[2]').extract()
#                     sml['案号']=tr.xpath('./td[3]/text()').extract()
#                     sml['执行标的']=tr.xpath('./td[4]/text()').extract()
#                     sml['执行法院']=tr.xpath('./td[5]/text()').extract()
#                     b.append({i:{'立案时间':sml['立案时间'],'案号':sml['案号'],'执行标的':sml['执行标的'],'执行法院':sml['执行法院']}})
#                     i+=1
#                 mid['被执行人信息']=b
#         else:
#             tr_list = response.xpath('//*[@id="executedPerson"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 sml['立案时间']=tr.xpath('./td[2]').extract()
#                 sml['案号']=tr.xpath('./td[3]/text()').extract()
#                 sml['执行标的']=tr.xpath('./td[4]/text()').extract()
#                 sml['执行法院']=tr.xpath('./td[5]/text()').extract()
#                 b.append({i:{'立案时间':sml['立案时间'],'案号':sml['案号'],'执行标的':sml['执行标的'],'执行法院':sml['执行法院']}})
#                 i+=1
#             mid['被执行人信息']=b
#         totalpage = int(driver.find_element_by_xpath('//*[@id="equityFreeze"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="equityFreeze"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="equityFreeze"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="equityFreeze"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['执行法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['执行事项']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['执行裁定文书号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['执行通知文书号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['被执行人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['被执行人持有股权、其它投资权益的数额']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['被执行人证件种类']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['被执行人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                     sml['冻结期限自']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                     sml['冻结期限至']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                     sml['冻结期限']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                     sml['公示日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[4]').get_attribute('textContent')
#                     b.append({i:{'执行法院':sml['执行法院'],'执行事项':sml['执行事项'],'执行裁定文书号':sml['执行裁定文书号'],'执行通知文书号':sml['执行通知文书号'],'被执行人':sml['被执行人'],'被执行人持有股权、其它投资权益的数额':sml['被执行人持有股权、其它投资权益的数额'],'被执行人证件种类':sml['被执行人证件种类'],'被执行人证件号码':sml['被执行人证件号码'],'冻结期限自':sml['冻结期限自'],'冻结期限至':sml['冻结期限至'],'冻结期限':sml['冻结期限'],'公示日期':sml['公示日期']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['股权冻结']=b
#         else:
#             tr_list = response.xpath('//*[@id="equityFreeze"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="equityFreeze"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['执行法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['执行事项']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['执行裁定文书号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['执行通知文书号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['被执行人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['被执行人持有股权、其它投资权益的数额']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['被执行人证件种类']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['被执行人证件号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                 sml['冻结期限自']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                 sml['冻结期限至']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                 sml['冻结期限']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                 sml['公示日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div[2]/table/tbody/tr[6]/td[4]').get_attribute('textContent')
#                 b.append({i:{'执行法院':sml['执行法院'],'执行事项':sml['执行事项'],'执行裁定文书号':sml['执行裁定文书号'],'执行通知文书号':sml['执行通知文书号'],'被执行人':sml['被执行人'],'被执行人持有股权、其它投资权益的数额':sml['被执行人持有股权、其它投资权益的数额'],'被执行人证件种类':sml['被执行人证件种类'],'被执行人证件号码':sml['被执行人证件号码'],'冻结期限自':sml['冻结期限自'],'冻结期限至':sml['冻结期限至'],'冻结期限':sml['冻结期限'],'公示日期':sml['公示日期']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['股权冻结']=b
#         totalpage = int(driver.find_element_by_xpath('//*[@id="terminationCase"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="terminationCase"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="terminationCase"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="terminationCase"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['被执行人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['组织机构代码/身份证号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['立案时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['案号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['终本日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['执行法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['执行标的']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     b.append({i:{'被执行人':sml['被执行人'],'组织机构代码/身份证号':sml['组织机构代码/身份证号'],'立案时间':sml['立案时间'],'案号':sml['案号'],'终本日期':sml['终本日期'],'执行法院':sml['执行法院'],'执行标的':sml['执行标的']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['终本案件']=b
#         else:
#             tr_list = response.xpath('//*[@id="terminationCase"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="terminationCase"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['被执行人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['组织机构代码/身份证号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['立案时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['案号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['终本日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['执行法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['执行标的']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 b.append({i:{'被执行人':sml['被执行人'],'组织机构代码/身份证号':sml['组织机构代码/身份证号'],'立案时间':sml['立案时间'],'案号':sml['案号'],'终本日期':sml['终本日期'],'执行法院':sml['执行法院'],'执行标的':sml['执行标的']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['终本案件']=b
#         totalpage = int(driver.find_element_by_xpath('//*[@id="restrictedConsumer"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="restrictedConsumer"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="restrictedConsumer"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="restrictedConsumer"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['限消法人或组织']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['关联企业']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['立案时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['案号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['案由']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['申请执行人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['限制令发布日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['执行法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                     sml['附件']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/div/a').get_attribute('href')
#                     b.append({i:{'限消法人或组织':sml['限消法人或组织'],'关联企业':sml['关联企业'],'立案时间':sml['立案时间'],'案号':sml['案号'],'案由':sml['案由'],'申请执行人':sml['申请执行人'],'限制令发布日期':sml['限制令发布日期'],'执行法院':sml['执行法院'],'附件':sml['附件']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['限制高消费']=b
#         else:
#             tr_list = response.xpath('//*[@id="restrictedConsumer"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="restrictedConsumer"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['限消法人或组织']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['关联企业']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['立案时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['案号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['案由']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['申请执行人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['限制令发布日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['执行法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                 sml['附件']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/div/a').get_attribute('href')
#                 b.append({i:{'限消法人或组织':sml['限消法人或组织'],'关联企业':sml['关联企业'],'立案时间':sml['立案时间'],'案号':sml['案号'],'案由':sml['案由'],'申请执行人':sml['申请执行人'],'限制令发布日期':sml['限制令发布日期'],'执行法院':sml['执行法院'],'附件':sml['附件']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['限制高消费']=b
#         totalpage = int(driver.find_element_by_xpath('//*[@id="abnormal"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="abnormal"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="abnormal"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     sml['列入日期']=tr.xpath('./td[2]').extract()
#                     sml['做出决定机关']=tr.xpath('./td[3]/text()').extract()
#                     sml['列入经营异常名录原因']=tr.xpath('./td[4]/text()').extract()
#                     sml['移出日期']=tr.xpath('./td[5]/text()').extract()
#                     sml['移出经营异常名录原因']=tr.xpath('./td[6]/text()').extract()
#                     b.append({i:{'列入日期':sml['列入日期'],'做出决定机关':sml['做出决定机关'],'列入经营异常名录原因':sml['列入经营异常名录原因'],'移出日期':sml['移出日期'],'移出经营异常名录原因':sml['移出经营异常名录原因']}})
#                     i+=1
#                 mid['经营异常']=b
#         else:
#             tr_list = response.xpath('//*[@id="abnormal"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 sml['列入日期']=tr.xpath('./td[2]').extract()
#                 sml['做出决定机关']=tr.xpath('./td[3]/text()').extract()
#                 sml['列入经营异常名录原因']=tr.xpath('./td[4]/text()').extract()
#                 sml['移出日期']=tr.xpath('./td[5]/text()').extract()
#                 sml['移出经营异常名录原因']=tr.xpath('./td[6]/text()').extract()
#                 b.append({i:{'列入日期':sml['列入日期'],'做出决定机关':sml['做出决定机关'],'列入经营异常名录原因':sml['列入经营异常名录原因'],'移出日期':sml['移出日期'],'移出经营异常名录原因':sml['移出经营异常名录原因']}})
#                 i+=1
#             mid['经营异常']=b
#
#         totalpage = int(driver.find_element_by_xpath('//*[@id="execution"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="execution"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="execution"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="execution"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['被执行人姓名/名称']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['身份证号码/组织机构代码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['法定代表人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['发布日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['执行法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['省份']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['执行依据文号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['立案时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                     sml['案号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                     sml['做出执行依据单位']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                     sml['被执行人履行情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                     sml['生效法律文书确定的义务']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[2]').get_attribute('textContent')
#                     sml['失信被执行人为具体情形']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[8]/td[2]').get_attribute('textContent')
#                     b.append({i:{'被执行人姓名/名称':sml['被执行人姓名/名称'],'身份证号码/组织机构代码':sml['身份证号码/组织机构代码'],'法定代表人':sml['法定代表人'],'发布日期':sml['发布日期'],'执行法院':sml['执行法院'],'省份':sml['省份'],'执行依据文号':sml['执行依据文号'],'立案时间':sml['立案时间'],'案号':sml['案号'],'做出执行依据单位':sml['做出执行依据单位'],'被执行人履行情况':sml['被执行人履行情况'],'生效法律文书确定的义务':sml['生效法律文书确定的义务'],'失信被执行人为具体情形':sml['失信被执行人为具体情形']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['失信信息']=b
#         else:
#             tr_list = response.xpath('//*[@id="execution"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="execution"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['被执行人姓名/名称']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['身份证号码/组织机构代码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['法定代表人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['发布日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['执行法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['省份']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['执行依据文号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['立案时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                 sml['案号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                 sml['做出执行依据单位']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                 sml['被执行人履行情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                 sml['生效法律文书确定的义务']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[2]').get_attribute('textContent')
#                 sml['失信被执行人为具体情形']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[8]/td[2]').get_attribute('textContent')
#                 b.append({i:{'被执行人姓名/名称':sml['被执行人姓名/名称'],'身份证号码/组织机构代码':sml['身份证号码/组织机构代码'],'法定代表人':sml['法定代表人'],'发布日期':sml['发布日期'],'执行法院':sml['执行法院'],'省份':sml['省份'],'执行依据文号':sml['执行依据文号'],'立案时间':sml['立案时间'],'案号':sml['案号'],'做出执行依据单位':sml['做出执行依据单位'],'被执行人履行情况':sml['被执行人履行情况'],'生效法律文书确定的义务':sml['生效法律文书确定的义务'],'失信被执行人为具体情形':sml['失信被执行人为具体情形']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['失信信息']=b
#         totalpage = int(driver.find_element_by_xpath('//*[@id="tddy"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="tddy"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="tddy"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="tddy"]/table/tbody/tr[{0}]/td[6]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['土地编号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['行政区']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['土地面积（公顷）']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['抵押面积（公顷）']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['评估金额（万元）']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['抵押金额（万元）']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['土地位置']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['抵押土地用途']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                     sml['土地他项权利人证号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                     sml['土地使用权证号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                     sml['土地抵押人名称']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                     sml['土地抵押人性质']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[4]').get_attribute('textContent')
#                     sml['土地抵押权人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[7]/td[2]').get_attribute('textContent')
#                     sml['抵押土地权属性质与使用权类型']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[7]/td[4]').get_attribute('textContent')
#                     sml['土地抵押登记起始时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[8]/td[2]').get_attribute('textContent')
#                     sml['土地抵押登记结束时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[8]/td[4]').get_attribute('textContent')
#                     b.append({i:{'土地编号':sml['土地编号'],'行政区':sml['行政区'],'土地面积（公顷）':sml['土地面积（公顷）'],'抵押面积（公顷）':sml['抵押面积（公顷）'],'评估金额（万元）':sml['评估金额（万元）'] ,'抵押金额（万元）':sml['抵押金额（万元）'],'土地位置':sml['土地位置'],'抵押土地用途':sml['抵押土地用途'],'土地他项权利人证号':sml['土地他项权利人证号'],'土地使用权证号':sml['土地使用权证号'],'土地抵押人名称':sml['土地抵押人名称'],'土地抵押人性质':sml['土地抵押人性质'],'土地抵押权人':sml['土地抵押权人'],'抵押土地权属性质与使用权类型':sml['抵押土地权属性质与使用权类型'],'土地抵押登记起始时间':sml['土地抵押登记起始时间'],'土地抵押登记结束时间':sml['土地抵押登记结束时间']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['土地抵押']=b
#         else:
#             tr_list = response.xpath('//*[@id="tddy"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="tddy"]/table/tbody/tr[{0}]/td[6]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['土地编号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['行政区']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['土地面积（公顷）']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['抵押面积（公顷）']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['评估金额（万元）']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['抵押金额（万元）']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['土地位置']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['抵押土地用途']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                 sml['土地他项权利人证号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                 sml['土地使用权证号']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
#                 sml['土地抵押人名称']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                 sml['土地抵押人性质']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[4]').get_attribute('textContent')
#                 sml['土地抵押权人']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[7]/td[2]').get_attribute('textContent')
#                 sml['抵押土地权属性质与使用权类型']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[7]/td[4]').get_attribute('textContent')
#                 sml['土地抵押登记起始时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[8]/td[2]').get_attribute('textContent')
#                 sml['土地抵押登记结束时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[8]/td[4]').get_attribute('textContent')
#                 b.append({i:{'土地编号':sml['土地编号'],'行政区':sml['行政区'],'土地面积（公顷）':sml['土地面积（公顷）'],'抵押面积（公顷）':sml['抵押面积（公顷）'],'评估金额（万元）':sml['评估金额（万元）'] ,'抵押金额（万元）':sml['抵押金额（万元）'],'土地位置':sml['土地位置'],'抵押土地用途':sml['抵押土地用途'],'土地他项权利人证号':sml['土地他项权利人证号'],'土地使用权证号':sml['土地使用权证号'],'土地抵押人名称':sml['土地抵押人名称'],'土地抵押人性质':sml['土地抵押人性质'],'土地抵押权人':sml['土地抵押权人'],'抵押土地权属性质与使用权类型':sml['抵押土地权属性质与使用权类型'],'土地抵押登记起始时间':sml['土地抵押登记起始时间'],'土地抵押登记结束时间':sml['土地抵押登记结束时间']}})
#                 i+=1
#                 driver.find_ele
#             mid['土地抵押']=b
#         totalpage = int(driver.find_element_by_xpath('//*[@id="auction"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="auction"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="auction"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="auction"]/table/tbody/tr[{0}]/td[5]/div/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['起拍价']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['拍卖日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                     sml['处置法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['权利来源']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                     sml['权利限制情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['拍品介绍']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     b.append({i:{'起拍价':sml['起拍价'],'拍卖日期':sml['拍卖日期'],'处置法院':sml['处置法院'],'权利来源':sml['权利来源'],'权利限制情况':sml['权利限制情况'] ,'拍品介绍':sml['拍品介绍']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['司法拍卖']=b
#         else:
#             tr_list = response.xpath('//*[@id="auction"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="auction"]/table/tbody/tr[{0}]/td[5]/div/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['起拍价']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['拍卖日期']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
#                 sml['处置法院']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['权利来源']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
#                 sml['权利限制情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['拍品介绍']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 b.append({i:{'起拍价':sml['起拍价'],'拍卖日期':sml['拍卖日期'],'处置法院':sml['处置法院'],'权利来源':sml['权利来源'],'权利限制情况':sml['权利限制情况'] ,'拍品介绍':sml['拍品介绍']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['司法拍卖']=b
#         totalpage = int(driver.find_element_by_xpath('//*[@id="auction"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
#         print(totalpage)
#         if totalpage!=1:
#             for p in range(1,totalpage):
#                 if p <= 3:
#                     p=p
#                 elif p==totalpage:
#                     p=5
#                 else:
#                     p=4
#                 page = driver.find_element_by_xpath('//*[@id="auction"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
#                 driver.execute_script('arguments[0].click()', page)
#                 time.sleep(2)
#                 tr_list = response.xpath('//*[@id="overdueTax"]/table/tbody/tr')
#                 i=1
#                 b=[]
#                 for tr in tr_list:
#                     a = driver.find_element_by_xpath('//*[@id="overdueTax"]/table/tbody/tr[{0}]/td[5]/a'.format(i))
#                     driver.execute_script('arguments[0].click()',a)
#                     time.sleep(2)
#                     sml['财务负责人姓名、性别、身份证号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                     sml['负有直接责任的中介机构']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                     sml['发布时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                     sml['所属税务机关']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                     sml['检察机关']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                     sml['抓区税务局']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                     sml['案件性质']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                     sml['主要违法事实']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                     sml['相关法律依据及税务处理处罚情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[7]/td[2]').get_attribute('textContent')
#                     sml['移送公安情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[8]/td[2]').get_attribute('textContent')
#                     b.append({i:{'财务负责人姓名、性别、身份证号码':sml['财务负责人姓名、性别、身份证号码'],'负有直接责任的中介机构':sml['负有直接责任的中介机构'],'发布时间':sml['发布时间'],'所属税务机关':sml['所属税务机关'],'检察机关':sml['检察机关'] ,'抓区税务局':sml['抓区税务局'],'案件性质':sml['案件性质'],'主要违法事实':sml['主要违法事实'],'相关法律依据及税务处理处罚情况':sml['相关法律依据及税务处理处罚情况'],'移送公安情况':sml['移送公安情况']}})
#                     i+=1
#                     driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#                 mid['税务信息']=b
#         else:
#             tr_list = response.xpath('//*[@id="overdueTax"]/table/tbody/tr')
#             i=1
#             b=[]
#             for tr in tr_list:
#                 a = driver.find_element_by_xpath('//*[@id="overdueTax"]/table/tbody/tr[{0}]/td[5]/a'.format(i))
#                 driver.execute_script('arguments[0].click()',a)
#                 time.sleep(2)
#                 sml['财务负责人姓名、性别、身份证号码']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
#                 sml['负有直接责任的中介机构']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
#                 sml['发布时间']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
#                 sml['所属税务机关']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
#                 sml['检察机关']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
#                 sml['抓区税务局']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
#                 sml['案件性质']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
#                 sml['主要违法事实']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
#                 sml['相关法律依据及税务处理处罚情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[7]/td[2]').get_attribute('textContent')
#                 sml['移送公安情况']=driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[8]/td[2]').get_attribute('textContent')
#                 b.append({i:{'财务负责人姓名、性别、身份证号码':sml['财务负责人姓名、性别、身份证号码'],'负有直接责任的中介机构':sml['负有直接责任的中介机构'],'发布时间':sml['发布时间'],'所属税务机关':sml['所属税务机关'],'检察机关':sml['检察机关'] ,'抓区税务局':sml['抓区税务局'],'案件性质':sml['案件性质'],'主要违法事实':sml['主要违法事实'],'相关法律依据及税务处理处罚情况':sml['相关法律依据及税务处理处罚情况'],'移送公安情况':sml['移送公安情况']}})
#                 i+=1
#                 driver.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]').click()
#             mid['税务信息']=b
#         mid['司法协助']=[]
#         item['content'] = [{'裁判文书':mid['裁判文书'],'被执行人信息':mid['被执行人信息'],'开庭公告':mid['开庭公告'],'法院公告':mid['法院公告'],'失信信息':mid['失信信息'],'动产抵押':mid['动产抵押'],'税务信息':mid['税务信息'],'司法拍卖':mid['司法拍卖'],'股权出质':mid['股权出质'],'经营异常':mid['经营异常'],'行政处罚':mid['行政处罚'],'环保处罚':mid['环保处罚'],'股权冻结':mid['股权冻结'],'立案信息':mid['立案信息'],'土地抵押':mid['土地抵押'],'终本案件':mid['终本案件'],'限制高消费':mid['限制高消费'],'司法协助':mid['司法协助']}]
#         driver.close()
#         yield item