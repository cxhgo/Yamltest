#coding:utf-8
import yaml
from lib.sendrequest import SendRequests
import urllib3
import unittest,ddt
from base.base import Base
urllib3.disable_warnings()
from config import setting
from lib.sendrequestheader import SendRequestsHeader


# f = open(setting.Test_Yaml,'r',encoding='utf-8')
# result = f.read()
#
# def get_yaml():
#      filename=Base.open_files(setting.Test_Yaml)
#      dictresult = yaml.load(filename,Loader=yaml.FullLoader)
#      print(dictresult)
#      return dictresult
#print(result)


#filename=setting.all
#def test(filename=setting.Test_Yaml):
# dictresult = Base.get_yaml(setting.Test_Yaml)
# one=Base.get_yaml(setting.Test_One)
# all=dictresult+one
dictresult =Base.get_value(setting.all)
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
        headers = SendRequestsHeader.sendRequestsheader(self,data)
        print(results)
        if data['ifneed']=='y':
           # f = open(setting.Test_Yaml,'a+',encoding='utf-8')
           # re=str(results)
           # read=yaml.dump(results['data']['uid'])
           # f.write(read)
            file = open(setting.Test_Yaml,"r",encoding='utf-8')
            content =file.read()
            findname="uid"
            findnames="serve_ids"
            pos = content.find(findname)
            posone = content.find(findnames)
            if pos !=-1:
                #content=content[:pos]+content_add+content[pos:]
                content=content[:pos+4]+' '+results['data']['uid']+'\n'+"           "+content[posone:]
                file = open(setting.Test_Yaml,"w",encoding='utf-8')
                file.write(content)
                file.close()


        base = Base()
        base.check_result(results,data['check'])
        #base.check_result(headers,data['check'])

    def tearDown(self):
        print("测试结束")


if __name__ == "__main__":
    unittest.main()