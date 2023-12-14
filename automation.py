from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

PATH = ".\chromedriver.exe"
service = Service(executable_path=PATH)
options = webdriver.ChromeOptions()
options.add_argument('--window-size=1920x1080')
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://dmail.pythonanywhere.com")

if driver.title == "Home":
    driver.quit()

# Specify the correct username and password in the input file before running 
with open("input.txt") as f:
    un1 = f.readline().strip()
    pw1 = f.readline().strip()

search = driver.find_element(By.XPATH, "/html/body/form/div[1]/input")
search.clear()
search.send_keys(un1)
search = driver.find_element(By.XPATH, "/html/body/form/div[2]/input")
search.clear()
search.send_keys(pw1)
search.send_keys(Keys.RETURN)

mydmails = driver.find_element(By.LINK_TEXT, "My Dmails")
mydmails.click()

f = open("output.txt","w")

try:
    mails = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "card"))
    )
    mails = driver.find_elements(By.CLASS_NAME, "card")
    for mail in mails:
        header = mail.find_element(By.CLASS_NAME ,"card-header")
        f.write(header.text+"\n")
    driver.back()
    f.close()
    time.sleep(1)
    driver.quit()
except Exception as e:
    print(f"An exception occurred: {e}")
    driver.quit()