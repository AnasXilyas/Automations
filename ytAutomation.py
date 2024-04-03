import json
from selenium import webdriver
from selenium.webdriver.common.by import By
list = []

driver = webdriver.Edge()

driver.get('https://www.youtube.com/playlist?list=PLmUgeKw7vSS4bnLJbdKNKIbx1PpAMaEa6')

amv_element = driver.find_elements(By.ID,"video-title")

for element in amv_element:
   
    video_name = element.text

    print("VIDEO TITLE: ", video_name)
    video = {"Video Name:": video_name}
    list.append(video)
    
file = open("Yt Title Scrapper.json", 'a')
file.write(json.dumps(list))
file.close()

