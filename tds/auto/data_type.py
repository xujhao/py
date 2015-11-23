# encoding: UTF-8
# auto generate by generate_fixDict.py

from ctypes import *

fixDict = {}

fixDict["ORDER_ID"] = c_char_p("11")#合同序号
fixDict["REPAY_ORDER_ID"] = c_char_p("11")#偿还合同序号
fixDict["CURRENCY"] = c_char_p("15")#货币代码
fixDict["MATCHED_SN"] = c_char_p("17")#成交编号
fixDict["STKBD_LINK"] = c_char_p("17")#关联板块
fixDict["OFFER_QTY"] = c_char_p("37")#申报数量
fixDict["ORDER_QTY"] = c_char_p("38")#委托数量
fixDict["ORDER_STATUS"] = c_char_p("39")#委托状态
fixDict["STK_BIZ_ACTION"] = c_char_p("40")#业务行为
fixDict["STK_BIZ_ACTION"] = c_char_p("40")#证券业务行为
fixDict["STK_BIZ_ACTION"] = c_char_p("40")#业务活动
fixDict["TRD_BIZ_ACCTION"] = c_char_p("40")#业务活动
fixDict["RAW_ORDER_ID"] = c_char_p("41")#原合同序号
fixDict["ORDER_PRICE"] = c_char_p("44")#委托价格
fixDict["STK_CODE"] = c_char_p("48")#证券代码
fixDict["TRD_CODE"] = c_char_p("48")#品种代码
fixDict["STK_NAME"] = c_char_p("55")#证券名称
fixDict["ORDER_TEXT"] = c_char_p("58")#委托扩展
fixDict["ORDER_BSN"] = c_char_p("66")#委托批号
fixDict["STKEX"] = c_char_p("207")#交易市场
fixDict["EXCHANGE"] = c_char_p("207")#交易所
fixDict["MATCHED_QTY"] = c_char_p("387")#已成交数量
fixDict["STK_TRDACCT"] = c_char_p("448")#证券账户
fixDict["TRDACCT"] = c_char_p("448")#交易账户
fixDict["TRDACCT"] = c_char_p("448")#证券账户
fixDict["STK_CLS"] = c_char_p("461")#证券类别
fixDict["STKBD"] = c_char_p("625")#交易板块
fixDict["BGN_EXE_TIME"] = c_char_p("916")#执行开始时间
fixDict["END_EXE_TIME"] = c_char_p("917")#执行结束时间
fixDict["OFFER_STIME"] = c_char_p("8500")#申报时间
fixDict["STK_PREBLN"] = c_char_p("8501")#证券昨日余额
fixDict["MATCHED_AMT"] = c_char_p("8504")#成交金额
fixDict["MATCHED_AMT"] = c_char_p("8504")#已成交金额
fixDict["REPAY_CONTRACT_AMT"] = c_char_p("8504")#偿还金额
fixDict["CONTINGENT_CONDITION"] = c_char_p("8713")#触发条件
fixDict["FORCE_CLOSE_REASON"] = c_char_p("8715")#强平原因
fixDict["BUSINESS_UNIT"] = c_char_p("8717")#业务单元
fixDict["IS_SWAP_ORDER"] = c_char_p("8720")#互换单标志
fixDict["GTD_DATA"] = c_char_p("8723")#GTD日期
fixDict["F_OP_USER"] = c_char_p("8810")#操作用户代码
fixDict["F_OP_ROLE"] = c_char_p("8811")#操作用户角色
fixDict["F_OP_SITE"] = c_char_p("8812")#操作站点
fixDict["OP_SITE"] = c_char_p("8812")#操作站点
fixDict["F_CHANNEL"] = c_char_p("8813")#操作渠道
fixDict["CHANNEL"] = c_char_p("8813")#操作渠道
fixDict["F_SESSION"] = c_char_p("8814")#会话凭证
fixDict["SESSION_ID"] = c_char_p("8814")#会话凭证
fixDict["F_FUNCTION"] = c_char_p("8815")#功能代码
fixDict["F_RUNTIME"] = c_char_p("8816")#调用时间
fixDict["MSG_CODE"] = c_char_p("8817")#信息代码
fixDict["MSG_LEVEL"] = c_char_p("8818")#信息级别
fixDict["MSG_TEXT"] = c_char_p("8819")#信息正文
fixDict["MSG_DEBUG"] = c_char_p("8820")#调试信息
fixDict["F_OP_ORG"] = c_char_p("8821")#操作机构
fixDict["ORDER_AMT"] = c_char_p("8830")#委托金额
fixDict["ORDER_FRZ_AMT"] = c_char_p("8831")#委托冻结金额
fixDict["ORDER_FRZ_AMT"] = c_char_p("8831")#冻结金额
fixDict["ORDER_SN"] = c_char_p("8832")#委托序号
fixDict["ORDER_VALID_FLAG"] = c_char_p("8833")#委托有效标志
fixDict["ORDER_DATE"] = c_char_p("8834")#委托日期
fixDict["ORDER_UFZ_AMT"] = c_char_p("8835")#委托解冻金额
fixDict["IS_WITHDRAW"] = c_char_p("8836")#撤单标志
fixDict["WITHDRAWN_QTY"] = c_char_p("8837")#已撤单数量
fixDict["IS_WITHDRAWN"] = c_char_p("8838")#已撤单标志
fixDict["MATCHED_TIME"] = c_char_p("8840")#成交时间
fixDict["MATCHED_PRICE"] = c_char_p("8841")#成交价格
fixDict["STK_BIZ"] = c_char_p("8842")#证券业务
fixDict["STK_BIZ"] = c_char_p("8842")#交易业务
fixDict["TRD_BIZ"] = c_char_p("8842")#交易业务
fixDict["STKPBU"] = c_char_p("8843")#交易单元
fixDict["TRD_DATE"] = c_char_p("8844")#交易日期
fixDict["ORDER_TIME"] = c_char_p("8845")#委托时间
fixDict["VALID_DATE"] = c_char_p("8859")#截止日期
fixDict["FUND_PREBLN"] = c_char_p("8860")#资金昨日余额
fixDict["FUND_AVL"] = c_char_p("8861")#资金可用金额
fixDict["FUND_FRZ"] = c_char_p("8862")#资金冻结金额
fixDict["FUND_UFZ"] = c_char_p("8863")#资金解冻金额
fixDict["FUND_TRD_FRZ"] = c_char_p("8864")#资金交易冻结金额
fixDict["FUND_TRD_UFZ"] = c_char_p("8865")#资金交易解冻金额
fixDict["FUND_TRD_OTD"] = c_char_p("8866")#资金交易在途金额
fixDict["FUND_TRD_BLN"] = c_char_p("8867")#资金交易轧差金额
fixDict["FUND_STATUS"] = c_char_p("8868")#资金状态
fixDict["STK_AVL"] = c_char_p("8869")#证券可用数量
fixDict["STK_FRZ"] = c_char_p("8870")#证券冻结数量
fixDict["STK_UFZ"] = c_char_p("8871")#证券解冻数量
fixDict["STK_TRD_FRZ"] = c_char_p("8872")#证券交易冻结数量
fixDict["STK_TRD_UFZ"] = c_char_p("8873")#证券交易解冻数量
fixDict["STK_TRD_OTD"] = c_char_p("8874")#证券交易在途数量
fixDict["STK_BCOST"] = c_char_p("8875")#证券买入成本
fixDict["STK_BCOST_RLT"] = c_char_p("8876")#证券买入成本（实时）
fixDict["STK_PLAMT"] = c_char_p("8877")#证券盈亏金额
fixDict["STK_PLAMT_RLT"] = c_char_p("8878")#证券盈亏金额（实时）
fixDict["MKT_VAL"] = c_char_p("8879")#市值
fixDict["CUST_CODE"] = c_char_p("8902")#客户代码
fixDict["INT_ORG"] = c_char_p("8911")#内部机构
fixDict["COMPONET_STK_CODE"] = c_char_p("8911")#成份股代码
fixDict["CLI_REMARK"] = c_char_p("8914")#备用信息
fixDict["CUACCT_CODE"] = c_char_p("8920")#资产账户
fixDict["CUACCT_ATTR"] = c_char_p("8921")#资产账户属性
fixDict["TRDACCT_SN"] = c_char_p("8928")#账户序号
fixDict["CUACCT_SN"] = c_char_p("8928")#账户序号
fixDict["TRDACCT_EXID"] = c_char_p("8929")#报盘账户
fixDict["TRDACCT_NAME"] = c_char_p("8932")#交易账户名称
fixDict["TRDACCT_STATUS"] = c_char_p("8933")#账户状态
fixDict["TREG_STATUS"] = c_char_p("8934")#指定状态
fixDict["BREG_STATUS"] = c_char_p("8935")#回购状态
fixDict["BOND_INT"] = c_char_p("8960")#债券利息
fixDict["COMPONET_STKBD"] = c_char_p("8962")#成份股板块
fixDict["TRD_CODE_CLS"] = c_char_p("8970")#品种类型
fixDict["SPREAD_NAME"] = c_char_p("8971")#组合名称
fixDict["UNDL_CODE"] = c_char_p("8972")#标的代码
fixDict["EXERCISE_PRICE"] = c_char_p("8973")#行权价
fixDict["CON_UNIT"] = c_char_p("8974")#合约单位
fixDict["STOP_PRICE"] = c_char_p("8975")#触发价格
fixDict["CON_EXP_DATE"] = c_char_p("8976")#合约到期日
fixDict["FUND_BLN"] = c_char_p("8984")#资金余额
fixDict["STK_BLN"] = c_char_p("8985")#证券余额
fixDict["ACCT_TYPE"] = c_char_p("8987")#账户类型
fixDict["QUERY_POS"] = c_char_p("8991")#定位串
fixDict["QRY_POS"] = c_char_p("8991")#定位串
fixDict["QRY_POS"] = c_char_p("8991")#定位串查询
fixDict["QUERY_NUM"] = c_char_p("8992")#查询行数
fixDict["CLIENT_INFO"] = c_char_p("9039")#终端信息
fixDict["VALUE_FLAG"] = c_char_p("9080")#取值标志
fixDict["QUERY_FLAG"] = c_char_p("9080")#查询方向
fixDict["OFFER_RET_MSG"] = c_char_p("9080")#申报信息
fixDict["MATCHED_TYPE"] = c_char_p("9080")#成交类型
fixDict["SECURITY_LEVEL"] = c_char_p("9080")#安全手段
fixDict["CANCEL_STATUS"] = c_char_p("9080")#内部撤单标志
fixDict["ACCT_ID"] = c_char_p("9081")#账户标识
fixDict["MARKET_VALUE"] = c_char_p("9081")#资产总值
fixDict["FLAG"] = c_char_p("9081")#查询标志
fixDict["SECURITY_INFO"] = c_char_p("9081")#安全信息
fixDict["MSG_OK"] = c_char_p("9081")#内撤信息
fixDict["USE_SCOPE"] = c_char_p("9082")#使用范围
fixDict["CHANNEL_ID"] = c_char_p("9082")#通道号
fixDict["FUND_VALUE"] = c_char_p("9082")#资金资产
fixDict["CANCEL_LIST"] = c_char_p("9082")#撤单列表
fixDict["OPT_NUM"] = c_char_p("9082")#合约编码
fixDict["AUTH_TYPE"] = c_char_p("9083")#认证类型
fixDict["STK_VALUE"] = c_char_p("9083")#市值
fixDict["PUBLISH_CTRL_FLAG"] = c_char_p("9083")#股票风控标志
fixDict["AUTH_DATA"] = c_char_p("9084")#认证数据
fixDict["FUND_LOAN"] = c_char_p("9084")#融资总金额
fixDict["ENCRYPT_KEY"] = c_char_p("9086")#加密因子
fixDict["COST_PRICE"] = c_char_p("9090")#成本价格
fixDict["PRO_INCOME"] = c_char_p("9091")#参考盈亏
fixDict["STK_CAL_MKTVAL"] = c_char_p("9092")#市值计算标识
fixDict["STK_QTY"] = c_char_p("9093")#当前拥股数
fixDict["ORDER_ID_EX"] = c_char_p("9093")#外部合同序号
fixDict["CURRENT_PRICE"] = c_char_p("9094")#最新价格
fixDict["PROFIT_PRICE"] = c_char_p("9095")#参考成本价
fixDict["STK_DIFF"] = c_char_p("9096")#可申赎数量
fixDict["STK_TRD_UNFRZ"] = c_char_p("9097")#已申赎数量
fixDict["INCOME"] = c_char_p("9098")#盈亏
fixDict["ORDER_ATTR"] = c_char_p("9100")#高级属性
fixDict["ATTR_CODE"] = c_char_p("9101")#属性代码
fixDict["CLI_ORDER_NO"] = c_char_p("9102")#客户端委托编号
fixDict["EXE_STATUS"] = c_char_p("9103")#执行状态
fixDict["EXE_INFO"] = c_char_p("9104")#执行信息
fixDict["ORDER_NO"] = c_char_p("9106")#委托编号
fixDict["REPAY_OPENING_DATE"] = c_char_p("9121")#偿还合约日期
fixDict["REPAY_STK_CODE"] = c_char_p("9218")#偿还证券代码
fixDict["STK_REMAIN"] = c_char_p("9398")#余券可用数量


