import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions, Chrome
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
try:
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument(
                            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36")
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_experimental_option(
        "useAutomationExtension", False)
    chrome_options.add_experimental_option(
        "excludeSwitches", ["enable-automation"])
    driver = Chrome( options=chrome_options)
    driver.implicitly_wait(3)
    driver.get("https://etherscan.io/tx/0x3b7f8bff36d84a932f4c48bed8e55b8a03733ef40f98dfc79efe2dd879fd35bb")

except Exception as error:
    print(error)

print(driver.find_element(By.CSS_SELECTOR, "div#ContentPlaceHolder1_divTimeStamp").text)

# print(driver.page_source)
