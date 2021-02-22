import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
Test_Dynamics= os.path.join(BASE_DIR,"testcase","test.yaml")
Test_Yaml= os.path.join(BASE_DIR,"testcase","test_one.yaml")
#配置文件
Test_Config = os.path.join(BASE_DIR,"config","config.ini")
#测试用例报告
Test_Report = os.path.join(BASE_DIR,"reports")
#测试用例程序文件
Test_Case = os.path.join(BASE_DIR,"main")

all=[]
all.append(Test_Yaml)
dynamics=[]
dynamics.append(Test_Dynamics)
#all.append(Test_One)
print(all)