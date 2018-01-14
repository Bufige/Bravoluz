#from selenium import webdriver
#from webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup
#we import the variables from the namespace that called this program!
from __main__  import FILENAME_LINKS, URL_CATEGORY




links = []


for pos in range(1,8):
	url_tmp = URL_CATEGORY
	url_tmp +=  str(pos)

	req = requests.get(url_tmp)
	page = req.text
	soup = BeautifulSoup(page,'lxml')

	products_link = soup.find_all('div', 'image image-swap-effect')

	count = 1
	for product in products_link:
		if count > 6:			
			links.append(product.a['href'])		
		count += 1

file = open(FILENAME_LINKS,"w+")

for link in links:
	file.write(link + "\n")
file.close()