replyMsgParam = {}
#用户登录(API)
replyMsgParam["10301105"] = {'ACCT_ID': 's,32',
                             'ACCT_TYPE': 's,2',
                             'BREG_STATUS': 'c',
                             'CHANNEL_ID': 's,2',
                             'CUACCT_CODE': 'l',
                             'CUST_CODE': 'l',
                             'INT_ORG': 'n',
                             'SESSION_ID': 's,128',
                             'STKBD': 'None',
                             'STKEX': 'c',
                             'STKPBU': 's,8',
                             'STK_TRDACCT': 's,10',
                             'TRDACCT_EXID': 's,10',
                             'TRDACCT_NAME': 's,32',
                             'TRDACCT_SN': 'n',
                             'TRDACCT_STATUS': 'c',
                             'TREG_STATUS': 'c',
                             }
#买卖委托
replyMsgParam["10302001"] = {'CUACCT_CODE': 'l',
                             'CUACCT_SN': 'n',
                             'ORDER_AMT': 'd',
                             'ORDER_BSN': 'n',
                             'ORDER_FRZ_AMT': 'd',
                             'ORDER_ID': 's,10',
                             'ORDER_PRICE': 'd',
                             'ORDER_QTY': 'l',
                             'STKBD': 'None',
                             'STKPBU': 's,8',
                             'STK_BIZ': 'n',
                             'STK_BIZ_ACTION': 'n',
                             'STK_CODE': 's,8',
                             'STK_NAME': 's,16',
                             'TRDACCT': 's,10',
                             }
