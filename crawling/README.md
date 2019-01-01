# Crawling
## Code Template
~~~python
from bs4 import BeautifulSoup
import urllib, urllib.request, urllib.parse
import re, os, time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

url_format = "https://someUrl?[queries]={}"
def request_and_extract(iter_index):
	query_values = [] # using iter_index
	url = url_format.format(*query_values))
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	# extract data using beautifulsoup object
	return data
def crawle_and_save(iter_index):
	try:
		result = request_and_extract(iter_index) 
	except urllib.error.HTTPError as e: return
	except Exception as e:print(e);exit()
	if not result: return
	 
	with open('./result_data/%d'%iter_index, 'w') as f:
		# save it
	time.sleep(1)

with ThreadPoolExecutor(max_workers=5) as executor:
	for iter_index in range(iter_end):
		try:
			executor.submit(crawle_and_save, iter_index)
		except KeyboardInterrupt:
			# some logging
			# backup saving
			exit()
~~~
