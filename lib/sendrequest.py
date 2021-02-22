# _*_ coding:utf-8 _*_
import os,sys,json
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import requests
import urllib3
urllib3.disable_warnings()

class SendRequests():
    def sendRequests(self,apiData):
        """
        发送接口请求
        :param apiData:接口请求数据
        :return: 返回接口响应信息，以json格式
        """
        try:
            #发送请求数据
            method = apiData["method"]
            # print(method)
            url = apiData["url"]
            # print(url)
            if apiData["params"] == "":
                par = None
            else:
                par = apiData["params"]
                # print(par)
            if apiData["headers"] == "":
                h = None
            else:
                h = apiData["headers"]
                print(h)
            if apiData["body"] == "":
                body_data = None
            else:
                body_data = apiData["body"]

            type = apiData["type"]
            #print(type)
            v = False
            if type == "data":
                body = body_data
                #print(body)
            elif type == "json":
                body =json.dumps(body_data)
            else:
                body = body_data
                #print(body)
            re =requests.request(method=method,url =url, headers =h,params = par,data=body,verify = v)
            print(re)
            msg = json.loads(re.text)
            # print(msg)
            msg['status_code']=re.status_code
            header = re.headers
            print(header)
            #print(msg)
            #print(re.status_code)
            return msg
            #print(re.text)
            # if method =="get":
            #    re = s.get(url =url, headers =h,params = par,data = body,verify = v)
            #    print(re.text)
            #    return re
            # elif method == "post":
            #    re = s.post(url =url, headers =h,params = par,data = body,verify = v)
            #    print(re.text)
            #    return re
        except Exception as e:
            print(e)