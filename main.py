import time, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from dotenv import load_dotenv

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/app/recs")

time.sleep(3)
log_in_button = driver.find_element(By.LINK_TEXT, value="Log in")
log_in_button.click()

time.sleep(3)
google_log_in_button = driver.find_element(By.ID, value="c-133197680")
google_log_in_button.click()

driver.switch_to.window(driver.window_handles[1])

email_input = driver.find_element(By.ID, value="identifierId")
email_input.send_keys(os.environ.get("USERNAME"), Keys.ENTER)

time.sleep(3)
password_input = driver.find_element(By.NAME, value="Passwd")
password_input.send_keys(os.environ.get("PASSWORD"), Keys.ENTER)

driver.switch_to.window(driver.window_handles[0])

time.sleep(10)
allow_location = driver.find_element(By.XPATH, value='//*[@id="c1351554381"]/div/div[1]/div/div/div[3]/button[1]')
allow_location.click()

time.sleep(5)
dismiss_notifications = driver.find_element(By.XPATH, value='//*[@id="c1351554381"]/div/div[1]/div/div/div[3]/button[2]')
dismiss_notifications.click()

accept_cookies = driver.find_element(By.XPATH, value='//*[@id="c-1215031839"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_cookies.click()

time.sleep(10)
for n in range(100):
    time.sleep(2)
    try:
        print("called like button #1")
        like = driver.find_element(By.XPATH, value='//*[@id="c-1215031839"]/div/div[1]/div/div/div/main/div/div/div/div/div[4]/div/div[4]/button')
        like.click()
        print("liked")

    except ElementClickInterceptedException:
        try:
            print("closing match popup")
            match_popup = driver.find_element(By.XPATH, value='//*[@id="q919367361"]/div/div/div[1]/div/div[3]/button/svg/g/path')
            match_popup.click()

        except NoSuchElementException:
            print("closing add homescreen popup")
            add_homescreen_popup = driver.find_element(By.XPATH, value='//*[@id="c1351554381"]/div/div/div[2]/button[2]')
            add_homescreen_popup.click()

    except NoSuchElementException:
        try:
            print("called like button #2+")
            like = driver.find_element(By.XPATH, value='//*[@id="c-1215031839"]/div/div[1]/div/div/div/main/div/div/div/div/div[5]/div/div[4]/button')
            like.click()
            print("liked")

        except ElementClickInterceptedException:
            try:
                print("closing match popup")
                match_popup = driver.find_element(By.XPATH, value='//*[@id="q919367361"]/div/div/div[1]/div/div[3]/button/svg/g/path')
                match_popup.click()

            except NoSuchElementException:
                print("closing add homescreen popup")
                add_homescreen_popup = driver.find_element(By.XPATH, value='//*[@id="c1351554381"]/div/div/div[2]/button[2]')
                add_homescreen_popup.click()

        except NoSuchElementException:
            print("loading like button")
            time.sleep(2)

print("Your 100 swaps are over!")
driver.quit()