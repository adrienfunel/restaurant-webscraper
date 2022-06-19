from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from time import sleep

from processor import parser
from processor.helper import smooth_scrolling
from constant import URL

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(URL)
sleep(2)
# Scroll to the bottom to dynamically upload the full HTML source code
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
smooth_scrolling(driver)
# sleep(3)


def main():
    """Main entry point"""
    page = collected = 0
    while True:
        sleep(1)
        # new_data = parser.parse_webpage(driver.page_source)
        # new_data = parser.parse_webpage(driver.execute_script("return document.body.outerHTML;"))

        element = driver.find_element(by=By.XPATH, value="//div[contains(@data-test, 'restaurant-cards')]")
        # // *[ @ id = "mainContent"] / div / div / div[2]
        element = element.get_attribute('outerHTML')
        new_data = parser.parse_webpage(element)
        page += 1
        collected += len(new_data)
        print(f'Page: {page} | Downloaded: {collected}')

        # next_button = driver.find_element(By.CLASS_NAME, "pBCjKaMJcpEY4UICo9ol shGmbXyM42Fia5DVEBAG")
        # next_button = driver.find_element_by_xpath('/html/body/div[1]/div/div/main/div/div/div[3]/div[2]/a')
        # wait = WebDriverWait(driver, 30)
        # wait.until(EC.element_to_be_clickable((By.ID, "Go to the next page")))
        # next_button = driver.find_element_by_id("Go to the next page")

        # next_button.click()


if __name__ == '__main__':
    main()
    driver.close()
