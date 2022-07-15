"""
    @author : siftikharm
    date : 15/7/2022
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
from datetime import datetime
import os
import sys

os.path.dirname(sys.executable)
currentTime = datetime.now()
date = currentTime.strftime('%d-%m-%y')

website = r'https://arynews.tv/'
path = r"C:\Users\sifti\Downloads\chromedriver.exe"

# HeadLess mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

links = []
titles = []

containers = driver.find_elements(by='xpath', value='//div[@class="td-module-meta-info"]/h3')
for container in containers:
    try:
        title = container.find_element(by='xpath', value='./a').get_attribute('title')
        link = container.find_element(by='xpath', value='./a').get_attribute('href')
        titles.append(title)
        links.append(link)
    except:
        print("Not found")

containers = driver.find_elements(by='xpath', value='//div[@class="td-module-meta-info"]/h4')
for container in containers:
    try:
        title = container.find_element(by='xpath', value='./a').get_attribute('title')
        link = container.find_element(by='xpath', value='./a').get_attribute('href')
        titles.append(title)
        links.append(link)
    except:
        print("Not found")

filename = f"AryNews-Headlines-{date}.csv"
finalPath = os.path.join(path, filename)
dictionary = {'Title': titles, 'Link': links}
dataFrame = pd.DataFrame(dictionary)
dataFrame.to_csv(filename)

driver.quit()
