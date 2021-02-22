#coding:utf-8
import yaml
from lib.sendrequest import SendRequests
import urllib3
import unittest,ddt
from base.base import Base
urllib3.disable_warnings()
from config import setting



dictresult =Base.get_value(setting.dynamics)
@ddt.ddt
class Demo_API(unittest.TestCase):
    """听芝app测服接口"""
    def setUp(self):
        print("测试开始")
    @ddt.data(*dictresult)
    def test_demoapi(self,data):
        print(data)
        print(data['number'])
        results = SendRequests().sendRequests(data)
        print(results)
        # if data['ifneed']=='y':
        #    # f = open(setting.Test_Yaml,'a+',encoding='utf-8')
        #    # re=str(results)
        #    # read=yaml.dump(results['data']['uid'])
        #    # f.write(read)
        #     file = open(setting.Test_Dynamics,"r",encoding='utf-8')
        #     content =file.read()
        #     findname="uid"
        #     findnames="serve_ids"
        #     pos = content.find(findname)
        #     posone = content.find(findnames)
        #     if pos !=-1:
        #         #content=content[:pos]+content_add+content[pos:]
        #         content=content[:pos+4]+' '+results['data']['uid']+'\n'+"           "+content[posone:]
        #         file = open(setting.Test_Dynamics,"w",encoding='utf-8')
        #         file.write(content)
        #         file.close()

        findname="uid"
        findnames="serve_ids"
        base = Base()
        base.dynamics(setting.Test_Dynamics,findname,findnames,results,data)
        base.check_result(results,data['check'])

    def tearDown(self):
        print("测试结束")


if __name__ == "__main__":
    unittest.main()