

# 获取签名的装饰器(方法) servletPath接口地址v5.0之后的路径,reauestType接口的请求类型 --装饰器类型的方法
import json

import requests

from bean.UrlParams import UrlParams
from config import GlobalConfig, ReadConfigFile
from config.GlobalConfig import setGlobalPumkinUserId
from logger.logge import logger


class CallApiAspect(BaseException):
    def aroundHandle(self,servletPath: str, reauestType: str) -> UrlParams():
        def listenTokenApi(func):
            def obtainToken(*args, **kwargs):
                logger.info("我执行了" + str(func.__name__))
                urlParams = UrlParams()
                f = False
                for key in args:
                    if isinstance(key, UrlParams):
                        urlParams = key
                        f = True
                # if GlobalConfig.getGlobalPumPkinToken() is None:
                #     # 组装获取签名的url链接，java项目无法区别是线上还是测试环境所以需要传全部的链接
                #     phone = ReadConfigFile.classNameAndFieldName("phone", "phone")
                #     middleParmDomain = ReadConfigFile.classNameAndFieldName("domainname", "middleParmDomain")
                #     secretApiPrifx = ReadConfigFile.classNameAndFieldName("domainname", "secretApiPrifx")
                #     userLogin = ReadConfigFile.classNameAndFieldName("user", "userLogin")
                #     # 登录接口的全链接
                #     secretApiPrifx = secretApiPrifx + middleParmDomain + userLogin
                #     apiPrifx = ReadConfigFile.classNameAndFieldName("domainname", "apiPrifx")
                #     header = ReadConfigFile.classNameAndFieldName("header")
                #     # 线上/测试的域名链接，不是全链接
                #     envPrifx = ReadConfigFile.classNameAndFieldName("domainname", "envPrifx")
                #     # 拼接请求链接的参数
                #     dataSource = {"envPrifx": envPrifx, "phone": phone, "secretApiPrifx": secretApiPrifx, "apiPrifx": apiPrifx,
                #                   "headerClass": header}
                #     params = UrlParams.UrlParams()
                #     # java项目的请求地址
                #     params.url = "http://127.0.0.1:8089/pythonLoginGetToken"
                #     # 获取返回的token
                #     response = requests.get(params.url, dataSource)
                #     s = str(response.content.decode('utf8'))
                #     GlobalConfig.setGlobalPumPkinTokenInfoMap(s)
                #     setGlobalPumkinUserId(s['user_id'])
                # # 这里是需要写使用Token去换取签名和时间搓
                # tokenInfoMap = GlobalConfig.getGlobalPumPkinTokenInfoMap()
                # loads = json.loads(tokenInfoMap)
                # url = "http://127.0.0.1:8089/pythonUpdateToken"
                # token_ = loads['token']
                # httpParam = {"pyToken": token_, "servletPath": servletPath, "requestType": reauestType}
                # signatureSecretInfo = requests.get(url, httpParam)
                # signatureSecretContent = str(signatureSecretInfo.content.decode('utf8'))
                # json_loads = json.loads(signatureSecretContent)
                # headerInfo = ReadConfigFile.classNameAndFieldName("header")
                # for key in json_loads.keys():
                #     headerInfo[key] = json_loads[key]
                # # 取出最新的请求头放入实体类中
                # urlParams.headMap = ReadConfigFile.classNameAndFieldName("header")
                # args.__add__(tuple([urlParams]))

                # 以下为测试数据
                urlParams.headMap = {""}
                name = ReadConfigFile.classNameAndFieldName('header')
                for key in name:
                    urlParams.headMap[key] = name[key]
                setGlobalPumkinUserId('4017434')
                if urlParams.url is None:
                    urlParams.url = 'url' + servletPath
                # 如果传了UrlParams可以直接使用args 如果没传就需要指定参数
                if f :
                    args.__add__(tuple([urlParams]))
                else:
                    kwargs['urlParams'] = urlParams
                test_func = func(*args, **kwargs)
                return test_func
            return obtainToken

        return listenTokenApi



if __name__ == '__main__':
    s = {"pythonSessionId": "ee103ab1bbc64611bd78d1c13ef38b95", "phone": "14100000001", "user_id": "39593318",
         "token": "1OV26uhk2VfVFzD1"}
    keys = s.keys()
    for key in keys:
        print(key)
