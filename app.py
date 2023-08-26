from flask import Flask, make_response, jsonify
from undetected_chromedriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
import time

app = Flask(__name__)

driver = None
options = ChromeOptions()
options.add_argument("--headless")
driver = Chrome(options=options)
def interceptor(request):
    request.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    request.headers['Cookie'] = '_ga=GA1.1.1422679124.1689979108; etherscan_cookieconsent=True; ASP.NET_SessionId=mw4gm0cu3qe3e4byj3ddqlpv; __cflb=0H28vPcoRrcznZcNZSuFrvaNdHwh857mdFQeeFybDTa; cf_clearance=6Lz94hEhOqTKxgOr8y28Gvhb7vCaupsn_IbIR9SquQs-1693022025-0-1-ba6f4700.1bb4a04c.4478fa33-0.2.1693022025; _ga_T1JC9RNQXV=GS1.1.1693030896.5.1.1693033089.0.0.0'


@app.route('/<hash>')
def get_info(hash):
    print(hash)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(f'https://etherscan.io/tx/{hash}')
    print(driver)
    try: 
        driver.find_element(By.CSS_SELECTOR, '#ContentPlaceHolder1_maintable .card:first-child #ContentPlaceHolder1_divTimeStamp span[data-bs-toggle]')
        driver.close()
        return jsonify({"status": True})
    except:
        driver.close()
        return jsonify({"status": False})