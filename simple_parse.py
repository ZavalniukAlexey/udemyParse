from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd

link = "https://www.udemy.com/course/flutter-mobile-development/"

driver = webdriver.Firefox()

free_videos=[]
locked_videos=[]
driver.get(link)

#time.sleep(3)
#element=driver.find_element_by_class_name("section--lecture--36j0E")
#element.click()
#time.sleep(3)
content = driver.page_source
soup = BeautifulSoup(content, features="lxml")


for element in soup.findAll("span", attrs = {"class":"section--previewable-lecture-title--cRADT"}):
    a = str(element)
    free_videos.append(a.split("\">")[1].split("</")[0])
    #answer = right.split[0]
    #answer)

for element in soup.findAll("ul", attrs = {"class":"section--lecture-title-and-description--3lul"}):
    a = str(element)
    print(a)
    right = a.split("<span class=\"\">")[1]
    answer = right.split("</")[0]
    locked_videos.append(answer)

print(free_videos)
print(locked_videos)
driver.quit()