# pythonProjectInterface
pythonProjectInterface 接口自动化
为自行封装使用，如有不妥之处请留言，以下列举推广后比较好的地方
1.以接口形式对外开放对使用者要求极低，和其他部门联动十分友好
2.内部采用多层封装隔离，如：
   数据隔离，用例层，接口层，开放接口层，request层
   当需要进行性能测试时直接将locust注解加上就能进行压测
   application-devUser.yml 存放与User相关的接口
3.可提供给开发人员自行冒烟测试，和历代版本的接口回归，快速有效
4.可提供给运维/客服进行环境判断，和环境部署后的环境监测
5.可直接部署到服务器上定时执行监控服务器状态(如需监控端口和CPU等服务器数据需额外添加配置)
   另：该项目删除了链接数据库和敏感数据，会对代码阅读造成不适，尽情谅解
   运行文件为：RestController.py文件，进行接口访问
   PS:该项目已经顺利推广多个部门中使用
