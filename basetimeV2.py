import urllib2

import time
from datetime import datetime

text = open("basetime.txt",'a')

request = urllib2.Request("http://en.wikipedia.org/wiki/Main_Page")
request.add_header('Pragma','no-store,no-cache,must-revalidate')
request.add_header('Cache-Control', 'no-cache')

for i in range(0, 100):#how many access?

    proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:6789"})
    opener = urllib2.build_opener(proxy_support)
    print "Start", i
    start = time.time()
    f = opener.open(request)
    html = f.read()
    print "recv html"
    f.close()
    end = time.time()

    result = end - start
    
    text.write("%s\n" % (result))
