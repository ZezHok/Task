# -*- coding: utf-8 -*-
import pytest
from selenium.webdriver.common.keys import Keys
from fixture.application import Aplication
from fixture.chat import ChatHelper
import time

def test_change_mode(app):
    # 1) Смена режима администратора(admin mode и operator mode)
    app.open_home_page()
    app.session.login(email="a@redmadrobot.com", password="swordfish42_is_bad_password_you_know!!!")
    app.click_header()
    app.change_parameter_mode()
    app.click_header()
    # assert

def test_change_status(app):
    # 4) Смена оператором статуса: Свободен > Занят
    app.open_home_page()
    app.session.login(email="a@redmadrobot.com", password="swordfish42_is_bad_password_you_know!!!")
    app.click_header()
    app.change_parameter_mode()
    app.click_header()
    app.change_status_online()
    # assert
    app.click_header()
    app.change_status_offline()
    # assert

def test_edit_message(app):
    #3) Редактирование оператором последнего сообщения.
    app.open_home_page()
    app.session.login(email="viktoriya.kan@open.ru", password="swordfish42_is_bad_password_you_know!") # operator
    app.chat.click_edit_mes()
   # app.wd.find_element_by_css_selector('[type="text"]').send_keys(Keys.UP)



   # 2) Создание нового тикета, отправка сообщений от пользователя оператору и обратно.
   # 5) Просмотр администратором всех сообщений выбранного пользователя.
   # 6) Переадресация тикета администратором.