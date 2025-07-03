import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def startBot (username,password,url):
    # path to the chromedriver executable
    path = "C:\\Users\\Naveen\\Desktop\\chromedriver-win64\\chromedriver.exe"

    # create a service object
    service = Service(path)

    #Optional: Setup chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized") # start a maxmized window

    #initialize the chromedriver withe the service options
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("Opening the login page...")
    driver.get(url)

    print("filling the username...")
    driver.find_element(By.ID, "login_field").send_keys(username)

    print("filling the password...")
    driver.find_element(By.ID, "password").send_keys(password)

    print("Clicking the login button...")
    driver.find_element(By.NAME,"commit").click()

    print("Login process initiated...")
    time.sleep(5)

    driver.quit()

username = "naveen450"
password = "000000000"
url = "https://github.com/login"

startBot(username, password, url)