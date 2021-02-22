# _*_ coding:utf-8 _*_
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser
from config import setting
from base.base import Base

def send_mail():
    """
    定义发送邮件
    :param file_new:
    :return: 成功：打印发送邮箱成功；失败：返回失败信息
    报告中测试用例名称需要修改ddt.py获取表格中的case_name显示
    """
    # f = open(file_new,'rb')
    # mail_body = f.read()
    # f.close()
    #发送附件
    con = configparser.ConfigParser()
    con.read(setting.Test_Config,encoding='UTF-8')
    report =Base.new_report(setting.Test_Report)
    sendfile = open(report,'rb').read()
    # --------- 读取config.ini配置文件 ---------------
    Hoster = con.get("user","HOST_SERVER")
    Sender = con.get("user","FROM")
    Receiver =con.get("user","TO")
    if '['in Receiver:
      receiver = eval(Receiver)#将字符串变成列表类型，同时发送多人
    else:
      receiver = Receiver
    User = con.get("user","user")
    Pwd = con.get("user","password")
    Subject = con.get("user","SUBJECT")
    att = MIMEText(sendfile,'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment", filename=("gbk", "", report))

    msg = MIMEMultipart('related')
    msg.attach(att)
    #msgtext = MIMEText(mail_body,'html','utf-8')
    msgtext = MIMEText('接口报告','plain','utf-8')
    msg.attach(msgtext)
    msg['Subject'] = Subject
    msg['From'] = Sender
    msg['To'] = ''.join(receiver)
    #msg['To'] =Receiver


    try:
        server = smtplib.SMTP()
        #server.set_debuglevel(1)#打开debug输出模式
        server.connect(Hoster)
        server.starttls()
        server.login(User,Pwd)
        server.sendmail(Sender,receiver,msg.as_string())
        server.quit()
        print("邮件发送成功！")
    except Exception as  e:
        print("失败: " + str(e))