#委托撤单
replyMsgParam["10302004"] = {'CANCEL_LIST': 's,256',
                             'CANCEL_STATUS': 'c',
                             'CUACCT_CODE': 'l',
                             'MSG_OK': 'None',
                             'ORDER_AMT': 'd',
                             'ORDER_BSN': 'n',
                             'ORDER_FRZ_AMT': 'd',
                             'ORDER_ID': 's,10',
                             'ORDER_PRICE': 'd',
                             'ORDER_QTY': 'l',
                             'STKBD': 'None',
                             'STKPBU': 's,8',
                             'STK_BIZ': 'n',
                             'STK_BIZ_ACTION': 'n',
                             'STK_CODE': 's,8',
                             'STK_NAME': 's,16',
                             'TRDACCT': 's,10',
                             }
#可用资金查询
replyMsgParam["10303001"] = {'CUACCT_ATTR': 'c',
                             'CUACCT_CODE': 'l',
                             'CURRENCY': 'c',
                             'CUST_CODE': 'l',
                             'FUND_AVL': 'd',
                             'FUND_BLN': 'd',
                             'FUND_FRZ': 'd',
                             'FUND_LOAN': 'd',
                             'FUND_PREBLN': 'd',
                             'FUND_STATUS': 'c',
                             'FUND_TRD_BLN': 'd',
                             'FUND_TRD_FRZ': 'd',
                             'FUND_TRD_OTD': 'd',
                             'FUND_TRD_UFZ': 'd',
                             'FUND_UFZ': 'd',
                             'FUND_VALUE': 'd',
                             'INT_ORG': 'n',
                             'MARKET_VALUE': 'd',
                             'STK_VALUE': 'd',
                             }
