__author__ = 'sexybaby'
# coding:gbk

f = open("/Users/sexybaby/Downloads/catalina.2015-01-26.log")             # ����һ���ļ�����
line = f.readline()             # �����ļ��� readline()����
while line:
    if line.find("printResultMessage") != -1:
        line = f.readline()
        x = open(r"./log.txt",'a')
        x.write(line)
        print line,
    else:
        line = f.readline()

f.close()