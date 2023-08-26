import requests
import bs4

headers = {
    "Accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "Referer":"https://etherscan.io/tx/0x670cbb199e371c220e1728b83f5526f54ef8b76d2d65cbc33158a9ed67be4b13",
    "Sec-Ch-Ua": '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    "Sec-Ch-Ua-Mobile":"?0",
    "Sec-Ch-Ua-Platform":"Windows",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
}

response = requests.get("https://etherscan.io/tx/0x3b7f8bff36d84a932f4c48bed8e55b8a03733ef40f98dfc79efe2dd879fd35bb", headers = headers)
soup = bs4.BeautifulSoup(response.content, 'html.parser')
print(soup)

text = soup.select_one("div#ContentPlaceHolder1_divTimeStamp span[data-bs-toggle='tooltip']")
print(text.text)


