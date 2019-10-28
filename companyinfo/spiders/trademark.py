# -*- coding: utf-8 -*-
import scrapy
import time
from selenium import webdriver
from companyinfo.items import CompanyinfoItem


class TrademarkSpider(scrapy.Spider):
    headers = {
        'Host': 'www.qixin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    }
    name = 'trademark'
    start_urls = {'https://www.qixin.com/ability/60214084-2b87-4ea3-9131-e4c313deacf0'}
    def parse(self, response):
        drive = webdriver.Chrome()
        drive.get("https://www.qixin.com/ability/60214084-2b87-4ea3-9131-e4c313deacf0")
        items = CompanyinfoItem()

        #商标
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
        #             strademark_detailml['商标注册号'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[2]/td[2]').get_attribute('textContent')
        #             trademark_detail['商标类别'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[3]/td[2]').get_attribute('textContent')
        #             trademark_detail['商标状态'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[4]/td[2]').get_attribute('textContent')
        #             trademark_detail['申请人'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
        #             smtrademark_detaill['申请日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
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
        #     drive.close()

        #专利信息
        # urls = response.xpath('//div[@class="container"]/div[@class="row"]/div[@class="col-md-18"]/div[@class="tab-content"]/table[@class="table table-bordered margin-t-1x"]/tbody/tr/td/h5[@class="h5"]/a/@href').extract()
        # i=0
        # for url in urls:
        #     url = str('https://www.qixin.com'+urls[i])
        #     i+=1
        #     str(url)
        #     print(url)
        #     yield scrapy.Request(url=url,callback=self.parse)
        # totalpage = int(drive.find_element_by_xpath('//*[@id="patent"]/h4/span').get_attribute('textContent')) // 5 + 1
        # print(totalpage)
        # if totalpage != 1:
        #     for p in range(1, totalpage):
        #         if p <= 3:
        #             p = p
        #         elif p == totalpage:
        #             p = 5
        #         else:
        #             p = 4
        #         page = drive.find_element_by_xpath('//*[@id="patent"]/div/div/nav/ul/li[{0}]/a'.format(p + 1))
        #         drive.execute_script('arguments[0].click()', page)
        #         time.sleep(2)
        #         patent_detail = {}
        #         i = 1
        #         patent = []
        #         tr_list = response.xpath('//*[@id="patent"]/table/tbody/tr')
        #         for tr in tr_list:
        #             time.sleep(2)
        #             patent_detail['专利名'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[5]/h5/a'.format(i)).get_attribute('textContent')
        #             patent_detail['专利类型'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[2]'.format(i)).get_attribute('textContent')
        #             patent_detail['申请公布号'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[3]'.format(i)).get_attribute('textContent')
        #             patent_detail['发布日期'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[4]'.format(i)).get_attribute('textContent')
        #             patent_detail['专利描述'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[5]/div'.format(i)).get_attribute('textContent')
        #             patent_detail['专利详情'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[5]/h5/a'.format(i)).get_attribute('href')
        #             patent.append({i: {'专利名': patent_detail['专利名'], '专利类型': patent_detail['专利类型'], '申请公布号': patent_detail['申请公布号'], '发布日期': patent_detail['发布日期'],'专利描述': patent_detail['专利描述'], '专利详情': patent_detail['专利详情']}})
        #             i += 1
        #         print(patent)
        #         items['专利'] = patent
        #         yield items
        # else:
        #     patent_detail = {}
        #     i = 1
        #     patent = []
        #     tr_list = response.xpath('//*[@id="patent"]/table/tbody/tr')
        #     for tr in tr_list:
        #         time.sleep(2)
        #         patent_detail['专利名'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[5]/h5/a'.format(i)).get_attribute('textContent')
        #         patent_detail['专利类型'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[2]'.format(i)).get_attribute('textContent')
        #         patent_detail['申请公布号'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[3]'.format(i)).get_attribute('textContent')
        #         patent_detail['发布日期'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[4]'.format(i)).get_attribute('textContent')
        #         patent_detail['专利描述'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[5]/div'.format(i)).get_attribute('textContent')
        #         patent_detail['专利详情'] = drive.find_element_by_xpath('//*[@id="patent"]/table/tbody/tr[{0}]/td[5]/h5/a'.format(i)).get_attribute('href')
        #         patent.append({i: {'专利名': patent_detail['专利名'], '专利类型': patent_detail['专利类型'], '申请公布号': patent_detail['申请公布号'], '发布日期': patent_detail['发布日期'],'专利描述': patent_detail['专利描述'], '专利详情': patent_detail['专利详情']}})
        #         i += 1
        #     print(patent)
        #     items['专利'] = patent
        #     yield items

        #著作权
        # totalpage = int(drive.find_element_by_xpath('//*[@id="copyRight"]/h4/span').get_attribute('textContent')) // 5 + 1
        # print(totalpage)
        # if totalpage != 1:
        #     for p in range(1, totalpage):
        #         if p <= 3:
        #             p = p
        #         elif p == totalpage:
        #             p = 5
        #         else:
        #             p = 4
        #         page = drive.find_element_by_xpath('//*[@id="copyRight"]/div/div/nav/ul/li[{0}]/a'.format(p + 1))
        #         drive.execute_script('arguments[0].click()', page)
        #         time.sleep(2)
        #         copyRight_detail = {}
        #         i = 1
        #         copyRight = []
        #         tr_list = response.xpath('//*[@id="copyRight"]/table/tbody/tr')
        #         for tr in tr_list:
        #             time.sleep(2)
        #             copyRight_detail['作品名称'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[2]'.format(i)).get_attribute('textContent')
        #             copyRight_detail['登记号'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[3]'.format(i)).get_attribute('textContent')
        #             copyRight_detail['类别'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[4]'.format(i)).get_attribute('textContent')
        #             copyRight_detail['创作完成日期'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[5]'.format(i)).get_attribute('textContent')
        #             copyRight_detail['登记日期'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[6]'.format(i)).get_attribute('textContent')
        #             copyRight_detail['首次发布日期'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[7]'.format(i)).get_attribute('textContent')
        #             copyRight.append({i: {'作品名称': copyRight_detail['作品名称'], '登记号': copyRight_detail['登记号'], '类别': copyRight_detail['类别'], '创作完成日期': copyRight_detail['创作完成日期'],'登记日期': copyRight_detail['登记日期'], '首次发布日期': copyRight_detail['首次发布日期']}})
        #             i += 1
        #         print(copyRight)
        #         items['著作权'] = copyRight
        #         yield items
        # else:
        #     copyRight_detail = {}
        #     i = 1
        #     copyRight = []
        #     tr_list = response.xpath('//*[@id="copyRight"]/table/tbody/tr')
        #     for tr in tr_list:
        #         time.sleep(2)
        #         copyRight_detail['作品名称'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[2]'.format(i)).get_attribute('textContent')
        #         copyRight_detail['登记号'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[3]'.format(i)).get_attribute('textContent')
        #         copyRight_detail['类别'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[4]'.format(i)).get_attribute('textContent')
        #         copyRight_detail['创作完成日期'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[5]'.format(i)).get_attribute('textContent')
        #         copyRight_detail['登记日期'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[6]'.format(i)).get_attribute('textContent')
        #         copyRight_detail['首次发布日期'] = drive.find_element_by_xpath('//*[@id="copyRight"]/table/tbody/tr[{0}]/td[7]'.format(i)).get_attribute('textContent')
        #         copyRight.append({i: {'作品名称': copyRight_detail['作品名称'], '登记号': copyRight_detail['登记号'], '类别': copyRight_detail['类别'], '创作完成日期': copyRight_detail['创作完成日期'],'登记日期': copyRight_detail['登记日期'], '首次发布日期': copyRight_detail['首次发布日期']}})
        #         i += 1
        #     print(copyRight)
        #     items['著作权'] = copyRight
        #     yield items


        #软件著作权


        #资质认证



        drive.close()




