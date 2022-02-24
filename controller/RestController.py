from flask import request

from CallApiLayer.SearchCallApi import SearchCallApi
from aspect.ControllerAspect import ControllerAspect
from config import ReadConfigFile, GlobalConfig
from config.FlaskConfig import flask
from dao.DatabaseOperation import DatabaseOperation
from testCase.ActorTestCase import ActorTestCase
from testCase.HallTestCase import HallTestCase
from testCase.HomeTestCase import HomeTestCase
from testCase.MovieTestCase import MovieTestCase
from testCase.QrCodeTestCase import QrCodeTestCase
from testCase.SearchTestCase import SearchTestCase
from testCase.SystemInfoTestCase import SystemInfoTestCase
from testCase.UserTestCase import UserTestCase
from utils import ResponseUtils


@flask.route("/notice", methods=['GET', 'POST'])
@ControllerAspect.listenControllerMethod(ControllerAspect())
def postMethod():
    envPrifx = request.args.get('envPrifx')
    phone = request.args.get('phone')
    # 更新环境数据
    updataEnvInfoConfig(envPrifx, phone)


    globleReport = GlobalConfig.getReportClassInfo()
    return ResponseUtils.reportToStrModelAndView(globleReport)


# 更新域名
def updataEnvInfoConfig(envPrifx: str = None, phone=None):
    if envPrifx is not None and envPrifx != '':
        # 项目中配置的默认就是bea环境数据，如果不是beta环境就为测试环境将域名改成测试环境，线上环境不能使用，需要特殊配置，如有需要自己改这里的代码
        if envPrifx is not None and 'beat' not in envPrifx:
            headerMap = ReadConfigFile.classNameAndFieldName('header')
            headerMap['envPrifx'] = envPrifx
            headerMap['apiPrifx'] = None
            headerMap['dorasPrifx'] = None
            headerMap['secretApiPrifx'] = None
        # 如果传入的手机号码有指定则使用指定的手机号码,没有指定就使用默认的
        if phone is not None and phone != '':
            phone = ReadConfigFile.classNameAndFieldName('phone')
            phone['phone'] = phone


@flask.route("/searchReport", methods=['GET', 'POST'])
def searchReportByMillers():
    millis = request.args.get('millis')
    report = DatabaseOperation().searchReport(millis)
    return ResponseUtils.responseModelAndView(report)


flask.run()
