#!/usr/bin/python3

import requests

# now make the request
url = 'http://158.69.76.135/level0.php'
proxies = {'https' : '47.254.89.62:8080',
           'https': '153.149.170.11	:3182'}
session = requests.Session()
for i in range(1024):
	h = session.head(url, allow_redirects=True)
	print(h)
	r = session.get(url, proxies=proxies)
	print(r)
	s = session.post('http://158.69.76.135/level0.php', data='269')
	print(s)
	print("voted {} times".format(i))
print("done")


