from selenium import webdriver
import time
from bs4 import BeautifulSoup
import pandas as pd
def getTags(link):
    driver = webdriver.Firefox()

    videos=[]

    driver.get(link)

    time.sleep(3)
    element=driver.find_element_by_class_name("section--lecture--36j0E")
    element.click()
    time.sleep(3)
    content = driver.page_source
    soup = BeautifulSoup(content, features="lxml")

    #driver.switch_to.window(driver.window_handles[0])
    #for button in driver.find_elements_by_class_name("udlite-custom-focus-visible course-preview--preview-row--O5SIC"):
        #button.click()
    for a in soup.findAll("video"):#, {"class":"udlite-custom-focus-visible course-preview--preview-row--O5SIC"}):

        if (a.find("src=\"")!=-1):
            videos.append(str(a))

    driver.quit()

    return videos

def getLinks(videos):
    links =[]
    for text in videos:
        right = text.split("src=\"")[1]
        answer = right.split("\"")
        #link[].split("\"")
            #print(right)
        links.append(answer[0])
    return links
if __name__ == "__main__":
    link = "https://www.udemy.com/course/flutter-mobile-development/"
    videos = getTags(link)
    link = getLinks(videos)
    print  (link)