#可用股份查询
replyMsgParam["10303002"] = {'COST_PRICE': 'd',
                             'CUACCT_CODE': 'l',
                             'CURRENCY': 'c',
                             'CURRENT_PRICE': 'd',
                             'CUST_CODE': 'l',
                             'INCOME': 'd',
                             'INT_ORG': 'n',
                             'MKT_VAL': 'd',
                             'PROFIT_PRICE': 'd',
                             'PRO_INCOME': 'd',
                             'QRY_POS': 's,32',
                             'STKBD': 'None',
                             'STKPBU': 's,8',
                             'STK_AVL': 'l',
                             'STK_BCOST': 'd',
                             'STK_BCOST_RLT': 'd',
                             'STK_BLN': 'l',
                             'STK_CAL_MKTVAL': 'c',
                             'STK_CLS': 'c',
                             'STK_CODE': 's,8',
                             'STK_DIFF': 'l',
                             'STK_FRZ': 'l',
                             'STK_NAME': 's,16',
                             'STK_PLAMT': 'd',
                             'STK_PLAMT_RLT': 'd',
                             'STK_PREBLN': 'l',
                             'STK_QTY': 'l',
                             'STK_REMAIN': 'l',
                             'STK_TRD_FRZ': 'l',
                             'STK_TRD_OTD': 'l',
                             'STK_TRD_UFZ': 'l',
                             'STK_TRD_UNFRZ': 'l',
                             'STK_UFZ': 'l',
                             'TRDACCT': 's,10',
                             }
