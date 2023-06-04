import os

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

import os

GOOGLE_CHROME_PATH = ''
CHROMEDRIVER_PATH = ''

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")

op.add_argument("--no-sandbox")
op.add_argument("--headless")
op.add_argument("--disable-dev-usage")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.binary_location = GOOGLE_CHROME_PATH
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

df = pd.DataFrame()
def steam_games(df,lis):
    try:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

        path = 'chromedriver.exe'

        url = 'https://www.reddit.com/search/?q=far%20cry%206%20review&type=link'
        driver = webdriver.Chrome(path)

        driver.get(url)

        scroll_pause_time = 3 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
        i = 1
        while True:
            # scroll one screen height each time
            driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
            i += 1
            time.sleep(scroll_pause_time)
            # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
            scroll_height = driver.execute_script("return document.body.scrollHeight;")
            # Break the loop when the height we need to scroll to is larger than the total scroll height
            if (screen_height) * i > scroll_height:
                break
            rev_title = driver.find_element_by_class_name('_1DK52RbaamLOWw5UPaht_S._3Ig_EsWWVLquWs2yBBQjec._1acwN_tUhJ8w-n7oCp-Aw3')
            rev_title.click()
            soup = BeautifulSoup(driver.page_source, "html.parser")
            review_title = soup.findAll('h3',class_='_eYtD2XCVieq6emjKBH3m')
            lis.append(review_title)

    except Exception as Argument:
        print(str(Argument))

def clickElements():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)

    path = 'chromedriver.exe'

    url = 'https://www.reddit.com/search/?q=far%20cry%206%20review&type=link'
    driver = webdriver.Chrome(path)

    driver.get(url)
    rev_title = driver.find_element_by_class_name('_1DK52RbaamLOWw5UPaht_S _3Ig_EsWWVLquWs2yBBQjec _1acwN_tUhJ8w-n7oCp-Aw3')
    rev_title.click()


lis = []
#steam_games(df,lis)
clickElements()

for i in lis:
    for j in i:
        print(j.span.text)

print(len(lis))
