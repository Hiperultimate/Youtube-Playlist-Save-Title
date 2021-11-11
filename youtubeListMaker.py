from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge(executable_path = r'Path of msedgedriver here')
url = "YOUTUBE URL HERE"
driver.get(url)

elem = driver.find_element_by_tag_name('html')
elem.send_keys(Keys.END)
time.sleep(3)
elem.send_keys(Keys.END)

innerHTML = driver.execute_script("return document.body.innerHTML")

page_soup = bs(innerHTML, 'html.parser')
res = page_soup.find_all('a',{'id':'video-title'})

titles = []
for video in res:
    print(video.get('title'))
    if video.get('title') != None:
        titles.append((video.get('title')))

file = open('YoutubeList.txt','w+', encoding="utf-8")
for title in titles:
    file.write(title+'\n')
    
file.close()

driver.close()
