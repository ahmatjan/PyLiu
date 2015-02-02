__author__ = 'sexybaby'
import urllib2
import HTMLParser
from bs4 import BeautifulSoup
import time

def str2url(s):
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

def getIdsXML(ids):
    return ['http://www.xiami.com/song/playlist/id/' + id + '/object_name/default/object_id.xml' for id in ids]

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else []

if __name__ == '__main__':

    send_headers = {
         'Host': 'www.xiami.com',
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:34.0) Gecko/20100101 Firefox/34.0',
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    req = urllib2.Request("http://www.xiami.com/space/lib-song/u/37524414",headers=send_headers)
    r = urllib2.urlopen(req)
    html = r.read()

    soup = BeautifulSoup(html)
    # print(soup.prettify())

    song_ids = [ link.get('id')[int(link.get('id').rfind('_')) + 1 : ] for link in soup.find_all('tr') if link.get('id') != None ]

    xmls = getIdsXML(song_ids)
    html_parser=HTMLParser.HTMLParser()

    for xml in xmls:
        req_song = urllib2.Request(xml,headers=send_headers)
        #print urllib2.urlopen(req_song).read()
        soup_song = BeautifulSoup(urllib2.urlopen(req_song).read(),features='xml')
        # print soup_song
        time.sleep(3)

        if soup_song.find('location') != None :
            print html_parser.unescape(soup_song.title.string) + ": " +str2url(soup_song.find('location').string)
