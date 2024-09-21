from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from config import get_paths


#all chrome stepup part done here 
def setup_driver():
    options = webdriver.ChromeOptions()
    service = Service(get_paths()[2])
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver
    