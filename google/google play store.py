from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = ''
driver = webdriver.Chrome("C:/python_project/chromedriver.exe")
driver.get(url)

for a in range(1, 3):
    driver.find_element_by_xpath('xpath').click()  # Xpath address
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    dummy = soup.find('div', {'jsname': 'sngebd'}).text
    print(dummy)
    driver.get(url)
    
    
driver.quit()



    """
    using selenium

    #dummy = soup.select_one("c-wiz c-wiz:nth-child(3) div  div meta")
    #ddd = driver.find_element_by_css_selector("c-wiz c-wiz:nth-child(3) div  div meta").get_attribute("content")
    #print(ddd)
    """
