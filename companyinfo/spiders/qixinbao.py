# -*- coding: utf-8 -*-
import urllib
from companyinfo.items import CompanyinfoItem
import scrapy


class QixinbaoSpider(scrapy.Spider):
    cookie = 'acw_tc=707c9fdb15710509288834359e54c6057047891e03cbb554e69db2c9fd791d; channel=%2Bbaidusem17; Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71=1571050927; Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71=1571052800; sid=s%3A5zX7X9rzI7wcIjvPmB3BaGfxNml6PFRc.tL%2B%2BQ1GOQOQFrZqwZnQom7Z9928lxFadVD9zHy2VdQU'
    headers = {
        'Host': 'www.qixin.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Cookie': cookie
    }

    name = 'qixinbao'
    allowed_domains = ['https://www.qixin.com']
    start_urls = ['https://www.qixin.com/search?from=baidusem17&key=']

    def start_requests(self):
        # 查询公司
        f = open('./company_list.txt', 'r', encoding='utf-8')
        for link in f:
            company = urllib.parse.quote(link).replace('\n', '')
            url = self.start_urls[0] + company
            url = url.replace('%0A','&page=1')
            print(url)
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        # 提取列表中第一个公司，进入该页
        link = response.css('.company-title a::attr(href)').extract()
        detail_link = response.urljoin(link)
        print(detail_link)
        yield scrapy.Request(detail_link, headers=self.headers, callback=self.detail)

    def detail(self, response):
        items = CompanyinfoItem()

        licence_pro = response.xpath('/html/body/div[5]/div/div[1]/div[1]/table/tbody/tr[3]/td[2]//text()').extract()[0]
        items['licence_pro'] = licence_pro.strip().replace('\n', '')

        yield items

































