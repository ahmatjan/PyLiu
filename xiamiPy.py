__author__ = 'sexybaby'
import urllib2
from lxml import etree
def str2url(s):
    #s = '9hFaF2FF%_Et%m4F4%538t2i%795E%3pF.265E85.%fnF9742Em33e162_36pA.t6661983%x%6%%74%2i2%22735'
    num_loc = s.find('h')
    rows = int(s[0:num_loc])
    strlen = len(s) - num_loc
    cols = strlen/rows
    right_rows = strlen % rows
    new_s = s[num_loc:]
    output = ''
    for i in xrange(len(new_s)):
        x = i % rows
        y = i / rows
        p = 0
        if x <= right_rows:
            p = x * (cols + 1) + y
        else:
            p = right_rows * (cols + 1) + (x - right_rows) * cols + y
        output += new_s[p]
    return urllib2.unquote(output).replace('^', '0')

def getIdrexml(s):
    #s = 'http://www.xiami.com/song/2262654?spm=a1z1s.3521865.23309997.1.VJOkkm'
    id = s[int(s.rfind('/')) + 1 : int(s.find('?'))]
    return 'http://www.xiami.com/song/playlist/id/' + id + '/object_name/default/object_id'

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else []

if __name__ == '__main__':
    url = getIdrexml('http://www.xiami.com/song/2262654?spm=a1z1s.3521865.23309997.1.VJOkkm')
    print url

    send_headers = {
         'Host': 'www.xiami.com',
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    req = urllib2.Request(url,headers=send_headers)
    r = urllib2.urlopen(req)
    html = r.read()

    root = etree.XML(html)
    tree = etree.ElementTree(root)
    tree.ElementTree()
    #print  str2url('7h%5xo2%%8F48%_5f55c%4%%lt2.imF2552__3ke3EEb5255tFfa%8FE122lFeff5b3E1EEp%im272%965.ay%8be158%-%2liF%72727mu%5a79cd85n3Fe.158F%63pt3E8c4b-4EuAm.c%E712553hDf%%fc18-l')

