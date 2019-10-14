# -*- coding: utf-8 -*-
import urllib

import scrapy


class QixinbaoSpider(scrapy.Spider):
    cookie = 'acw_tc=2f624a5615707693004962356e0a1789d82b20f65cc8c5f95024decfe87d6d; channel=%2Bbaidusem8; cookieShowLoginTip=2; Hm_lvt_52d64b8d3f6d42a2e416d59635df3f71=1571016421,1571018903,1571024473,1571024511; sid=s%3Acgp9FWrNHbl5fbKxMln3R9ClU35_5er6.UrmFCeFoVhRo6QboVL1PPPNQSl14YTIH5d%2B4edGBYzE; Hm_lpvt_52d64b8d3f6d42a2e416d59635df3f71=1571036295'
    headers = {
        'Host': 'www.qixin.com',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
        'Cookie': cookie
    }

    name = 'qixinbao'
    allowed_domains = ['https://www.qixin.com']
    start_urls = ['https://www.qixin.com/search?from=baidusem17&key=']

    def start_requests(self):
        # 查询公司
        f = open('E://python_work/companyinfo/companyinfo/company_list.txt', 'r', encoding='utf-8')
        for link in f:
            company = urllib.parse.quote(link).replace('\n', '')
            url = self.start_urls[0] + company
            url = url.replace('%0A','&page=1')
            print(url)
            yield scrapy.Request(url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        # 提取列表中第一个公司，进入该页
        link = response.xpath('/html/body/div[2]/div[3]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/a/@href').extract_first()
        detail_link = response.urljoin(link)
        print(detail_link)
        yield scrapy.Request(detail_link, headers=self.headers, callback=self.page_parse)
