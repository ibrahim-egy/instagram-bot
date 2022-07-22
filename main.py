from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep

SIMILAR_ACCOUNT = "cr7cristianoronaldo"
USERNAME = "pythontest1164@gmail.com"
PASSWORD = "shortroad0#"

chrome_driver_path = "C:\Development\chromedriver.exe"
ser = Service(chrome_driver_path)


class InstagramBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=ser)
        self.driver.get("https://www.instagram.com/")
        self.SCROLL_PAUSE_TIME = 0.5

    def login(self):
        sleep(2)
        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(5)
        search = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SIMILAR_ACCOUNT)
        sleep(1)
        search.send_keys(Keys.ENTER)
        search.send_keys(Keys.ENTER)
        sleep(5)
        followers = self.driver.find_element(By.CSS_SELECTOR, ".Y8-fY a div")
        followers.click()
        sleep(5)
        for _ in range(10):
            scr1 = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)

    def follow(self):
        sleep(2)
        follow_buttons = self.driver.find_elements(By.CLASS_NAME, "sqdOP")
        for button in follow_buttons:
            sleep(1)
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel.click()
                continue


bot = InstagramBot()
bot.login()
bot.find_followers()
bot.follow()
