__author__ = 'sexybaby'
import urllib2
import string
import re


outstring = ''
fp = open('in.data','r')
for line in fp:
	for letter in line:
		if letter >= 'a' and letter <= 'z':
			outstring += letter
fp.close()
print outstring

#
# import string
# fp = open('in.data','r')
# print filter(lambda x: x in string.letters, fp.read())
# fp.close()


# outstring = ''
# dic = {}
# fp = open('in.data','r')
# for line in fp:
# 	for letter in line:
# 		if letter in dic:
# 			dic[letter] += 1
# 		else:
# 			dic[letter] = 1
# 		if letter >= 'a' and letter <= 'z':
# 			outstring += letter
# fp.close()
# lst = dic.items()
# lst.sort(key = lambda x : x[1])
# for x in lst:
# 	print x
# print outstring

# f = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()
#
# print f

#print filter(lambda x: x in string.letters, fp.read())

# html = "<!--  aa  -->"
#
# if __name__ == '__main__':
#     p = re.compile('\<\!\-\-(.*)\-\-\>',re.M)
#     match = p.search(html).group()
#     print match[0],match[1]