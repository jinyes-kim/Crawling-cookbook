from bs4 import BeautifulSoup
from selenium import webdriver

wd = webdriver.Chrome("C:/python_project/chromedriver.exe")

for a in range(0, 5):
    url = "https://section.blog.naver.com/BlogHome.nhn?directoryNo=&currentPage=" + str(a) + "&groupId=0"
    wd.get(url)
    #html = wd.page_source
    #soup = BeautifulSoup(html, "html.parser")
    data_list = wd.find_elements_by_css_selector("div .info_post")

    #name_author
    #text
    #title_post
    #.reply em

    for a in data_list:
        try:
            item1 = a.find_element_by_css_selector(".name_author").text
            item2 = a.find_element_by_css_selector(".title_post").text
            try:
                item3 = a.find_element_by_css_selector(".reply em").text
            except:
                item3 = '0'
        except:
            pass
        print(item1, end='')
        print(item2, end='')
        print(item3)

wd.quit()
