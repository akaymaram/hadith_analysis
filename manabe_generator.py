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


def arabic_to_english_numeral_converter(arabic_string):
    english_string = ''
    for char in arabic_string:
        if '٠' <= char <= '٩':
            english_string += str(ord(char) - ord('٠'))
        else:
            english_string += char
    return int(english_string)

def arrange_lines(text):
    lines = text.splitlines()
    counts = []
    titles = []

    for i, line in enumerate(lines):
        if (i + 1) % 2 == 0:
            print('even:', line)
            counts.append(int(line.strip().strip("()")))
        else:
            titles.append(line.strip())
            print('odd:', line)
    
    max_lines = max(len(counts), len(titles))

    return [counts,titles]

print(datetime.datetime.now())
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options)

url = sys.argv[1]
driver.get(url)
time.sleep(10)
try:
	Manba = driver.find_element(By.TAG_NAME, 'tree-node-collection')
	lines = Manba.text
	lines = arrange_lines(lines)
	data = {'source': lines[0], 
         'count': lines[1]}
	df = pd.DataFrame(data)
	print(df)




except Exception as e:
	print(e)
	print('got an Exception')

driver.quit()
sys.exit("26")