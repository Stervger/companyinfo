# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from companyinfo.items import CompanyinfoItem


class OperationSpider(scrapy.Spider):
    name = 'operation'
    headers = {
        'Host': 'www.qixin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    }
    start_urls = {'https://www.qixin.com/operation/5cc0ecc5-0920-4e9e-ae89-d8d5043e3da0'}

    def parse(self, response):
        drive = webdriver.Chrome()
        drive.get("https://www.qixin.com/operation/5cc0ecc5-0920-4e9e-ae89-d8d5043e3da0")
        items = CompanyinfoItem()

        #融资信息
        # totalpnum = int(drive.find_element_by_xpath('//*[@id="financeData"]/h4/span').get_attribute('textContent'))
        # if totalpnum != 0:
        #     financeData_detail = {}
        #     i = 1
        #     financeData = []
        #     tr_list = response.xpath('//*[@id="financeData"]/table/tbody/tr')
        #     for tr in tr_list:
        #         time.sleep(2)
        #         financeData_detail['融资时间'] = drive.find_element_by_xpath('//*[@id="financeData"]/table/tbody/tr[{0}]/td[1]'.format(i)).get_attribute('textContent')
        #         financeData_detail['融资轮次'] = drive.find_element_by_xpath('//*[@id="financeData"]/table/tbody/tr[{0}]/td[2]'.format(i)).get_attribute('textContent')
        #         financeData_detail['融资金额'] = drive.find_element_by_xpath('//*[@id="financeData"]/table/tbody/tr[{0}]/td[3]'.format(i)).get_attribute('textContent')
        #         financeData_detail['投资方'] = drive.find_element_by_xpath('//*[@id="financeData"]/table/tbody/tr[{0}]/td[4]'.format(i)).get_attribute('textContent')
        #         financeData.append({i: {'融资时间': financeData_detail['融资时间'], '融资轮次': financeData_detail['融资轮次'], '融资金额': financeData_detail['融资金额'], '投资方': financeData_detail['投资方']}})
        #         i += 1
        #     print(financeData)
        #     items['融资信息'] = financeData
        #     yield items
        # else:
        #     items['融资信息'] = ''
        #     yield items


        #质权人
        # totalnum=int(drive.find_element_by_xpath('//*[@id="pawneeInfo"]/h4/span').get_attribute('textContent'))
        # if totalnum==5:
        #     totalpage=1
        # else:
        #     totalpage = totalnum // 5 + 1
        # lastpagenum=totalnum%5
        # print(totalpage)
        # if totalpage!=1:
        #     for p in range(1,totalpage+1):
        #         if p <= 3:
        #             p=p
        #         elif p==totalpage:
        #             p=5
        #         else:
        #             p=4
        #         page = drive.find_element_by_xpath('//*[@id="pawneeInfo"]/div/div/nav/ul/li[{0}]/a'.format(p+1))
        #         drive.execute_script('arguments[0].click()', page)
        #         time.sleep(2)
        #         pawneeInfo_detail = {}
        #         i = 1
        #         pawneeInfo = []
        #         tr_list = response.xpath('//*[@id="pawneeInfo"]/table/tbody/tr')
        #         trlenth = len(tr_list)
        #         if lastpagenum==0:
        #             trlenth = trlenth
        #         elif p == totalpage:
        #             trlenth = lastpagenum
        #         for tr in range(trlenth):
        #             detail = drive.find_element_by_xpath('//*[@id="pawneeInfo"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
        #             drive.execute_script('arguments[0].click()', detail)
        #             time.sleep(2)
        #             pawneeInfo_detail['登记日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
        #             pawneeInfo_detail['状态'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
        #             pawneeInfo_detail['出质人名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('textContent')
        #             pawneeInfo_detail['出质人详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('href')
        #             pawneeInfo_detail['出质人'] = {'出质人名称': pawneeInfo_detail['出质人名称'],'出质人详情': pawneeInfo_detail['出质人详情']}
        #             pawneeInfo_detail['出质股权数'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
        #             pawneeInfo_detail['出质人证件号码'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
        #             pawneeInfo_detail['登记编号'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
        #             pawneeInfo_detail['标的方名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('textContent')
        #             pawneeInfo_detail['标的方详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('href')
        #             pawneeInfo_detail['标的方'] = {'标的方名称':pawneeInfo_detail['标的方名称'],'标的方详情':pawneeInfo_detail['标的方详情']}
        #             pawneeInfo_detail['质权人名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('textContent')
        #             pawneeInfo_detail['质权人详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('href')
        #             pawneeInfo_detail['质权人'] = {'质权人名称':pawneeInfo_detail['质权人名称'],'质权人详情':pawneeInfo_detail['质权人详情']}
        #             pawneeInfo_detail['质权人证件号码'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
        #             pawneeInfo_detail['备注'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
        #             close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
        #             drive.execute_script('arguments[0].click()', close)
        #             pawneeInfo.append({i: {'登记日期': pawneeInfo_detail['登记日期'], '状态': pawneeInfo_detail['状态'], '出质人': pawneeInfo_detail['出质人'], '出质股权数': pawneeInfo_detail['出质股权数'],'出质人证件号码': pawneeInfo_detail['出质人证件号码'], '登记编号': pawneeInfo_detail['登记编号'], '标的方': pawneeInfo_detail['标的方'], '质权人': pawneeInfo_detail['质权人'],'质权人证件号码': pawneeInfo_detail['质权人证件号码'], '备注': pawneeInfo_detail['备注']}})
        #             i += 1
        #         print(pawneeInfo)
        #         items['质权人'] = pawneeInfo
        #         yield items
        # else:
        #     pawneeInfo_detail = {}
        #     i = 1
        #     pawneeInfo = []
        #     tr_list = response.xpath('//*[@id="pawneeInfo"]/table/tbody/tr')
        #     for tr in tr_list:
        #         detail = drive.find_element_by_xpath('//*[@id="pawneeInfo"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
        #         drive.execute_script('arguments[0].click()', detail)
        #         time.sleep(2)
        #         pawneeInfo_detail['登记日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
        #         pawneeInfo_detail['状态'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
        #         pawneeInfo_detail['出质人名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('textContent')
        #         pawneeInfo_detail['出质人详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('href')
        #         pawneeInfo_detail['出质人'] = {'出质人名称': pawneeInfo_detail['出质人名称'],'出质人详情': pawneeInfo_detail['出质人详情']}
        #         pawneeInfo_detail['出质股权数'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
        #         pawneeInfo_detail['出质人证件号码'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
        #         pawneeInfo_detail['登记编号'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
        #         pawneeInfo_detail['标的方名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('textContent')
        #         pawneeInfo_detail['标的方详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('href')
        #         pawneeInfo_detail['标的方'] = {'标的方名称':pawneeInfo_detail['标的方名称'],'标的方详情':pawneeInfo_detail['标的方详情']}
        #         pawneeInfo_detail['质权人名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('textContent')
        #         pawneeInfo_detail['质权人详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('href')
        #         pawneeInfo_detail['质权人'] = {'质权人名称':pawneeInfo_detail['质权人名称'],'质权人详情':pawneeInfo_detail['质权人详情']}
        #         pawneeInfo_detail['质权人证件号码'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
        #         pawneeInfo_detail['备注'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
        #         close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
        #         drive.execute_script('arguments[0].click()', close)
        #         pawneeInfo.append({i: {'登记日期': pawneeInfo_detail['登记日期'], '状态': pawneeInfo_detail['状态'], '出质人': pawneeInfo_detail['出质人'], '出质股权数': pawneeInfo_detail['出质股权数'],'出质人证件号码': pawneeInfo_detail['出质人证件号码'], '登记编号': pawneeInfo_detail['登记编号'], '标的方': pawneeInfo_detail['标的方'], '质权人': pawneeInfo_detail['质权人'],'质权人证件号码': pawneeInfo_detail['质权人证件号码'], '备注': pawneeInfo_detail['备注']}})
        #         i += 1
        #     print(pawneeInfo)
        #     items['质权人'] = pawneeInfo
        #     yield items

        #行政许可
        # totalnum=int(drive.find_element_by_xpath('//*[@id="admLicense"]/h4/span').get_attribute('textContent'))
        # if totalnum==5:
        #     totalpage=1
        # else:
        #     totalpage = totalnum // 5 + 1
        # lastpagenum=totalnum%5
        # print(totalpage)
        # if totalpage!=1:
        #     for p in range(1,totalpage+1):
        #         if p <= 3:
        #             p=p
        #         elif p==totalpage:
        #             p=5
        #         else:
        #             p=4
        #         page = drive.find_element_by_xpath('//*[@id="admLicense"]/div/div/nav/ul/li[{0}]/a'.format(p+1))
        #         drive.execute_script('arguments[0].click()', page)
        #         time.sleep(2)
        #         admLicense_detail = {}
        #         i = 1
        #         admLicense = []
        #         tr_list = response.xpath('//*[@id="admLicense"]/table/tbody/tr')
        #         trlenth = len(tr_list)
        #         if lastpagenum==0:
        #             trlenth = trlenth
        #         elif p == totalpage:
        #             trlenth = lastpagenum
        #         for tr in range(trlenth):
        #             detail = drive.find_element_by_xpath('//*[@id="admLicense"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
        #             drive.execute_script('arguments[0].click()', detail)
        #             time.sleep(2)
        #             admLicense_detail['许可文件编号'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
        #             admLicense_detail['许可文件名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
        #             admLicense_detail['有效期自'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
        #             admLicense_detail['有效期至'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
        #             admLicense_detail['许可机关'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
        #             admLicense_detail['许可内容'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
        #             close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
        #             drive.execute_script('arguments[0].click()', close)
        #             admLicense.append({i: {'登记日期': admLicense_detail['许可文件编号'], '许可文件名称': admLicense_detail['许可文件名称'], '有效期自': admLicense_detail['有效期自'], '有效期至': admLicense_detail['有效期至'],'许可机关': admLicense_detail['许可机关'], '许可内容': admLicense_detail['许可内容']}})
        #             i += 1
        #         print(admLicense)
        #         items['行政许可'] = admLicense
        #         yield items
        # else:
        #     admLicense_detail = {}
        #     i = 1
        #     admLicense = []
        #     tr_list = response.xpath('//*[@id="admLicense"]/table/tbody/tr')
        #     for tr in tr_list:
        #         detail = drive.find_element_by_xpath('//*[@id="admLicense"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
        #         drive.execute_script('arguments[0].click()', detail)
        #         time.sleep(2)
        #         admLicense_detail['许可文件编号'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
        #         admLicense_detail['许可文件名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
        #         admLicense_detail['有效期自'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
        #         admLicense_detail['有效期至'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
        #         admLicense_detail['许可机关'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
        #         admLicense_detail['许可内容'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]').get_attribute('textContent')
        #         close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
        #         drive.execute_script('arguments[0].click()', close)
        #         admLicense.append({i: {'登记日期': admLicense_detail['许可文件编号'], '许可文件名称': admLicense_detail['许可文件名称'], '有效期自': admLicense_detail['有效期自'], '有效期至': admLicense_detail['有效期至'],'许可机关': admLicense_detail['许可机关'], '许可内容': admLicense_detail['许可内容']}})
        #         i += 1
        #     print(admLicense)
        #     items['行政许可'] = admLicense
        #     yield items

        #税务评级
        # totalnum = int(drive.find_element_by_xpath('//*[@id="tax"]/h4/span').get_attribute('textContent'))
        # if totalnum==5:
        #     totalpage=1
        # else:
        #     totalpage = totalnum // 5 + 1
        # lastpagenum=totalnum%5
        # print(totalpage)
        # if totalpage != 1:
        #     for p in range(1, totalpage+1):
        #         if p <= 3:
        #             p = p
        #         elif p == totalpage:
        #             p = 5
        #         else:
        #             p = 4
        #         page = drive.find_element_by_xpath('//*[@id="tax"]/div/div/nav/ul/li[{0}]/a'.format(p + 1))
        #         drive.execute_script('arguments[0].click()', page)
        #         time.sleep(2)
        #         tax_detail = {}
        #         i = 1
        #         tax = []
        #         tr_list = response.xpath('//*[@id="tax"]/table/tbody/tr')
        #         trlenth = len(tr_list)
        #         if lastpagenum == 0:
        #             trlenth = trlenth
        #         elif p == totalpage:
        #             trlenth = lastpagenum
        #         for tr in range(trlenth):
        #             time.sleep(2)
        #             tax_detail['评价年度'] = drive.find_element_by_xpath('//*[@id="tax"]/table/tbody/tr[{0}]/td[2]'.format(i)).get_attribute('textContent')
        #             tax_detail['纳税人信用级别'] = drive.find_element_by_xpath('//*[@id="tax"]/table/tbody/tr[{0}]/td[3]'.format(i)).get_attribute('textContent')
        #             tax_detail['纳税人名称'] = drive.find_element_by_xpath('//*[@id="tax"]/table/tbody/tr[{0}]/td[4]'.format(i)).get_attribute('textContent')
        #             tax_detail['纳税人识别号'] = drive.find_element_by_xpath('//*[@id="tax"]/table/tbody/tr[{0}]/td[5]'.format(i)).get_attribute('textContent')
        #             tax.append({i: {'评价年度': tax_detail['评价年度'], '纳税人信用级别': tax_detail['纳税人信用级别'], '纳税人名称': tax_detail['纳税人名称'], '纳税人识别号': tax_detail['纳税人识别号']}})
        #             i += 1
        #         print(tax)
        #         items['税务评级'] = tax
        #         yield items
        # else:
        #     tax_detail = {}
        #     i = 1
        #     tax = []
        #     tr_list = response.xpath('//*[@id="copyRightSoft"]/table/tbody/tr')
        #     for tr in tr_list:
        #         time.sleep(2)
        #         tax_detail['评价年度'] = drive.find_element_by_xpath('//*[@id="tax"]/table/tbody/tr[{0}]/td[2]'.format(i)).get_attribute('textContent')
        #         tax_detail['纳税人信用级别'] = drive.find_element_by_xpath('//*[@id="tax"]/table/tbody/tr[{0}]/td[3]'.format(i)).get_attribute('textContent')
        #         tax_detail['纳税人名称'] = drive.find_element_by_xpath('//*[@id="tax"]/table/tbody/tr[{0}]/td[4]'.format(i)).get_attribute('textContent')
        #         tax_detail['纳税人识别号'] = drive.find_element_by_xpath('//*[@id="tax"]/table/tbody/tr[{0}]/td[5]'.format(i)).get_attribute('textContent')
        #         tax.append({i: {'评价年度': tax_detail['评价年度'], '纳税人信用级别': tax_detail['纳税人信用级别'],'纳税人名称': tax_detail['纳税人名称'], '纳税人识别号': tax_detail['纳税人识别号']}})
        #         i += 1
        #     print(tax)
        #     items['税务评级'] = tax
        #     yield items

        #新闻动态
        # totalnum = int(drive.find_element_by_xpath('//*[@id="news"]/h4/span').get_attribute('textContent'))
        # if totalnum==5:
        #     totalpage=1
        # else:
        #     totalpage = totalnum // 5 + 1
        # lastpagenum=totalnum%5
        # print(totalpage)
        # if totalpage != 1:
        #     for p in range(1, totalpage+1):
        #         if p <= 3:
        #             p = p
        #         elif p == totalpage:
        #             p = 5
        #         else:
        #             p = 4
        #         page = drive.find_element_by_xpath('//*[@id="news"]/div[2]/div/nav/ul/li[{0}]/a'.format(p + 1))
        #         drive.execute_script('arguments[0].click()', page)
        #         time.sleep(2)
        #         news_detail = {}
        #         i = 1
        #         news = []
        #         tr_list = response.xpath('//*[@id="news"]/div[1]/div/div')
        #         trlenth = len(tr_list)
        #         if lastpagenum == 0:
        #             trlenth = trlenth
        #         elif p == totalpage:
        #             trlenth = lastpagenum
        #         for tr in range(trlenth):
        #             time.sleep(2)
        #             news_detail['新闻标题'] = drive.find_element_by_xpath('//*[@id="news"]/div[1]/div/div[{0}]/a[1]/div'.format(i)).get_attribute('textContent')
        #             news_detail['新闻概要'] = drive.find_element_by_xpath('//*[@id="news"]/div[1]/div/div[{0}]/p[2]'.format(i)).get_attribute('textContent')
        #             news_detail['时间来源'] = drive.find_element_by_xpath('//*[@id="news"]/div[1]/div/div[{0}]/p[1]/small'.format(i)).get_attribute('textContent')
        #             news_detail['详情连接'] = drive.find_element_by_xpath('//*[@id="news"]/div[1]/div/div[{0}]/a[2]'.format(i)).get_attribute('textContent')
        #             news.append({i: {'新闻标题': news_detail['新闻标题'], '新闻概要': news_detail['新闻概要'], '详情连接': news_detail['详情连接']}})
        #             i += 1
        #         print(news)
        #         items['新闻动态'] = news
        #         yield items
        # else:
        #     news_detail = {}
        #     i = 1
        #     news = []
        #     tr_list = response.xpath('//*[@id="news"]/div[1]/div/div')
        #     for tr in tr_list:
        #         time.sleep(2)
        #         news_detail['新闻标题'] = drive.find_element_by_xpath('//*[@id="news"]/div[1]/div/div[{0}]/a[1]/div'.format(i)).get_attribute('textContent')
        #         news_detail['新闻概要'] = drive.find_element_by_xpath('//*[@id="news"]/div[1]/div/div[{0}]/p[2]'.format(i)).get_attribute('textContent')
        #         news_detail['时间来源'] = drive.find_element_by_xpath('//*[@id="news"]/div[1]/div/div[{0}]/p[1]/small'.format(i)).get_attribute('textContent')
        #         news_detail['详情连接'] = drive.find_element_by_xpath('//*[@id="news"]/div[1]/div/div[{0}]/a[2]'.format(i)).get_attribute('textContent')
        #         news.append({i: {'新闻标题': news_detail['新闻标题'], '新闻概要': news_detail['新闻概要'], '详情连接': news_detail['详情连接']}})
        #         i += 1
        #     print(news)
        #     items['新闻动态'] = news
        #     yield items


        #招聘信息
        # totalnum = int(drive.find_element_by_xpath('//*[@id="job"]/h4/span').get_attribute('textContent'))
        # if totalnum == 10:
        #     totalpage = 1
        # else:
        #     totalpage = totalnum // 10 + 1
        # lastpagenum = totalnum % 10
        # print(totalpage)
        # if totalpage!=1:
        #     for p in range(1,totalpage+1):
        #         if p <= 3:
        #             p=p
        #         elif p==totalpage:
        #             p=5
        #         else:
        #             p=4
        #         page = drive.find_element_by_xpath('//*[@id="job"]/div/div/nav/ul/li[{0}]/a'.format(p+1))
        #         drive.execute_script('arguments[0].click()', page)
        #         time.sleep(2)
        #         job_detail = {}
        #         i = 1
        #         job = []
        #         tr_list = response.xpath('//*[@id="job"]/table/tbody/tr')
        #         trlenth = len(tr_list)
        #         if lastpagenum == 0:
        #             trlenth = trlenth
        #         elif p == totalpage:
        #             trlenth = lastpagenum
        #         for tr in range(trlenth):
        #             detail = drive.find_element_by_xpath('//*[@id="job"]/table/tbody/tr[{0}]/td[8]/a'.format(i))
        #             drive.execute_script('arguments[0].click()', detail)
        #             time.sleep(2)
        #             job_detail['职位名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
        #             job_detail['发布日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
        #             job_detail['工作地点'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
        #             job_detail['薪资待遇'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
        #             job_detail['学历要求'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
        #             job_detail['工作经验'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[4]').get_attribute('textContent')
        #             job_detail['工作类型'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]').get_attribute('textContent')
        #             job_detail['年龄要求'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[4]').get_attribute('textContent')
        #             job_detail['招聘人数'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
        #             job_detail['信息来源'] = {'来源名称':job_detail['来源名称'],'来源链接':job_detail['来源链接']}
        #             job_detail['来源名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[4]/a').get_attribute('textContent')
        #             job_detail['来源链接'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[4]/a').get_attribute('href')
        #             job_detail['职位描述'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
        #             close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
        #             drive.execute_script('arguments[0].click()', close)
        #             job.append({i: {'职位名称': job_detail['职位名称'], '发布日期': job_detail['发布日期'], '工作地点': job_detail['工作地点'], '薪资待遇': job_detail['薪资待遇'],'学历要求': job_detail['学历要求'], '工作经验': job_detail['工作经验'], '工作类型': job_detail['工作类型'], '年龄要求': job_detail['年龄要求'],'招聘人数': job_detail['招聘人数'], '信息来源': job_detail['信息来源'], '职位描述': job_detail['职位描述']}})
        #             i += 1
        #         print(job)
        #         items['商标'] = job
        #         yield items
        # else:
        #     job_detail = {}
        #     i = 1
        #     job = []
        #     tr_list = response.xpath('//*[@id="job"]/table/tbody/tr')
        #     for tr in tr_list:
        #         detail = drive.find_element_by_xpath('//*[@id="job"]/table/tbody/tr[{0}]/td[8]/a'.format(i))
        #         drive.execute_script('arguments[0].click()', detail)
        #         time.sleep(2)
        #         job_detail['职位名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]').get_attribute('textContent')
        #         job_detail['发布日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[1]/td[4]').get_attribute('textContent')
        #         job_detail['工作地点'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]').get_attribute('textContent')
        #         job_detail['薪资待遇'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[2]/td[4]').get_attribute('textContent')
        #         job_detail['学历要求'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]').get_attribute('textContent')
        #         job_detail['工作经验'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[3]/td[4]').get_attribute('textContent')
        #         job_detail['工作类型'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]').get_attribute('textContent')
        #         job_detail['年龄要求'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[4]/td[4]').get_attribute('textContent')
        #         job_detail['招聘人数'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
        #         job_detail['来源名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[4]/a').get_attribute('textContent')
        #         job_detail['来源链接'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[4]/a').get_attribute('href')
        #         job_detail['信息来源'] = {'来源名称': job_detail['来源名称'], '来源链接': job_detail['来源链接']}
        #         job_detail['职位描述'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
        #         close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
        #         drive.execute_script('arguments[0].click()', close)
        #         job.append({i: {'职位名称': job_detail['职位名称'], '发布日期': job_detail['发布日期'], '工作地点': job_detail['工作地点'],'薪资待遇': job_detail['薪资待遇'], '学历要求': job_detail['学历要求'], '工作经验': job_detail['工作经验'],'工作类型': job_detail['工作类型'], '年龄要求': job_detail['年龄要求'], '招聘人数': job_detail['招聘人数'],'信息来源': job_detail['信息来源'], '职位描述': job_detail['职位描述']}})
        #         i += 1
        #     print(job)
        #     items['招聘信息'] = job
        #     yield items

        #地块公示
        totalnum = int(drive.find_element_by_xpath('//*[@id="tdgs"]/h4/span').get_attribute('textContent'))
        if totalnum == 5:
            totalpage = 1
        else:
            totalpage = totalnum // 5 + 1
        lastpagenum = totalnum % 5
        print(totalpage)
        if totalpage!=1:
            for p in range(1,totalpage+1):
                if p <= 3:
                    p=p
                elif p==totalpage:
                    p=5
                else:
                    p=4
                page = drive.find_element_by_xpath('//*[@id="tdgs"]/div/div/nav/ul/li[{0}]/a'.format(p+1))
                drive.execute_script('arguments[0].click()', page)
                time.sleep(2)
                tdgs_detail = {}
                i = 1
                tdgs = []
                tr_list = response.xpath('//*[@id="tdgs"]/table/tbody/tr')
                trlenth = len(tr_list)
                if lastpagenum == 0:
                    trlenth = trlenth
                elif p == totalpage:
                    trlenth = lastpagenum
                for tr in range(trlenth):
                    detail = drive.find_element_by_xpath('//*[@id="tdgs"]/table/tbody/tr[{0}]/td[6]/a'.format(i))
                    drive.execute_script('arguments[0].click()', detail)
                    time.sleep(2)
                    tdgs_detail['土地编号'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
                    tdgs_detail['发布日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
                    tdgs_detail['土地面积（公顷）'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
                    tdgs_detail['行政区'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
                    tdgs_detail['土地位置'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
                    tdgs_detail['项目名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
                    tdgs_detail['受让单位'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/p/a').get_attribute('textContent')
                    tdgs_detail['土地用途'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
                    tdgs_detail['公示开始日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
                    tdgs_detail['公示结束日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
                    close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
                    drive.execute_script('arguments[0].click()', close)
                    tdgs.append({i: {'土地编号': tdgs_detail['土地编号'], '发布日期': tdgs_detail['发布日期'], '土地面积（公顷）': tdgs_detail['土地面积（公顷）'], '行政区': tdgs_detail['行政区'],'土地位置': tdgs_detail['土地位置'], '项目名称': tdgs_detail['项目名称'], '受让单位': tdgs_detail['受让单位'], '土地用途': tdgs_detail['土地用途'],'公示开始日期': tdgs_detail['公示开始日期'], '公示结束日期': tdgs_detail['公示结束日期']}})
                    i += 1
                print(tdgs)
                items['地块公示'] = tdgs
                yield items
        else:
            tdgs_detail = {}
            i = 1
            tdgs = []
            tr_list = response.xpath('//*[@id="tdgs"]/table/tbody/tr')
            for tr in tr_list:
                detail = drive.find_element_by_xpath('//*[@id="tdgs"]/table/tbody/tr[{0}]/td[6]/a'.format(i))
                drive.execute_script('arguments[0].click()', detail)
                time.sleep(2)
                tdgs_detail['土地编号'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
                tdgs_detail['发布日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
                tdgs_detail['土地面积（公顷）'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]').get_attribute('textContent')
                tdgs_detail['行政区'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
                tdgs_detail['土地位置'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
                tdgs_detail['项目名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
                tdgs_detail['受让单位'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/p/a').get_attribute('textContent')
                tdgs_detail['土地用途'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[4]').get_attribute('textContent')
                tdgs_detail['公示开始日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]').get_attribute('textContent')
                tdgs_detail['公示结束日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
                close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
                drive.execute_script('arguments[0].click()', close)
                tdgs.append({i: {'土地编号': tdgs_detail['土地编号'], '发布日期': tdgs_detail['发布日期'],'土地面积（公顷）': tdgs_detail['土地面积（公顷）'], '行政区': tdgs_detail['行政区'],'土地位置': tdgs_detail['土地位置'], '项目名称': tdgs_detail['项目名称'], '受让单位': tdgs_detail['受让单位'],'土地用途': tdgs_detail['土地用途'], '公示开始日期': tdgs_detail['公示开始日期'],'公示结束日期': tdgs_detail['公示结束日期']}})
                i += 1
            print(tdgs)
            items['地块公示'] = tdgs
            yield items

        drive.close()