import os
from openpyxl import Workbook


# here we have url for the category that we want to search. 
'''
Yes, we could make another script to get every category and make this a list and pass to the other script to return our links.
By doing that, we would have to change our other script a little bit to work. In case you want to do so, just put the loop there inside
the loop of a new loop that go through each category. Each category link should be assigned to "url_tmp" and it should work.
'''
URL_CATEGORY = 'https://bravoluz.com.br/shop/medicas-cientificas?page='

# if this file doesn't exists, it will run the other python file to get the list of links to acess.
FILENAME_LINKS = "links.txt"
#excel output filename

FILENAME_EXCEL_OUPUT = "output.xlsm"

if not os.path.exists(FILENAME_LINKS):
	import get_links


#we get all the products info!
import get_products_info
#we post the data into excel. 
import post_excel

#here we start working on importing our data to the excel!