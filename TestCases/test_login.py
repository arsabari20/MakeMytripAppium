import time
import pytest
import allure
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from Utilities import Scroll_util


def test_login():
    desired_caps = {'platformName': 'Android', 'deviceName': 'Android', 'appPackage': 'com.makemytrip',
                    'appActivity': 'com.mmt.travel.app.home.ui.SplashActivity', 'noReset': True}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    print("opened the mmt app")
    driver.implicitly_wait(5)
    # driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='SKIP']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.ImageView[@content-desc='Hamburger']").click()
    log = driver.find_element(AppiumBy.XPATH,
                              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")
    print(log.text)
    log.click()
    # driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='LOGIN']").click()
    driver.implicitly_wait(5)
    choose = driver.find_element(AppiumBy.XPATH, "//android.widget.LinearLayout[@content-desc='Choose an Account']")
    choose.is_displayed()
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='NONE OF THE ABOVE']").click()
    driver.implicitly_wait(3)
    email = driver.find_element(AppiumBy.ID, "com.makemytrip:id/inputFieldChild")
    email.click()
    email.set_text("ssabari007@gmail.com")
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='CONTINUE']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Login via Password']").click()
    pwd = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter Password']")
    pwd.click()
    pwd.set_text("Sonar@2022")
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='SUBMIT']").click()



def test_booking():
    desired_caps = {'platformName': 'Android', 'deviceName': 'Android', 'appPackage': 'com.makemytrip',
                    'appActivity': 'com.mmt.travel.app.home.ui.SplashActivity', 'noReset': True}
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(4)
    driver.find_element(AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                        ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                        "/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android"
                                        ".widget.FrameLayout["
                                        "2]/android.view.ViewGroup/android.widget.RelativeLayout/android.widget"
                                        ".FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget"
                                        ".FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout["
                                        "3]").click()
    BookBusticket = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                    "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android" \
                    ".widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup" \
                    "/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[" \
                    "2]/android.view.ViewGroup/android.view.ViewGroup[" \
                    "1]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[" \
                    "2]/android.view.ViewGroup[2]/android.view.ViewGroup"
    driver.find_element(AppiumBy.XPATH, BookBusticket).click()
    time.sleep(2)
    boarding_point = driver.find_element(AppiumBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup")
    boarding_point.click()
    City1 = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter City Name']")
    City1.set_text("Chennai")
    koyambedu = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android" \
                ".widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget" \
                ".FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android" \
                ".view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[" \
                "2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[" \
                "2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[" \
                "2]/android.view.ViewGroup[1]"
    driver.find_element(AppiumBy.XPATH, koyambedu).click()
    drop_point = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android" \
                 ".widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget" \
                 ".FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view" \
                 ".ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[" \
                 "2]/android.view.ViewGroup/android.view.ViewGroup[" \
                 "1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[" \
                 "1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup"
    driver.find_element(AppiumBy.XPATH, drop_point).click()
    City2 = driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Enter City Name']")
    City2.set_text("Bangalore")
    EC = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup[1]"
    driver.find_element(AppiumBy.XPATH, EC).click()
    driver.find_element(AppiumBy.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[1]").click()
    driver.find_element(AppiumBy.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ScrollView/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[21]").click()
    driver.find_element(AppiumBy.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.ImageView").click()

    driver.find_element(AppiumBy.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sort & Filter']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Early Departure First']").click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='APPLY']").click()
    el = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("YBM   Travels").instance(0))')
    el.click()
    seat=driver.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[4]/android.view.ViewGroup/android.widget.ImageView")
    seat.click()
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='NEXT']").click()
    driver.implicitly_wait(5)
    Scroll_util.ScrollUtil.swipeUp(3,driver)
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='YBM TRAVELS, 32/1155, P H Road, Koyambedu, Chennai-107.Near Metro Railway Station']").click()
    driver.implicitly_wait(2)
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Electronic City.']").click()
    time.sleep(2)
    name = "Ananth"
    age = "27"
    Gender = "Male"
    email = "sam@gmail.com"
    Phone = "1112233333"
    wait = WebDriverWait(driver, 25, poll_frequency=1,
                         ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                             NoSuchElementException])

    nm = wait.until(lambda X: X.find_element(AppiumBy.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.EditText"))
    nm.set_text(name)
    age_d = driver.find_element(AppiumBy.XPATH,
                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.EditText")
    age_d.set_text(age)
    SX = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Male']")
    SX.click()
    #driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    #                    'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("Email address").instance(0))')
    Scroll_util.ScrollUtil.swipeUp(1,driver)
    mail= driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Email ID']")
    mail.set_text(email)
    time.sleep(2)
    mobile= driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[@text='Phone Number']")
    mobile.set_text(Phone)
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='NEXT']").click()
    wait.until(lambda X: X.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Select Payment Mode']"))
    details = driver.find_element(AppiumBy.ID,"com.makemytrip:id/tv_view_details")
    details.click()
    allure.attach(driver.get_screenshot_as_png(),name="SCR",attachment_type=AttachmentType.PNG)
    driver.back()
    driver.back()
    driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='GO BACK']").click()



