from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

from processor import parser
from constant import URL

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)


def main():
    page = collected = 0
    while True:
        sleep(1)
        new_data = parser.parse_webpage(driver.page_source)
        print(new_data)
        page += 1
        collected += len(new_data)
        print(f'Page: {page} | Downloaded: {collected}')
        # driver.find_element(By.LINK_TEXT, "Next").click()
        driver.find_element(By.CLASS_NAME, "iIrPGlN8h2M_kZhJJZH_")


if __name__ == '__main__':
    main()
    driver.close()
