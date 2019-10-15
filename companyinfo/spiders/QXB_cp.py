import  scrapy
from companyinfo.items import CompanyinfoItem
from urllib.parse import urlencode
import urllib
import re
from DJ import unlock

class sinaCJSpider(scrapy.Spider):
    name = 'QXB'
    def start_requests(self):
        f = open('./company_list.txt','r',encoding='utf-8')
        urls = ['https://www.qixin.com/search?key={0}&page=1'.format(urllib.parse.quote(f_out[:-1])) for f_out in f]
        # for f_out in f:
        #     # for url in self.start_urls:
        #     company = urllib.parse.quote(f_out)
        #     url = urls[0] + company[:-1]
        #unlock(urls)
        for url in urls[:10]:
            yield scrapy.Request(url=url,callback=self.parse)
    def parse(self, response):
        # time.sleep(random.uniform(0.5,5))
        # if '点击按钮进行验证' in response.text:
        try:

            # b = response.xpath('/html/body/div[6]/div[2]/div[6]/div/div/div[2]/div[1]/div/div[2]/img')
            # if b:
            unlock(response.url)
            # else:
            #     HuaDong(driver)
            return scrapy.Request(url=response.url,callback=self.parse)
        except:
            print('没有验证码')

            urls = re.findall(r'keyId="(.*?)"',response.text,re.M)
            st_url = 'www.qixin.com/company/'
            for url in urls:
                fu_url = {st_url+url}
                yield scrapy.Request(url=fu_url,callback=self.company)
    def company(self,response):
        item = CompanyinfoItem()
        tr_list = response.xpath('//*[@id="icinfo"]/table')
        item['uni_cre_code']=tr_list.xpath('./tbody/tr[1]/td[2]/text()').extract()
        item['org_code']=tr_list.xpath('./tbody/tr[1]/td[4]/text()').extract()
        item['reg_no']=tr_list.xpath('./tbody/tr[2]/td[2]/text()').extract()
        item['ope_status']=tr_list.xpath('./tbody/tr[2]/td[4]/text()').extract()
        item['source_type']=tr_list.xpath('./tbody/tr[3]/td[2]/text()').extract()
        item['est_date']=tr_list.xpath('./tbody/tr[3]/td[4]/text()').extract()#============================================
        item['firm_type']=tr_list.xpath('./tbody/tr[4]/td[2]/text()').extract()
        item['open_date']=tr_list.xpath('./tbody/tr[4]/td[4]/text()').extract()[:11]
        item['close_date']=tr_list.xpath('./tbody/tr[4]/td[4]/text()').extract()[-10:]
        item['legal_rep']=tr_list.xpath('./tbody/tr[5]/td[2]/a/text()').extract()
        item['release_date']=tr_list.xpath('./tbody/tr[5]/td[4]/text()').extract()
        item['reg_cap']=tr_list.xpath('./tbody/tr[6]/td[2]/text()').extract()
        item['reg_institution']=tr_list.xpath('./tbody/tr[6]/td[4]/text()').extract()#===============
        item['con_addr']=tr_list.xpath('./tbody/tr[7]/td[2]/text()').extract()
        item['ope_scope']=tr_list.xpath('./tbody/tr[8]/td[2]/text()').extract()
        yield item

