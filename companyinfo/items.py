# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyinfoItem(scrapy.Item):
    #基本信息
    dc_id = scrapy.Field()  # 主键
    data_version_id = scrapy.Field()  # 版本
    licence_pro = scrapy.Field()  # 许可经营项目
    ind_econ_code = scrapy.Field()  # 国民经济行业代码
    ind_econ_name = scrapy.Field()  # 国民经济代码名称
    source_type = scrapy.Field()  # 类型（0:il_annualreport、1:annualreport)
    oreg_no = scrapy.Field()  # 原注册号
    reg_no = scrapy.Field()  # 企业注册号
    firm_name = scrapy.Field()  # 企业名称简称
    firm_name_en = scrapy.Field()  # 企业英文名称
    firm_name_sh = scrapy.Field()  # 企业名称简称
    firm_name_used = scrapy.Field()  # 企业曾用名
    firm_type_code = scrapy.Field()  # 企业类型编码
    firm_type = scrapy.Field()  # 企业类型
    org_code = scrapy.Field()  # 组织机构代码
    uni_cre_code = scrapy.Field()  # 统一信用代码
    postalcode = scrapy.Field()  # 企业邮政编码
    legal_rep = scrapy.Field()  # 法定代表人
    reg_institution = scrapy.Field()  # 登记机关
    est_date = scrapy.Field()  # 成立日期
    cancel_date = scrapy.Field()  # 注销日期
    appr_date = scrapy.Field()  # 核准日期
    rev_date = scrapy.Field()  # 吊销日期
    open_date = scrapy.Field()  # 营业开始日期
    close_date = scrapy.Field()  # 营业结束日期
    province = scrapy.Field()  # 省份
    city = scrapy.Field()  # 城市
    district = scrapy.Field()  # 区/县
    final_check_year = scrapy.Field()  # 最后年检年度
    con_email = scrapy.Field()  # 联系邮箱
    con_addr = scrapy.Field()  # 地址
    con_tel = scrapy.Field()  # 联系电话
    addr_district = scrapy.Field()  # 住所所在行政区
    reg_addr_code = scrapy.Field()  # 注册地址行政编号
    reg_cap = scrapy.Field()  # 注册资本
    reg_cap_cur = scrapy.Field()  # 注册资本币种
    rec_cap = scrapy.Field()  # 实收资本(万元)
    ope_status = scrapy.Field()  # 经营状态
    ope_scope = scrapy.Field()  # 经营业务范围
    emp_num = scrapy.Field()  # 员工人数
    ann_report_id = scrapy.Field()  # 年报ID
    ann_report_date = scrapy.Field()  # 年报日期
    ann_report_year = scrapy.Field()  # 年报年份
    release_date = scrapy.Field()  # 发布日期
    ins_num_pen = scrapy.Field()  # 城镇职工基本养老保险参保人数
    ins_num_unemp = scrapy.Field()  # 失业保险参保人数
    ins_num_med = scrapy.Field()  # 职工基本医疗保险参保人数
    ins_num_injury = scrapy.Field()  # 工伤保险参保人数
    ins_num_rear = scrapy.Field()  # 生育保险参保人数
    ins_real_pay_pen = scrapy.Field()  # 参加城镇职工基本养老保险本期实际缴费金额
    ins_real_pay_unemp = scrapy.Field()  # 参加失业保险本期实际缴费金额
    ins_real_pay_med = scrapy.Field()  # 参加职工基本医疗保险本期实际缴费金额
    ins_real_pay_injury = scrapy.Field()  # 参加工伤保险本期实际缴费金额
    ins_real_pay_rear = scrapy.Field()  # 参加生育保险本期实际缴费金额
    ins_base_pen = scrapy.Field()  # 单位参加城镇职工基本养老保险缴费基数
    ins_base_unemp = scrapy.Field()  # 单位参加失业保险缴费基数
    ins_base_med = scrapy.Field()  # 单位参加职工基本医疗保险缴费基数
    ins_base_injury = scrapy.Field()  # 单位参加工伤保险缴费基数
    ins_base_rear = scrapy.Field()  # 单位参加生育保险缴费基数
    ins_unpaid_city = scrapy.Field()  # 单位参加城镇职工基本养老保险累计欠缴金额
    ins_unpaid_unemp = scrapy.Field()  # 单位参加失业保险累计欠缴金额
    ins_unpaid_med = scrapy.Field()  # 单位参加职工基本医疗保险累计欠缴金额
    ins_unpaid_injury = scrapy.Field()  # 参加工伤保险累计欠缴金额
    ins_unpaid_rear = scrapy.Field()  # 单位参加生育保险累计欠缴金额
    whether_website = scrapy.Field()  # 是否有网站或网店
    web_addr = scrapy.Field()  # 网站地址
    web_name = scrapy.Field()  # 网站名称
    web_type = scrapy.Field()  # 网站类型
    web_source = scrapy.Field()  # 网址来源
    domain_addr = scrapy.Field()  # 域名网址
    domain_name = scrapy.Field()  # 域名名称
    domain_permit_num = scrapy.Field()  # 域名许可证号
    domain_date = scrapy.Field()  # 域名登记批准日期
    liquidation_debt_receiver = scrapy.Field()  # 清算债务承接人
    liquidation_credit_receiver = scrapy.Field()  # 清算债权承接人
    liquidation_principal = scrapy.Field()  # 清算负责人
    liquidation_member = scrapy.Field()  # 清算组成员
    liquidation_start_date = scrapy.Field()  # 清算开始日期
    liquidation_end_date = scrapy.Field()  # 清算完结日期
    liquidation_period = scrapy.Field()  # 清算时长
    liquidation_end_details = scrapy.Field()  # 清算完结情况
    liquidation_type = scrapy.Field()  # 清算类型
    liquidation_prop_amt = scrapy.Field()  # 清算财产数额
    liquidation_valu_method = scrapy.Field()  # 清算财产计价方法
    liquidation_cost = scrapy.Field()  # 清算费用
    datachange_lasttime = scrapy.Field()  # 获取时间

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