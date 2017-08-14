from selenium import webdriver

browser = webdriver.Firefox() # need to download webdriver (http://docs.seleniumhq.org/download/)
browser.get('http://localhost:8000')

assert 'Django' in browser.title