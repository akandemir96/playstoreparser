from selenium import webdriver
from bs4 import BeautifulSoup
import time


def web_parser(keyword):
    driver = webdriver.Firefox(executable_path = "")  #geckodriver local path
    driver.get("https://play.google.com/store/apps")
    driver.find_element_by_id("gbqfq").send_keys(keyword)
    driver.find_element_by_class_name("gbqfb").click()
    time.sleep(5)
    html = driver.page_source
    s = BeautifulSoup(html, "lxml")
    apps = s.find_all("a", class_="title")
    app_url="https://play.google.com/store/apps/details?"
    for app in apps:
        url=app_url+app["href"].split("?")[1]
        print (app.text)
        print (url)
    driver.quit()


def __main__():
    keyword = input("keyword: ")
    web_parser(keyword)


__main__()