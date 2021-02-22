import unittest
import yaml
import os
class Base(unittest.TestCase):

   def check_result(self,response,data):
       # for key in data:
       #     for jey in response:
       #         if key == jey:
       #             print(key,response[key])
       #             print(key,data[key])
       #             response_values=str(response[key])
       #             data_values=str(data[key])
       #             print(response_values,data_values)
       #             self.assertEqual(response_values,data_values,"返回实际结果是->:%s" % response_values)

        key1=response.keys()
        key2=data.keys()
        for key in key2:
            print(key)
            if key in key2 and key in key1:
              response_values=str(response[key])
              data_values=str(data[key])
              print(response_values,data_values)
              self.assertEqual(response_values,data_values,"返回实际结果是->:%s" % response_values)
            else:
              #print("没有找到：",key)
              raise Exception("没有找到：",key)


   def new_report(testreport):
    """
    生成最新的测试报告文件
    :param testreport:报告所在文件夹
    :return:返回文件
    """
    #返回指定的文件夹包含的文件或文件夹的名字的列表
    lists = os.listdir(testreport)
    #print(lists)
    #sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
    #最后对lists元素，按文件修改时间大小从小到大排序。
    #获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    lists.sort(key = lambda fn:os.path.getmtime(testreport +"\\"+fn))
    #连接testreport和list[-1]的值
    file_new = os.path.join(testreport,lists[-1])
    return file_new

   def get_yaml(filepath):
      f = open(filepath,'r',encoding='utf-8')
      result = f.read()
      #filename=Base.open_files(self,filepath)
      dictresult = yaml.load(result,Loader=yaml.FullLoader)
      print(dictresult)
      f.close()
      return dictresult

   def get_value(name):
        allData=[]
        for i in range(len(name)):
            allData += Base.get_yaml(name[i])
        print(allData)
        return allData


   def dynamics(self,filepath,findtargit,findother,response,data):
        if data['ifneed']=='y':
           # f = open(setting.Test_Yaml,'a+',encoding='utf-8')
           # re=str(results)
           # read=yaml.dump(results['data']['uid'])
           # f.write(read)
            file = open(filepath,"r",encoding='utf-8')
            content =file.read()
            findname=findtargit
            findnames=findother
            pos = content.find(findname)
            posother = content.find(findother)
            if pos !=-1:
                #content=content[:pos]+content_add+content[pos:]
                content=content[:pos+4]+' '+response['data'][findtargit]+'\n'+"           "+content[posother:]
                file = open(filepath,"w",encoding='utf-8')
                file.write(content)
                print(content)
                file.close()
