import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Confidential_Data.InputData import ConfidentialData


class Surya:
    url = "https://www.instagram.com"

    driver = webdriver.Firefox()

    def insta_login(self):
        #login using facebook credentials
        user_name = ConfidentialData().username
        pass_word = ConfidentialData().password
        self.driver.get(self.url)
        time.sleep(4)
        #clicking 'log in with facebook' button
        facebook_button_xpath = '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div[1]/div[5]/button'
        facebook_click = self.driver.find_element(by=By.XPATH, value=facebook_button_xpath)
        time.sleep(5)
        facebook_click.click()

        #entering the credentials and logging in
        email_id_xpath = '//*[@id="email"]'
        password_xpath = '//*[@id="pass"]'
        Log_button_xpath = '//*[@id="loginbutton"]'
        username1 = self.driver.find_element(by=By.XPATH, value= email_id_xpath)
        password1 = self.driver.find_element(by=By.XPATH, value=password_xpath)
        Logbutton = self.driver.find_element(by=By.XPATH, value=Log_button_xpath)
        username1.send_keys(user_name)
        password1.send_keys(pass_word)
        time.sleep(2)
        Logbutton.click()
        time.sleep(10)

        #getting otp realtime
        otp_field_xpath= '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[1]/div/label/input'
        confirm_xpath = '//*[@id="react-root"]/section/main/div/div/div[1]/div[2]/form/div[2]/button'

        otp = input("Enter the otp ")
        otp_field = self.driver.find_element(by=By.XPATH, value=otp_field_xpath)
        confirm = self.driver.find_element(by=By.XPATH, value=confirm_xpath)
        otp_field.send_keys(otp)
        confirm.click()
        time.sleep(10)

        #clicking the Not now button
        Not_now_xpath = '//*[@id="mount_0_0_+/"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]'
        Not_now = self.driver.find_element(by=By.XPATH, value=Not_now_xpath)
        Not_now.click()

    def Search_user(self):
        # click on the search icon
        Search_icon="//div[text()='Search'][@class='_aacl _aacp _aacu _aacx _aada']"
        self.driver.find_element(by=By.XPATH, value=Search_icon).click()
        Search_textbox = "//input[@placeholder='Search']"
        self.driver.find_element(by=By.XPATH, value=Search_textbox).send_keys()







