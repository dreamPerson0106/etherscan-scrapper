import undetected_chromedriver as uc
from selenium.webdriver import ChromeOptions, Chrome
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
try:
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument(
                            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    chrome_options.add_argument('--log-level=3')
    driver = Chrome(options=chrome_options)
    driver.get("https://etherscan.io")


    WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[title='Widget containing a Cloudflare security challenge']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "label.ctp-checkbox-label"))).click()
except Exception as error:
    print(error)



print(driver.page_source)
time.sleep(100)