#当日委托查询
replyMsgParam["10303003"] = {'BOND_INT': 'None',
                             'CHANNEL': 'None',
                             'CUACCT_CODE': 'l',
                             'CUACCT_SN': 'n',
                             'CURRENCY': 'c',
                             'CUST_CODE': 'l',
                             'INT_ORG': 'n',
                             'IS_WITHDRAW': 'c',
                             'IS_WITHDRAWN': 'c',
                             'MATCHED_AMT': 'd',
                             'MATCHED_QTY': 'l',
                             'OFFER_QTY': 'l',
                             'OFFER_RET_MSG': 's,64',
                             'OFFER_STIME': 'n',
                             'OP_SITE': 's,32',
                             'ORDER_AMT': 'd',
                             'ORDER_BSN': 'n',
                             'ORDER_DATE': 'n',
                             'ORDER_FRZ_AMT': 'd',
                             'ORDER_ID': 's,10',
                             'ORDER_PRICE': 'd',
                             'ORDER_QTY': 'l',
                             'ORDER_STATUS': 'c',
                             'ORDER_TIME': 's,32',
                             'ORDER_UFZ_AMT': 'd',
                             'ORDER_VALID_FLAG': 'c',
                             'QRY_POS': 's,32',
                             'RAW_ORDER_ID': 's,10',
                             'STKBD': 'None',
                             'STKPBU': 's,8',
                             'STK_BIZ': 'n',
                             'STK_BIZ_ACTION': 'n',
                             'STK_CODE': 's,8',
                             'STK_NAME': 's,16',
                             'TRDACCT': 's,10',
                             'TRD_DATE': 'n',
                             'WITHDRAWN_QTY': 'l',
                             }
#当日成交查询
replyMsgParam["10303004"] = {'BOND_INT': 'None',
                             'CUACCT_CODE': 'l',
                             'CUACCT_SN': 'n',
                             'CURRENCY': 'c',
                             'CUST_CODE': 'l',
                             'INT_ORG': 'n',
                             'IS_WITHDRAW': 'c',
                             'MATCHED_AMT': 'd',
                             'MATCHED_PRICE': 'd',
                             'MATCHED_QTY': 'd',
                             'MATCHED_SN': 's,16',
                             'MATCHED_TIME': 's,8',
                             'MATCHED_TYPE': 'c',
                             'ORDER_AMT': 'd',
                             'ORDER_BSN': 'n',
                             'ORDER_DATE': 'n',
                             'ORDER_FRZ_AMT': 'd',
                             'ORDER_ID': 's,10',
                             'ORDER_PRICE': 'd',
                             'ORDER_QTY': 'l',
                             'ORDER_SN': 'n',
                             'ORDER_STATUS': 'c',
                             'QRY_POS': 's,32',
                             'STKBD': 'None',
                             'STKPBU': 's,8',
                             'STK_BIZ': 'n',
                             'STK_BIZ_ACTION': 'n',
                             'STK_CODE': 's,8',
                             'STK_NAME': 's,16',
                             'STK_TRDACCT': 's,10',
                             }
#量化委托
replyMsgParam["10388101"] = {'CLI_ORDER_NO': 's,32',
                             'CUACCT_CODE': 'l',
                             'EXE_INFO': 's,128',
                             'EXE_STATUS': 'c',
                             'ORDER_BSN': 'n',
                             'ORDER_DATE': 'n',
                             'ORDER_NO': 'n',
                             'ORDER_QTY': 'l',
                             'ORDER_TIME': 's,32',
                             'TRD_BIZ': 'n',
                             'TRD_BIZ_ACCTION': 'n',
                             'TRD_CODE': 's,8',
                             'UNDL_CODE': 's,16',
                             }
#应答第一结果集
replyMsgParam["88888888"] = {'MSG_CODE': 'n',
                             'MSG_DEBUG': 's,1024',
                             'MSG_LEVEL': 'c',
                             'MSG_TEXT': 's,256',
                             }


funNameDict = {}
funNameDict["10301105"] = u"用户登录(API)"
funNameDict["10302001"] = u"买卖委托"
funNameDict["10302004"] = u"委托撤单"
funNameDict["10303001"] = u"可用资金查询"
funNameDict["10303002"] = u"可用股份查询"
funNameDict["10303003"] = u"当日委托查询"
funNameDict["10303004"] = u"当日成交查询"
funNameDict["10388101"] = u"量化委托"
funNameDict["88888888"] = u"应答第一结果集"