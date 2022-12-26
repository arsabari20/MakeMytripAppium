from appium.webdriver.common.appiumby import AppiumBy
import logging
from Utilities.LogUtil import Logger
from Utilities.configReader import readConfig

log = Logger(__name__, logging.INFO)


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def Click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, readConfig("locators", locator)).click()
        log.logger.info("Clicking on Element"+str(locator))

    def Type(self, locator, value):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, readConfig("locators", locator)).send_keys(value)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, readConfig("locators", locator)).send_keys(value)
        log.logger.info("Typing in an Element"+str(locator), "entered the value as :", value)

    def GetText(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(AppiumBy.XPATH, readConfig("locators", locator)).text()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(AppiumBy.ID, readConfig("locators", locator)).text()
        log.logger.info("The text is:"+str(locator))
