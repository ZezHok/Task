# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.chat import ChatHelper

class Aplication:
    def __init__(self):
        #self.wd = WebDriver('/Users/j.chistova/PycharmProjects/chromedriver')
        self.wd = WebDriver('C:\Users\Yulia\PycharmProjects\chromedriver')
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.chat = ChatHelper(self)

    def click_header(self):
        wd =self.wd
        wd.find_element_by_css_selector('[class="operators-header--user-info"]').click()

    def change_parameter_mode(self):
        wd = self.wd
        wd.find_element_by_xpath("//header/div[3]/p[3]").click()

    def change_status_online(self):
        wd = self.wd
        wd.find_element_by_css_selector('ng-click="operator.changeStatus(1)"').click()

    def change_status_offline(self):
        wd = self.wd
        wd.find_element_by_css_selector('ng-click="operator.changeStatus(3)"').click()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://redalert.staging.redmadrobot.com/")

    def destroy(self):
        self.wd.quit()