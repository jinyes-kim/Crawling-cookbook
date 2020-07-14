from bs4 import BeautifulSoup
from selenium import webdriver

# attach web driver
wd = webdriver.Chrome("C:/python_project/chromedriver.exe")

url = "https://sports.news.naver.com/index.nhn"
wd.get(url)

# get source
data_list = wd.find_elements_by_css_selector(".today_item")


#title
#information span:nth-of-type(1)
#information span:nth-of-type(2)
for a in data_list:
    try:
        item1 = a.find_element_by_css_selector(".text_area .title").text
        item2 = a.find_element_by_css_selector(".information span:nth-of-type(1)").text
        item3 = a.find_element_by_css_selector(".information span:nth-of-type(2)").text
    except:
        pass
    print(item1, end=' /')
    print(item2, end=' /')
    print(item3)

wd.quit()
