__author__ = 'sexybaby'
# -*- coding: UTF-8 -*-
'''
发送txt文本邮件
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

mailto_list=["liushengjie_qt@he.chinamobile.com"]
mail_host="smtp.he.chinamobile.com"  #设置服务器
mail_user="liushengjie_qt@he.chinamobile.com"    #用户名
mail_pass="1qaz@WSX"   #口令
mail_postfix="he.chinamobile.com"  #发件箱的后缀

def send_mail_text(to_list,sub,content):
    me="hello"+"<"+mail_user+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False

def send_mail_html(to_list,sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="hello"+"<"+mail_user+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='gb2312')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, to_list, msg.as_string())  #发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail_text(mailto_list,"hello","hello world！"):
        print "发送成功"
    else:
        print "发送失败"

    if send_mail_html(mailto_list,"hello","<a href='http://www.baidu.com'>liushengjie</a>"):
        print "发送成功"
    else:
        print "发送失败"