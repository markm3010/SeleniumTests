from selenium import webdriver
import time


class DriverClass:
    def __init__(self):
        PATH: str = "C:/Drivers/chromedriver_win32/chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def fill_in_data(self):
        self.driver.get('http://www.sandwiches.com/')

        # my name
        name = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/form/div[2]/table[1]/tbody/tr/td[2]/input')
        name.click()
        name.send_keys("Mark Johnson")

        # my email address
        time.sleep(1)
        my_mail = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/form/div[2]/table[2]/tbody/tr/td[2]/input')
        my_mail.click()
        my_mail.send_keys("MJ@somewhere.net")

        # my phone no.
        time.sleep(1)
        my_phone = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/form/div[2]/table[3]/tbody/tr/td[2]/input')
        my_phone.click()
        my_phone.send_keys("666-666-6969")

        # my offer for sandwiches.com
        time.sleep(1)
        my_offer = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/form/div[2]/table[5]/tbody/tr/td[2]/input')
        my_offer.click()
        time.sleep(1)
        my_offer.send_keys("30,000.99")

        # I really want to buy this domain name, for thirty grand, lol!
        time.sleep(1)
        my_comment = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/form/div[2]/table[6]/tbody/tr/td[2]/textarea')
        my_comment.click()
        time.sleep(1)
        my_comment.send_keys("I hope you take this offer, its the best you'll get from me! ;-)")

        send_offer = self.driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/form/div[4]/input')
        send_offer.click()


bot = DriverClass()
bot.fill_in_data()
