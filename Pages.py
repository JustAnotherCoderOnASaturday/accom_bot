from selenium import webdriver
from selenium.webdriver.support.ui import Select
from http.client import HTTPException
from selenium.webdriver import ActionChains
import time
class accom_pages:
    def __init__(self, url):
        self.url = url

    def getSite(self):
        try:
            driver = webdriver.Chrome()
            driver.get(self.url)

            self.nextPage(driver)
            self.nextPage(driver)

            #en = driver.find_element_by_id('mMyRange1')
            en = driver.find_element_by_xpath('//*[@id="mMyRange1"]')
            move = ActionChains(driver)
            move.click_and_hold(en).move_by_offset(0.5, 0).click()

            #move.click_and_hold(en).move_by_offset(0.5, 0).release().perform()
            time.sleep(5)
            move.click_and_hold(en).move_by_offset(0, -0.5).release().perform()
            time.sleep(5)
            ##self.nextPage(driver)

        except HTTPException:
            print('[-] Connection Error')
        finally:
            #driver.close()
            pass

    def nextPage(self, driver):
        # Use for Instruction pages
        driver.find_element_by_xpath('//*[@id="form"]/div/button').click()

    def preferences(self, driver):
        en = driver.find_element_by_xpath('//*[@id="mMyRange1"]')
        move = ActionChains(driver)
        move.click_and_hold(en).move_by_offset(0.5, 0).click()

