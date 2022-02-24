from bean.CheckResponseResult import CheckResponseResult
from config import FlaskConfig, GlobalConfig
from logger.logge import logger
from utils import ResponseUtils


class ControllerAspect:
    # 监控接口层
    def listenControllerMethod(self):
        def handlerFunc(func):
            def handlerControllerExcept(*args, **kwargs):
                logger.info("正在进行监控")
                t = None
                try:
                    t = func(*args, **kwargs)
                except BaseException() as e:
                    logger.info(e)
                    result = {"result": "执行过程中出现错误,请检查项目"}
                    return ResponseUtils.responseModelAndView(result)

                finally:
                    # 最后重置报告数据
                    GlobalConfig.setRepotClassInfo(CheckResponseResult())
                    # 此处要加上邮件报告
                    logger.info("记得发报告")

                return t
            return handlerControllerExcept
        return handlerFunc
