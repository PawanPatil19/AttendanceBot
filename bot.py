from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time



def activity():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)

    driver.get("https://eduserver.nitc.ac.in/login/index.php")
    #print(driver.title)  # prints the title of the tab in the browser



    search_username = driver.find_element_by_name("username")
    search_username.send_keys("*******") # As per requirement

    search_password = driver.find_element_by_name("password")
    search_password.send_keys("********")# As per requirement
    search_password.send_keys(Keys.RETURN)



    link2 = driver.find_element_by_link_text("m2020cy1001dj")
    link2.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Attendance"))
        )
        element.click()

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Submit Attendance"))
        )
        element.click()

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "Present"))
        )
        element.click()

        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "Present"))
        )
        element.click()


    except:
        driver.quit()



schedule.every().monday.at("12:45").do(activity)
schedule.every().tuesday.at("09:30").do(activity)
schedule.every().thurday.at("10:30").do(activity)
schedule.every().friday.at("15:30").do(activity)
while True:
    schedule.run_pending()
    time.sleep(1)


