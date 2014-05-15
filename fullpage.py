import requests
import re
import time
from multiprocessing import Process, Pool
import urllib2


text = open("fullpage.txt",'a')

def http_get(image):
	
	result = {"url": image, "data": requests.get(image, headers=headers,proxies=proxies)}
	return result




for i in range(0, 5):#how many access?

	start1 = time.time()

	headers = {'cache-control':'no-cache'}
	proxies = {"http":"http://127.0.0.1:6789",}#portcontrol
	website = requests.get('http://en.wikipedia.org/wiki/Main_Page', headers=headers)


	html = website.text
	pat = re.compile(r'<\s*img [^>]*src="([^"]+)')
	img = pat.findall(html)

	imglen = len(img)

	for num in range(0,imglen) :
		img[num] = 'http:'+img[num]

	
	
	opener = urllib2.build_opener() 
	
	pool = Pool(processes = imglen)

	results = pool.map(http_get, img)
	#for result in results:
		#print result
	end2 = time.time()

	
	res = end2 - start1
	pool.close()
	time.sleep(1.5)
	

	text.write("%s\n" % (res))
	
