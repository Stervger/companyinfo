# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyinfoItem(scrapy.Item):
    #基本信息


##########################################################################
    #商标（trademark）
    商标 = scrapy.Field()
    商标图片 = scrapy.Field()# 商标图片链接
    商标名称 = scrapy.Field()  # 商标名称
    商标状态 = scrapy.Field()  # 商标状态
    申请日 = scrapy.Field()  # 商标申请时间
    商标注册号 = scrapy.Field()  # 商标注册号
    商标类别 = scrapy.Field()  # 商标类别
    申请人 = scrapy.Field()  # 商标申请人
    初审公告日 = scrapy.Field()  # 商标初审公告日期
    注册公告日 = scrapy.Field()  # 商标注册公告日
    专用期限 = scrapy.Field()  # 商标专用期限
    专利代理机构 = scrapy.Field()  # 商标代理机构信息
    商品服务项目 = scrapy.Field()  # 商标产品服务列表名

############################################################################
    #专利（patent）
    专利 = scrapy.Field()
    专利名 = scrapy.Field()
    专利类型 = scrapy.Field()
    申请公布号 = scrapy.Field()
    发布日期 = scrapy.Field()
    专利描述 = scrapy.Field()
    专利详情 = scrapy.Field()

#############################################################################
    #著作权（copyright）
    著作权 = scrapy.Field()
    作品名称 = scrapy.Field()
    登记号 = scrapy.Field()
    类别 = scrapy.Field()
    创作完成日期 = scrapy.Field()
    登记日期 = scrapy.Field()
    首次发布日期 = scrapy.Field()

###########################################################################
    #软件著作权
    软件著作权 = scrapy.Field()
    软件名称 = scrapy.Field()
    登记号 = scrapy.Field()
    版本号 = scrapy.Field()
    分类号 = scrapy.Field()
    登记批准日期 = scrapy.Field()
    软件简称 = scrapy.Field()

##########################################################################
    #资质认证
    资质认证 = scrapy.Field()
    发证日期 = scrapy.Field()
    证书类别 = scrapy.Field()
    截止日期 = scrapy.Field()
    证书编号 = scrapy.Field()
    状态 = scrapy.Field()
    备注 = scrapy.Field()





































