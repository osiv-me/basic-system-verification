import pytest
from fixtures import db_clean, customers, driver
from selenium import webdriver
import time
from help_methods import *


class TestEditCustomerSuite:
    def test_click_new_customer(self, db_clean, customers, driver):
        time.sleep(0.5)
        driver.find_element_by_tag_name('button').click()
        displayed_values = get_gui_values(driver)
        empty_customer = get_new_customer_full_empty()
        assert displayed_values == empty_customer

    def test_new_customer_updated_in_db(self, db_clean, customers, driver):
        time.sleep(0.5)
        driver.find_element_by_tag_name('button').click()
        new_customer = get_new_customer()
        edit_customer(driver, new_customer)
        click_by_id(driver, 'save_customer_btn')

        latestCustomer = get_latest_customer()
        assert db_customer_to_customer_dict(latestCustomer) == new_customer

    def test_new_customer_shown(self, db_clean, customers, driver):
        time.sleep(0.5)
        driver.find_element_by_tag_name('button').click()
        new_customer = get_new_customer()
        edit_customer(driver, new_customer)
        click_by_id(driver, 'save_customer_btn')

        latestCustomer = get_latest_customer()
        click_by_id(driver, latestCustomer['ID'])
        displayed_values = get_gui_customer_values(driver)
        assert displayed_values == new_customer
