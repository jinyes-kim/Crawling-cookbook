# naver store farm
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:/Chromedriver")
driver.get() #url address

res_list = [] # review bag

for a in range(2, 12): # 
    driver.find_element_by_xpath("").click()  # Xpath address
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    dummy = soup.select() # class tag
    dummy = list(dummy)
    for word in dummy:
        word = str(word)
        word = word.replace('', '')
        word = word.replace('\n', '')
        res_list.append(word)

