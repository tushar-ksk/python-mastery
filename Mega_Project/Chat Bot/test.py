from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_argument("--user-data-dir=C:/selenium/whatsapp-profile")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--no-first-run")
options.add_argument("--no-default-browser-check")
options.add_argument("--remote-debugging-port=9223")

driver = webdriver.Chrome(options=options)

time.sleep(2)
driver.get("https://web.whatsapp.com/")
