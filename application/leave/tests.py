# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from selenium.webdriver.common.action_chains import ActionChains
from django.test.client import Client
from selenium import webdriver
from django.core.urlresolvers import reverse
import time
from datetime import datetime

from django.contrib.auth.models import User
from leave.models import employee


class LeaveApplication(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/home/popoola/Documents/tangent/solution/tangent_leave_app_solution/leave/chromedriver")
        

        
        
    def tearDown(self):
        self.browser.quit()

    def test_1_valid_leave_application(self):
        self.browser.get('http://localhost:8010/leave/apply')
        #self.assertIn('Login', self.browser.title)
        
        time.sleep(3)
        username = self.browser.find_element_by_id("id_username")
        username.send_keys('kate')

        password = self.browser.find_element_by_id("id_password")
        password.send_keys('kate')

        self.browser.find_element_by_id("login").submit()

        start_date = self.browser.find_element_by_id("start_date")
        time.sleep(3)
        ActionChains(self.browser).move_to_element(start_date).click().send_keys('03/06/2017').perform()

        
        end_date = self.browser.find_element_by_id("end_date")
        time.sleep(3)
        ActionChains(self.browser).move_to_element(end_date).click().send_keys('08/06/2017').perform()

        self.browser.find_element_by_id("submit").submit()
        
        time.sleep(20)
        self.assertIn('Leave Application', self.browser.title)

    def test_2_new_employee_leave_application(self):
        self.browser.get('http://localhost:8010/leave/apply')
        
        time.sleep(3)
        username = self.browser.find_element_by_id("id_username")
        username.send_keys('ben')

        password = self.browser.find_element_by_id("id_password")
        password.send_keys('ben')

        self.browser.find_element_by_id("login").submit()

        start_date = self.browser.find_element_by_id("start_date")
        time.sleep(3)
        ActionChains(self.browser).move_to_element(start_date).click().send_keys('01/06/2017').perform()

        
        end_date = self.browser.find_element_by_id("end_date")
        time.sleep(3)
        ActionChains(self.browser).move_to_element(end_date).click().send_keys('05/06/2017').perform()

        self.browser.find_element_by_id("submit").submit()
        

        self.assertIn('You cannot apply for leave as you just got employed less than 3 months ago.', self.browser.page_source)

  
    def test_3_Leave_greater_than_18_days(self):
        self.browser.get('http://localhost:8010/leave/apply')
        
        time.sleep(3)
        username = self.browser.find_element_by_id("id_username")
        username.send_keys('kate')

        password = self.browser.find_element_by_id("id_password")
        password.send_keys('kate')

        self.browser.find_element_by_id("login").submit()

        start_date = self.browser.find_element_by_id("start_date")
        time.sleep(3)
        ActionChains(self.browser).move_to_element(start_date).click().send_keys('01/07/2017').perform()

        
        end_date = self.browser.find_element_by_id("end_date")
        time.sleep(3)
        ActionChains(self.browser).move_to_element(end_date).click().send_keys('30/07/2017').perform()

        self.browser.find_element_by_id("submit").submit()
        

        self.assertIn('kindly select a shorter period', self.browser.page_source)

    def test_4_start_date_already_passed(self):
        self.browser.get('http://localhost:8010/leave/apply')
        
        time.sleep(3)
        username = self.browser.find_element_by_id("id_username")
        username.send_keys('kate')

        password = self.browser.find_element_by_id("id_password")
        password.send_keys('kate')

        self.browser.find_element_by_id("login").submit()

        start_date = self.browser.find_element_by_id("start_date")
        time.sleep(3)
        ActionChains(self.browser).move_to_element(start_date).click().send_keys('29/05/2017').perform()

        
        end_date = self.browser.find_element_by_id("end_date")
        time.sleep(3)
        ActionChains(self.browser).move_to_element(end_date).click().send_keys('10/06/2017').perform()

        self.browser.find_element_by_id("submit").submit()
        

        self.assertIn('This date has passed', self.browser.page_source)




        
        


    

