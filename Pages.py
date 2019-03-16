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

            self.clickNextPage(driver)
            self.questionnairePage(driver)
            self.clickNextPage(driver)
            self.clickNextPage(driver)      ## Stage 2 page

            self.instructionPage(driver)  ## /**
            self.instructionPage(driver)
            self.instructionPage(driver)
            self.instructionPage(driver)  ## Instruction
            self.instructionPage(driver)
            self.instructionPage(driver)  ## Pages
            #self.instructionPage(driver)
            self.instructionPage(driver)  ## **/

            time.sleep(160)
            print("[+] Completed")

        except HTTPException:
            print('[-] Connection Error')
        finally:
            driver.close()


    def clickNextPage(self, driver):
        # Use for Instruction pages
        driver.find_element_by_xpath('//*[@id="form"]/div/button').click()

    def waitPage(self, driver):
        page = 'otree/WaitPage.html'
        while driver.title == page:
            time.sleep(5)

    def questionnairePage(self, driver):
        driver.find_element_by_xpath('//*[@id="id_gender_2"]').click()
        inputElement = driver.find_element_by_id('id_major')
        inputElement.send_keys('Robotiks')
        time.sleep(3)

    def preferences(self, driver):
        en = driver.find_element_by_xpath('//*[@id="mMyRange1"]')
        move = ActionChains(driver)
        move.click_and_hold(en).move_by_offset(0.5, 0).click()

    def matchOpponent(self, driver):
        en = driver.find_element_by_xpath('//*[@id="mMyRange1"]')
        move = ActionChains(driver)
        move.click_and_hold(en).move_by_offset(0.5, 0).click()

    def instructionPage(self, driver):
        driver.find_element_by_xpath('// *[ @ id = "form"] / div / button').click()
        time.sleep(1)

    def setUtilPage(self, driver):
        pass

    def personalPage(self, driver):
        ##driver.find_element_by_xpath
        time.sleep(5)
