import urllib2

import time
from datetime import datetime

proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:6789"})
#need to port setting
opener = urllib2.build_opener(proxy_support) 

request = urllib2.Request("http://en.wikipedia.org/wiki/Main_Page")
request.add_header('Pragma','no-store,no-cache,must-revalidate')
request.add_header('Cache-Control', 'no-cache')

urllib2.install_opener(opener)
opened = urllib2.build_opener(proxy_support)
    
text = open("basetime.txt",'a')

for i in range(0, 5):#how many access?
   

    #proxy_support = urllib2.ProxyHandler({"http" : "127.0.0.1:6789"})


    start = time.time()

    
    
    content = opened.open(request)
    contrd = content.read()

    end = time.time()
    result = end - start

    
    #now = datetime.now()
    text.write("%s\n" % (result))
