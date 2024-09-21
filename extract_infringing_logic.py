import time, requests, logging
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
import time
from bs4 import BeautifulSoup

def get_infringing_links(driver, query, num_pages=3):
    domain_list = []
    try:
        driver.get('https://www.google.com')
        search_box = driver.find_element(By.NAME, 'q')
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        for _ in range(num_pages):
            time.sleep(2)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
               
            for link in soup.find_all('a', attrs={'jsname': True}, href=True):
                url = link.get('href')
                print(url)
                if url.startswith('https://') or url.startswith('http://'):
                    parsed_url = urlparse(url)
                    base_url = parsed_url.netloc
                    domain_list.append(base_url)
                    print(domain_list)

            try:
                next_button = driver.find_element(By.XPATH, '//a[@id="pnnext"]')
                next_button.click()
                time.sleep(3)
            except Exception as e:
                logging.warning(f"Next button not found or error: {e}")
                break
    except Exception as e:
        print(e)
        logging.error(f"Error during web scraping: {e}")
    finally:
        driver.quit()
    
    return domain_list