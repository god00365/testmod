import requests
import re
import time
from multiprocessing import Process, Pool
import urllib2
import os

text = open("fullpage.txt",'a')

def http_get(image):
    pid = os.getpid()
    print "start of %s" % (pid)
    result = requests.get(image, headers=headers,proxies=proxies)
    
    print "%s's connection %s" % (pid,result.headers['connection'])
    print "%s's content-length %s" % (pid,result.headers['content-length'])
    return result




for i in range(0, 1):#how many access?

    start1 = time.time()

    headers = {'cache-control':'no-cache'}
    proxies = {"http":"http://127.0.0.1:8118",}#portcontrol
    website = requests.get('http://en.wikipedia.org/wiki/Main_Page', headers=headers,proxies=proxies)


    html = website.text
    pat = re.compile(r'<\s*img [^>]*src="([^"]+)')
    img = pat.findall(html)

    imglen = len(img)

    for num in range(0,imglen) :
        img[num] = 'http:'+img[num]

    
    
    #opener = urllib2.build_opener() 
    
    pool = Pool(processes = imglen)

    results = pool.map(http_get, img)
    #for result in results:
        #print result
    end2 = time.time()

    
    res = end2 - start1
    
    pool.close()
    time.sleep(1.5)
    

    text.write("%s\n" % (res))
