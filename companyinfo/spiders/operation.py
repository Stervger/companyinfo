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
    start_urls = {'https://www.qixin.com/operation/0398b081-6676-4a91-856b-abbabaee5e70'}

    def parse(self, response):
        drive = webdriver.Chrome()
        drive.get("https://www.qixin.com/operation/0398b081-6676-4a91-856b-abbabaee5e70")
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
        totalpage = int(drive.find_element_by_xpath('//*[@id="pawneeInfo"]/h4/span').get_attribute('textContent'))//5 + 1
        print(totalpage)
        if totalpage!=1:
            for p in range(1,totalpage+1):
                if p <= 3:
                    p=p
                elif p==totalpage:
                    p=5
                else:
                    p=4
                page = drive.find_element_by_xpath('//*[@id="pawneeInfo"]/div/div/nav/ul/li[{0}]/a'.format(p+1))
                drive.execute_script('arguments[0].click()', page)
                time.sleep(2)
                pawneeInfo_detail = {}
                i = 1
                pawneeInfo = []
                tr_list = response.xpath('//*[@id="pawneeInfo"]/table/tbody/tr')
                for tr in tr_list:
                    detail = drive.find_element_by_xpath('//*[@id="pawneeInfo"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
                    drive.execute_script('arguments[0].click()', detail)
                    time.sleep(2)
                    pawneeInfo_detail['登记日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
                    pawneeInfo_detail['状态'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
                    pawneeInfo_detail['出质人名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('textContent')
                    pawneeInfo_detail['出质人详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('href')
                    pawneeInfo_detail['出质人'] = {'出质人名称': pawneeInfo_detail['出质人名称'],'出质人详情': pawneeInfo_detail['出质人详情']}
                    pawneeInfo_detail['出质股权数'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
                    pawneeInfo_detail['出质人证件号码'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
                    pawneeInfo_detail['登记编号'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
                    pawneeInfo_detail['标的方名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('textContent')
                    pawneeInfo_detail['标的方详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('href')
                    pawneeInfo_detail['标的方'] = {'标的方名称':pawneeInfo_detail['标的方名称'],'标的方详情':pawneeInfo_detail['标的方详情']}
                    pawneeInfo_detail['质权人名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('textContent')
                    pawneeInfo_detail['质权人详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('href')
                    pawneeInfo_detail['质权人'] = {'质权人名称':pawneeInfo_detail['质权人名称'],'质权人详情':pawneeInfo_detail['质权人详情']}
                    pawneeInfo_detail['质权人证件号码'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
                    pawneeInfo_detail['备注'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
                    close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
                    drive.execute_script('arguments[0].click()', close)
                    pawneeInfo.append({i: {'登记日期': pawneeInfo_detail['登记日期'], '状态': pawneeInfo_detail['状态'], '出质人': pawneeInfo_detail['出质人'], '出质股权数': pawneeInfo_detail['出质股权数'],'出质人证件号码': pawneeInfo_detail['出质人证件号码'], '登记编号': pawneeInfo_detail['登记编号'], '标的方': pawneeInfo_detail['标的方'], '质权人': pawneeInfo_detail['质权人'],'质权人证件号码': pawneeInfo_detail['质权人证件号码'], '备注': pawneeInfo_detail['备注']}})
                    i += 1
                print(pawneeInfo)
                items['质权人'] = pawneeInfo
                yield items
        else:
            pawneeInfo_detail = {}
            i = 1
            pawneeInfo = []
            tr_list = response.xpath('//*[@id="pawneeInfo"]/table/tbody/tr')
            for tr in tr_list:
                detail = drive.find_element_by_xpath('//*[@id="pawneeInfo"]/table/tbody/tr[{0}]/td[7]/a'.format(i))
                drive.execute_script('arguments[0].click()', detail)
                time.sleep(2)
                pawneeInfo_detail['登记日期'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[2]').get_attribute('textContent')
                pawneeInfo_detail['状态'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[1]/td[4]').get_attribute('textContent')
                pawneeInfo_detail['出质人名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('textContent')
                pawneeInfo_detail['出质人详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[2]/a').get_attribute('href')
                pawneeInfo_detail['出质人'] = {'出质人名称': pawneeInfo_detail['出质人名称'],'出质人详情': pawneeInfo_detail['出质人详情']}
                pawneeInfo_detail['出质股权数'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[2]/td[4]').get_attribute('textContent')
                pawneeInfo_detail['出质人证件号码'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[2]').get_attribute('textContent')
                pawneeInfo_detail['登记编号'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[3]/td[4]').get_attribute('textContent')
                pawneeInfo_detail['标的方名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('textContent')
                pawneeInfo_detail['标的方详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[4]/td[2]/a').get_attribute('href')
                pawneeInfo_detail['标的方'] = {'标的方名称':pawneeInfo_detail['标的方名称'],'标的方详情':pawneeInfo_detail['标的方详情']}
                pawneeInfo_detail['质权人名称'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('textContent')
                pawneeInfo_detail['质权人详情'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[2]/a').get_attribute('href')
                pawneeInfo_detail['质权人'] = {'质权人名称':pawneeInfo_detail['质权人名称'],'质权人详情':pawneeInfo_detail['质权人详情']}
                pawneeInfo_detail['质权人证件号码'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[5]/td[4]').get_attribute('textContent')
                pawneeInfo_detail['备注'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/table/tbody/tr[6]/td[2]').get_attribute('textContent')
                close = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[1]/div[1]')
                drive.execute_script('arguments[0].click()', close)
                pawneeInfo.append({i: {'登记日期': pawneeInfo_detail['登记日期'], '状态': pawneeInfo_detail['状态'], '出质人': pawneeInfo_detail['出质人'], '出质股权数': pawneeInfo_detail['出质股权数'],'出质人证件号码': pawneeInfo_detail['出质人证件号码'], '登记编号': pawneeInfo_detail['登记编号'], '标的方': pawneeInfo_detail['标的方'], '质权人': pawneeInfo_detail['质权人'],'质权人证件号码': pawneeInfo_detail['质权人证件号码'], '备注': pawneeInfo_detail['备注']}})
                i += 1
            print(pawneeInfo)
            items['质权人'] = pawneeInfo
            yield items

        #行政许可
        # totalpage = int(drive.find_element_by_xpath('//*[@id="admLicense"]/h4/span').get_attribute('textContent')) // 5 + 1
        # print(totalpage)
        # if totalpage!=1:
        #     for p in range(1,totalpage+1):
        #         # if totalpage<6:
        #         #     p=p
        #         #     print('aaa')
        #         # else:
        #         #     print('bbb')
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
        #         for tr in tr_list:
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

        drive.close()