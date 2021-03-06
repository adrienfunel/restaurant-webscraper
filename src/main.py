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


def main():
    """Main entry point"""
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    sleep(2)
    # Scroll to the bottom to dynamically upload the full HTML source code
    smooth_scrolling(driver)

    page = collected = 0

    element = driver.find_element(by=By.XPATH, value="//div[contains(@data-test, 'restaurant-cards')]")
    # # // *[ @ id = "mainContent"] / div / div / div[2]
    element = element.get_attribute('outerHTML')

    max_page = parser.get_last_page(element)

    while page < max_page:
        new_data = parser.parse_webpage(element)
        if new_data.empty:
            break
        if page == 0:
            new_data.to_csv('output.csv', index=False)
        elif page > 0:
            new_data.to_csv('output.csv', index=False, header=None, mode='a')
        page += 1
        collected += len(new_data)
        print(f'Page: {page} | Downloaded: {collected}')

        try:
            wait = WebDriverWait(driver, 30)
            wait.until(EC.element_to_be_clickable((By.ID, "Go to the next page")))
            next_button = driver.find_element_by_id("Go to the next page")
            next_button.click()
        except TimeoutError:
            pass

    driver.close()


if __name__ == '__main__':
    main()
