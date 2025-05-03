from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime
import time
import sys
import os
import importlib

'''
Running this script with the csv output file name as a command line argument
generates the first 25 manabeh from the manabeh list.
Example:
python3 manabeh_generator.py manabeh.csv
generates manabeh.csv in the same directory of this script with the first 25 manabeh
'''

url = "https://hadith.inoor.ir/fa/hadithlist?pagenumber=1&pagesize=10&sortcolumn=default&sortdirection=asc&searchtype=and&infeild=all&isgroup=0&isfulltext=0&iserab=1&pagesizegrouping=10&flexibleforstem=1&flexibleforletter=1&flexibleforroot=0&searchin=hadith"

output_name = str(sys.argv[1])

def manabeh_element_parser(element_text):
	lines = element_text.splitlines()
	counts = []
	titles = []

	for i, line in enumerate(lines):
		if (i + 1) % 2 == 0:
			counts.append(int(line.strip().strip("()")))
		else:
			titles.append(line.strip())

	return [titles, counts]

print(datetime.datetime.now())
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

driver.get(url)
time.sleep(10)
try:
	web_element = driver.find_element(By.TAG_NAME, 'tree-node-collection')
	source_and_count_list = manabeh_element_parser(web_element.text)
	data = {'source_title': source_and_count_list[0], 
		 'hadith_count': source_and_count_list[1]}
	print(data)
	df = pd.DataFrame(data)
	print(df)
	print(output_name)
	df.to_csv('outputs/'+ output_name, encoding='utf-8-sig', index=True)

except Exception as e:
	print(e)
	print('got the above Exception')

driver.quit()