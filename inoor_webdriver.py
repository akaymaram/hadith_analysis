from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time
import sys
import os
from PIL import Image
import pywhatkit
import importlib
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

'''
Running this script with the total_num_pages, items_per_page, output_file_name, book_ID
commandline arguments, generates a txt file with the provided output_file_name in the outputs
directory containing n (total_num_pages*items_per_page) chain of narrations for n ahadith
Example:
python3 inoor_webdriver.py 2 10 output 1527
generates output.txt in the outputs directory with 20 chains of narration for book 1527 Kitab Suleym
in a python list format with inoor hadith IDs for each list
'''

total_num_pages = sys.argv[1]
items_per_page = sys.argv[2]
output_file_name = sys.argv[3]
book_ID = sys.argv[4]
#://hadith.inoor.ir/fa/hadithlist?pagenumber=1&pagesize=10&sortcolumn=default&sortdirection=asc&searchtype=and&infeild=all&book=1487&isgroup=0&isfulltext=0&iserab=1&pagesizegrouping=10&flexibleforstem=1&flexibleforletter=1&flexibleforroot=0&searchin=hadith

pd.set_option('display.max_rows', None)
# Display all columns
pd.set_option('display.max_columns', None)

print(datetime.datetime.now())
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

def sanad_and_matn_extractor():
	content = driver.find_element(By.CLASS_NAME, 'hadith-content')
	return content.text

def sanad_extractor(sanad_and_matn):
	content = sanad_and_matn.find_element(By.TAG_NAME, 'document')
	return content.text

def hadith_list_extractor():
	content = driver.find_element(By.CLASS_NAME, 'hadith-list')
	return content.text

def hadith_seperator(hadith_list_str):
	list_of_10_hadith = hadith_list_str.split("برای ثبت نمایه، وارد شوید")
	print("list length", len(list_of_10_hadith))
	return(list_of_10_hadith)

def arabic_to_english(arabic_string):
	"""Converts a string containing Arabic numerals to English numerals."""
	arabic_digits = "٠١٢٣٤٥٦٧٨٩"
	english_digits = "0123456789"
	translation_table = str.maketrans(arabic_digits, english_digits)
	return arabic_string.translate(translation_table)

# Example usage
arabic_number = "١٢٣٤٥"
english_number = arabic_to_english(arabic_number)
number_of_pages = int(total_num_pages)
number_of_hadith_per_page = int(items_per_page)

# driver = webdriver.Chrome()
# Get search results for a given date range
# try:

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# left_arrow = driver.find_element(By.CLASS_NAME, "hadith-icon hadith-keyboard-arrow-left")
# left_arrow.click()
# sys.exit('61')

url_start = "https://hadith.inoor.ir/fa/hadithlist?pagenumber="
url_end = f"(&pagesize={number_of_hadith_per_page}&sortcolumn=default&sortdirection=asc&searchtype=and&infeild=all&book={book_ID}&isgroup=0&isfulltext=1&iserab=1&pagesizegrouping=10&flexibleforstem=1&flexibleforletter=1&flexibleforroot=0&searchin=hadith"
list_of_hadith_IDs = []
list_of_locations = []
list_of_sanads = []
list_of_list_of_narrators = []
for page in range(1,number_of_pages+1):
	url = url_start + str(page) + url_end
	print(url)
	driver.get(url)
	time.sleep(10)
	print(page)
	hadith_list = driver.find_element(By.CLASS_NAME, 'hadith-list')
	hadith_list_num = driver.find_elements(By.CLASS_NAME, 'hadith-list ng-tns-c264-15 ng-star-inserted')
	for hadith_element_number in range(1,number_of_hadith_per_page+1):
		try:
			hadith_element_number_str = str(hadith_element_number)
			path = '//*[@id="mat-tab-content-0-0"]/div/div/div[2]/div['+hadith_element_number_str+']'
			hadith_element = hadith_list.find_element(By.XPATH, path)
			document = hadith_element.find_element(By.TAG_NAME, 'document')
			# other tags: exporter, hadithqael,innocent
			narrs = document.find_elements(By.TAG_NAME, 'narrator')
			list_of_narrators = []
			for  narr in narrs:
				narr_name = narr.text.strip()
				list_of_narrators.append(narr_name)
			list_of_list_of_narrators.append(list_of_narrators)
			list_of_sanads.append(document.text.strip())
			hadith = hadith_element.text
			if len(hadith) == 0:
				break
			first_line = hadith.strip().splitlines()[0]
			idx1 = first_line.find("|")
			arabic_nuumeral = first_line[idx1-10:idx1].strip()
			source = first_line[idx1+1:].strip().replace(" نشانی :","")
			list_of_hadith_IDs.append(arabic_nuumeral)
			list_of_locations.append(source)
		except Exception as e:
			print(e)
			


		# content = driver.find_element(By.XPATH, '//*[@id="103902"]/a/div/p/hadith/document')
		# print(content.text)
	# left_arrow = driver.find_element()
	# left_arrow.click()
	# iframe = driver.find_element(By.CLASS_NAME, "hadith-icon hadith-keyboard-arrow-left")
	# ActionChains(driver)\
	# .scroll_to_element(iframe)\
	# .perform()
	# print(list_of_hadith_IDs)
	# for x in list_of_locations:
	# 	print(x)
	# for x in list_of_sanads:
	# 	print(x)
	# for x in list_of_list_of_narrators:
	# 	print(x)
	driver.implicitly_wait(3)


driver.quit()
data1 = {'hadith_IDs': list_of_hadith_IDs, 'chain': list_of_list_of_narrators}
df1 = pd.DataFrame(data1)
# pd.set_option('display.max_colwidth', None)
df1.reset_index(inplace=True)
print(df1)
df1.to_csv('outputs/'+ output_file_name +'.txt', index=False)



# except Exception as e:
# 	driver.quit()
# 	sys.exit(e)


# driver.quit()


		