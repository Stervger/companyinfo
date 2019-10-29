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
    start_urls = {'https://www.qixin.com/operation/01c71ec5-d063-4bf7-896d-4418e8848931'}

    def parse(self, response):
        drive = webdriver.Chrome()
        drive.get("https://www.qixin.com/operation/01c71ec5-d063-4bf7-896d-4418e8848931")
        items = CompanyinfoItem()

        #融资信息
        totalpnum = int(drive.find_element_by_xpath('//*[@id="financeData"]/h4/span').get_attribute('textContent'))
        if totalpnum != 0:
            financeData_detail = {}
            i = 1
            financeData = []
            tr_list = response.xpath('//*[@id="financeData"]/table/tbody/tr')
            for tr in tr_list:
                time.sleep(2)
                financeData_detail['融资时间'] = drive.find_element_by_xpath('//*[@id="financeData"]/table/tbody/tr[{0}]/td[1]'.format(i)).get_attribute('textContent')
                financeData_detail['融资轮次'] = drive.find_element_by_xpath('//*[@id="financeData"]/table/tbody/tr[{0}]/td[2]'.format(i)).get_attribute('textContent')
                financeData_detail['融资金额'] = drive.find_element_by_xpath('//*[@id="financeData"]/table/tbody/tr[{0}]/td[3]'.format(i)).get_attribute('textContent')
                financeData_detail['投资方'] = drive.find_element_by_xpath('//*[@id="financeData"]/table/tbody/tr[{0}]/td[4]'.format(i)).get_attribute('textContent')
                financeData.append({i: {'融资时间': financeData_detail['融资时间'], '融资轮次': financeData_detail['融资轮次'], '融资金额': financeData_detail['融资金额'], '投资方': financeData_detail['投资方']}})
                i += 1
            print(financeData)
            items['融资信息'] = financeData
            yield items
        else:
            items['融资信息'] = ''
            yield items


        #质权人
        # totalpage = int(drive.find_element_by_xpath('//*[@id="trademark"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
        # print(totalpage)
        # if totalpage!=1:
        #     for p in range(1,totalpage):
        #         if p <= 3:
        #             p=p
        #         elif p==totalpage:
        #             p=5
        #         else:
        #             p=4
        #         page = drive.find_element_by_xpath('//*[@id="trademark"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
        #         drive.execute_script('arguments[0].click()', page)
        #         time.sleep(2)
        #         trademark_detail = {}
        #         i = 1
        #         trademark = []
        #         tr_list = response.xpath('//*[@id="trademark"]/table/tbody/tr')
        #         for tr in tr_list:
        #             detail = drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[{0}]/td[@class="text-center nowrap"]/a'.format(i))
        #             drive.execute_script('arguments[0].click()', detail)
        #             time.sleep(2)
        #             trademark_detail['商标图片'] = drive.find_element_by_xpath('//img[@class="img-responsive img-center"]').get_attribute('src')
        #             trademark_detail['商标名称'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr/td[@class="td-2"]').get_attribute('textContent')
        #             trademark_detail['商标注册号'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[2]/td[2]').get_attribute('textContent')
        #             trademark_detail['商标类别'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[3]/td[2]').get_attribute('textContent')
        #             trademark_detail['商标状态'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[4]/td[2]').get_attribute('textContent')
        #             trademark_detail['申请人'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
        #             trademark_detail['申请日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
        #             trademark_detail['初审公告日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[4]').get_attribute('textContent')
        #             trademark_detail['注册公告日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[2]').get_attribute('textContent')
        #             trademark_detail['专用期限'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[4]').get_attribute('textContent')
        #             trademark_detail['专利代理机构'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[8]/td[2]').get_attribute('textContent')
        #             trademark_detail['商标公告'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[9]/td[2]').get_attribute('textContent')
        #             trademark_detail['商品服务项目'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[11]/td[1]').get_attribute('textContent')
        #             close = drive.find_element_by_xpath('//div[@class="modal-header modal-new-header"]/div[@class="close-div"]')
        #             drive.execute_script('arguments[0].click()', close)
        #             trademark.append({i: {'商标图片': trademark_detail['商标图片'], '商标名称': trademark_detail['商标名称'], '商标注册号': trademark_detail['商标注册号'], '商标类别': trademark_detail['商标类别'],'商标状态': trademark_detail['商标状态'], '申请人': trademark_detail['申请人'], '申请日': trademark_detail['申请日'], '初审公告日': trademark_detail['初审公告日'],'注册公告日': trademark_detail['注册公告日'], '专用期限': trademark_detail['专用期限'], '专利代理机构': trademark_detail['专利代理机构'],'商标公告': trademark_detail['商标公告'], '商品服务项目': trademark_detail['商品服务项目']}})
        #             i += 1
        #         print(trademark)
        #         items['商标'] = trademark
        #         yield items
        # else:
        #     trademark_detail = {}
        #     i = 1
        #     trademark = []
        #     tr_list = response.xpath('//*[@id="trademark"]/table/tbody/tr')
        #     for tr in tr_list:
        #         detail = drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[{0}]/td[@class="text-center nowrap"]/a'.format(i))
        #         drive.execute_script('arguments[0].click()', detail)
        #         time.sleep(2)
        #         trademark_detail['商标图片'] = drive.find_element_by_xpath('//img[@class="img-responsive img-center"]').get_attribute('src')
        #         trademark_detail['商标名称'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr/td[@class="td-2"]').get_attribute('textContent')
        #         trademark_detail['商标注册号'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[2]/td[2]').get_attribute('textContent')
        #         trademark_detail['商标类别'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[3]/td[2]').get_attribute('textContent')
        #         trademark_detail['商标状态'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[4]/td[2]').get_attribute('textContent')
        #         trademark_detail['申请人'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
        #         trademark_detail['申请日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
        #         trademark_detail['初审公告日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[4]').get_attribute('textContent')
        #         trademark_detail['注册公告日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[2]').get_attribute('textContent')
        #         trademark_detail['专用期限'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[4]').get_attribute('textContent')
        #         trademark_detail['专利代理机构'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[8]/td[2]').get_attribute('textContent')
        #         trademark_detail['商标公告'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[9]/td[2]').get_attribute('textContent')
        #         trademark_detail['商品服务项目'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[11]/td[1]').get_attribute('textContent')
        #         close = drive.find_element_by_xpath('//div[@class="modal-header modal-new-header"]/div[@class="close-div"]')
        #         drive.execute_script('arguments[0].click()', close)
        #         trademark.append({i: {'商标图片': trademark_detail['商标图片'], '商标名称': trademark_detail['商标名称'], '商标注册号': trademark_detail['商标注册号'], '商标类别': trademark_detail['商标类别'],'商标状态': trademark_detail['商标状态'], '申请人': trademark_detail['申请人'], '申请日': trademark_detail['申请日'], '初审公告日': trademark_detail['初审公告日'],'注册公告日': trademark_detail['注册公告日'], '专用期限': trademark_detail['专用期限'], '专利代理机构': trademark_detail['专利代理机构'],'商标公告': trademark_detail['商标公告'], '商品服务项目': trademark_detail['商品服务项目']}})
        #         i += 1
        #     print(trademark)
        #     items['商标'] = trademark
        #     yield items

        drive.close()