# this BOT uses GOOGLE PROFILE to sub to channel 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time




def ChannelToSub():
    channel_links = []
    chnl_links = input("ENTER YOUR CHANNEL LINKS :")
    channel_links = chnl_links.split(",")
    print(channel_links)
    return channel_links

def Subscribe(channel_links):
        for link in channel_links:
            driver.get(link)
            time.sleep(10) 
            sub_button_element = driver.find_element(By.XPATH, "//button[@class='yt-spec-button-shape-next yt-spec-button-shape-next--filled yt-spec-button-shape-next--mono yt-spec-button-shape-next--size-m']")
            sub_button_element.click()
            print(f"Subscribed to channel: {link}")
                          


chrome_profile_path = 'C:/Users/GC/AppData/Local/Google/Chrome/User Data' #change this path to match your profile
chrome_options = Options()
chrome_options.add_argument(f'--user-data-dir={chrome_profile_path}')
driver = webdriver.Chrome(options=chrome_options)


links = ChannelToSub()
Subscribe(links)

