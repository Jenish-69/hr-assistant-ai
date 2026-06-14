from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

urls = [
    "https://help.zoho.com/portal/en/kb/people/employee-handbook-5-0/leave/articles/leave",
    "https://help.zoho.com/portal/en/kb/people/employee-handbook-5-0/attendance/articles/attendance"
]

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

for url in urls:
    driver.get(url)
    time.sleep(5)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    text = soup.get_text(separator="\n", strip=True)

    print("--------------------------------")
    print("URL:", url)
    print("Text length:", len(text))
    print("Preview:")
    print(text[:1000])
    with open("website_context.txt", "a", encoding="utf-8") as file:
        file.write("\n\n")
        file.write("SOURCE: " + url)
        file.write("\n\n")
        file.write(text)

driver.quit()