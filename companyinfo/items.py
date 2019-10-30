# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyinfoItem(scrapy.Item):


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

#########################################################################
    #融资信息
    融资信息 = scrapy.Field()
    融资时间 = scrapy.Field()
    融资轮次 = scrapy.Field()
    融资金额 = scrapy.Field()
    投资方 = scrapy.Field()

##########################################################################
    #质权人
    质权人 = scrapy.Field()
    登记日期 = scrapy.Field()
    状态 = scrapy.Field()
    出质人 = scrapy.Field()
    出质人详情 = scrapy.Field()
    出质股权数 = scrapy.Field()
    出质人证件号码 = scrapy.Field()
    登记编号 = scrapy.Field()
    标的方 = scrapy.Field()
    标的方详情 = scrapy.Field()
    质权人 = scrapy.Field()
    质权人详情 = scrapy.Field()
    质权人证件号码 = scrapy.Field()
    备注 = scrapy.Field()

###########################################################################
    #行政许可
    行政许可 = scrapy.Field()
    许可文件编号 = scrapy.Field()
    许可文件名称 = scrapy.Field()
    有效期自 = scrapy.Field()
    有效期至 = scrapy.Field()
    许可机关 = scrapy.Field()
    许可内容 = scrapy.Field()


































