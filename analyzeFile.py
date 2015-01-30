__author__ = 'sexybaby'
# coding:gbk

f = open("/Users/sexybaby/Downloads/catalina.2015-01-26.log")             # 返回一个文件对象
line = f.readline()             # 调用文件的 readline()方法
while line:
    if line.find("printResultMessage") != -1:
        line = f.readline()
        x = open(r"./log.txt",'a')
        x.write(line)
        print line,
    else:
        line = f.readline()

f.close()