from selenium import webdriver
import time
driver=webdriver.Chrome(r"C:\Users\Sowjanya N-3147\Downloads\chromedriver_win32 (1)\chromedriver")
driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(5)
driver.maximize_window()