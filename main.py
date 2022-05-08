#pip install webdriver-setup
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
PASSWORD="nG62V!gPu3dTx!M"
PHONE = "7792012033"
EMAIL = "erkan0901@gmail.com"

chrome_servie = fs.Service(executable_path="C:/Development/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_servie)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
signin = driver.find_element(By.CLASS_NAME, "login__form_action_container")
signin.click()

#clicking on links
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3033402885&f_LF=f_AL&geoId=100345145&keywords=junior%20python%20developer&location=West%20Midlands%2C%20England%2C%20United%20Kingdom")
time.sleep(3)
email = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
email.click()

phone_no = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone_no.text == "":
    phone_no.send_keys(PHONE)

submit = driver.find_element(By.CSS_SELECTOR, "footer button")
submit.click()