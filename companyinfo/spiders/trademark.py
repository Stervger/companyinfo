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

        totalpage = int(drive.find_element_by_xpath('//*[@id="trademark"]/div[1]/h4/span').get_attribute('textContent'))//5 + 1
        print(totalpage)
        if totalpage!=1:
            for p in range(1,totalpage):
                if p <= 3:
                    p=p
                elif p==totalpage:
                    p=5
                else:
                    p=4
                page = drive.find_element_by_xpath('//*[@id="trademark"]/div[2]/div/nav/ul/li[{0}]/a'.format(p+1))
                drive.execute_script('arguments[0].click()', page)
                time.sleep(2)
                sml = {}
                i = 1
                a = []
                tr_list = response.xpath('//*[@id="trademark"]/table/tbody/tr')
                for tr in tr_list:
                    detail = drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[{0}]/td[@class="text-center nowrap"]/a'.format(i))
                    drive.execute_script('arguments[0].click()', detail)
                    time.sleep(2)
                    sml['商标图片'] = drive.find_element_by_xpath('//img[@class="img-responsive img-center"]').get_attribute('src')
                    sml['商标名称'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr/td[@class="td-2"]').get_attribute('textContent')
                    sml['商标注册号'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[2]/td[2]').get_attribute('textContent')
                    sml['商标类别'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[3]/td[2]').get_attribute('textContent')
                    sml['商标状态'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[4]/td[2]').get_attribute('textContent')
                    sml['申请人'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
                    sml['申请日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
                    sml['初审公告日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[4]').get_attribute('textContent')
                    sml['注册公告日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[2]').get_attribute('textContent')
                    sml['专用期限'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[4]').get_attribute('textContent')
                    sml['专利代理机构'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[8]/td[2]').get_attribute('textContent')
                    sml['商标公告'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[9]/td[2]').get_attribute('textContent')
                    sml['商品服务项目'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[11]/td[1]').get_attribute('textContent')
                    close = drive.find_element_by_xpath('//div[@class="modal-header modal-new-header"]/div[@class="close-div"]')
                    drive.execute_script('arguments[0].click()', close)
                    a.append({i: {'商标图片': sml['商标图片'], '商标名称': sml['商标名称'], '商标注册号': sml['商标注册号'], '商标类别': sml['商标类别'],'商标状态': sml['商标状态'], '申请人': sml['申请人'], '申请日': sml['申请日'], '初审公告日': sml['初审公告日'],'注册公告日': sml['注册公告日'], '专用期限': sml['专用期限'], '专利代理机构': sml['专利代理机构'],'商标公告': sml['商标公告'], '商品服务项目': sml['商品服务项目']}})
                    i += 1
                print(a)
                items['商标'] = a
                yield items
        else:
            sml = {}
            i = 1
            a = []
            tr_list = response.xpath('//*[@id="trademark"]/table/tbody/tr')
            for tr in tr_list:
                detail = drive.find_element_by_xpath('//table[@class="table table-bordered margin-t-1x text-middle"]/tbody/tr[{0}]/td[@class="text-center nowrap"]/a'.format(i))
                drive.execute_script('arguments[0].click()', detail)
                time.sleep(2)
                sml['商标图片'] = drive.find_element_by_xpath('//img[@class="img-responsive img-center"]').get_attribute('src')
                sml['商标名称'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr/td[@class="td-2"]').get_attribute('textContent')
                sml['商标注册号'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[2]/td[2]').get_attribute('textContent')
                sml['商标类别'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[3]/td[2]').get_attribute('textContent')
                sml['商标状态'] = drive.find_element_by_xpath('//div[@class="modal-content"]/div[@class="modal-body padding-t-0x"]/div[@class="row"]/div[@class="col-xs-24"]/table[@class="table table1 table-bordered"]/tbody/tr[4]/td[2]').get_attribute('textContent')
                sml['申请人'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]').get_attribute('textContent')
                sml['申请日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[2]').get_attribute('textContent')
                sml['初审公告日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[6]/td[4]').get_attribute('textContent')
                sml['注册公告日'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[2]').get_attribute('textContent')
                sml['专用期限'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[7]/td[4]').get_attribute('textContent')
                sml['专利代理机构'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[8]/td[2]').get_attribute('textContent')
                sml['商标公告'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[9]/td[2]').get_attribute('textContent')
                sml['商品服务项目'] = drive.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div/div/table/tbody/tr[11]/td[1]').get_attribute('textContent')
                close = drive.find_element_by_xpath('//div[@class="modal-header modal-new-header"]/div[@class="close-div"]')
                drive.execute_script('arguments[0].click()', close)
                a.append({i: {'商标图片': sml['商标图片'], '商标名称': sml['商标名称'], '商标注册号': sml['商标注册号'], '商标类别': sml['商标类别'],'商标状态': sml['商标状态'], '申请人': sml['申请人'], '申请日': sml['申请日'], '初审公告日': sml['初审公告日'],'注册公告日': sml['注册公告日'], '专用期限': sml['专用期限'], '专利代理机构': sml['专利代理机构'], '商标公告': sml['商标公告'],'商品服务项目': sml['商品服务项目']}})
                i += 1
            print(a)
            items['商标'] = a
            yield items

        #专利信息
        # urls = response.xpath('//div[@class="container"]/div[@class="row"]/div[@class="col-md-18"]/div[@class="tab-content"]/table[@class="table table-bordered margin-t-1x"]/tbody/tr/td/h5[@class="h5"]/a/@href').extract()
        # # print(urls)
        # i=0
        # url = list('https://www.qixin.com'+urls[i].format(x) for x in range(6))
        # print(url)
        # i+=1
        # yield scrapy.Request(url=url,callback=self.parse)


        #著作权


        #软件著作权


        #资质认证


            drive.close()
