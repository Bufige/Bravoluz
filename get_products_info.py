import requests
from bs4 import BeautifulSoup
from __main__  import FILENAME_LINKS


#list of maps
data = []


#open file
file = open(FILENAME_LINKS,"r+")


#function to get correctly our desired output, which is a list of products that are compatible
def fix_compatibility_output(str):
	
	#replace each break of new line in HTML to break in text line.
	str = str.replace('<br/>','\n')
	
	# temp variable to hold the data we want
	tmp = ""

	#bool to set the current state of our search.
	found = False
	#loop through the string.
	for c in str:
		#it is the beggining of a div?
		if c == '<':
			#yes
			found = True
		elif c == '>': #it is the end?			
			found = False
		else: # if not the cases above.
			# if found = true, it means we are inside a tag. doesn't matter if it is opening a tag or closing.
			if not found: # we are not inside, therefore we can add the current char to our temp variable.
				tmp += c			
	#return the data.
	return tmp



#we go through each line
for line in file:

	#clear the content
	url_tmp = line.strip()

	#map with the info we want

	data_temp = {}

	#request to the url we got.
	req = requests.get(url_tmp)
	#get its text.
	page = req.text
	#send to bs4
	soup = BeautifulSoup(page,'lxml')

	#here we do the stuff to get what we want.

	product_title = soup.find('div', class_ ='product-name').get_text().strip()
	product_image = soup.find('div', class_ = 'item').a['href']
	product_model = soup.find('div', class_ = 'description').find('span',class_="value").get_text().strip()
	product_price = soup.find('span', id='price-old').get_text().strip()


	tmp_categories = soup.find_all('div', 'inline')[3].find_all('a')
	

	product_categories = ''.join((category.get_text().strip() + ',') for category in tmp_categories)

	
	product_description = soup.find('div', id='tab-description').find_all()[0].text
	
	
	product_compatibility = fix_compatibility_output(str(soup.find_all('div','tab-content')[1]))

	data_temp['title'] = product_title
	data_temp['image'] = product_image
	data_temp['model'] = product_model
	data_temp['categories'] = product_categories
	data_temp['description'] = product_description
	data_temp['compatibility'] = product_compatibility
	
	#we append our map to the list of maps.
	data.append(data_temp)	
	
# file no longer needed, therefore we delete it.

file.close()
