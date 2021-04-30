import pytest
from fixtures import db_clean, customers, driver
from selenium import webdriver
import time
from help_methods import *
from environmentVariables import sleep_time


class TestEditCustomerSuite:
    def test_click_customer(self, db_clean, customers, driver):
        time.sleep(sleep_time)
        first_customer = driver.find_element_by_id(customers[0]['ID'])
        assert first_customer is not None
        assert first_customer.text == '{} {}'.format(
            customers[0]['Firstname'], customers[0]['Lastname'])

    def test_customer_displayed(self, db_clean, customers, driver):
        time.sleep(sleep_time)
        click_by_id(driver, customers[0]['ID'])
        displayed_values = get_gui_values(driver)
        customer_values = db_customer_to_full_dict(
            get_full_customer(customers[0]['ID']))
        assert displayed_values == customer_values

    def test_edit_customer_updated_in_db(self, db_clean, customers, driver):
        time.sleep(sleep_time)
        click_by_id(driver, customers[0]['ID'])
        click_by_id(driver, 'edit_customer_btn')
        # edit all the values.
        newCustomer = get_new_customer()
        edit_customer(driver, newCustomer)
        # click save
        click_by_id(driver, 'save_customer_btn')
        time.sleep(sleep_time)

        # verify the customer list has been updated
        latestCustomer = get_latest_customer()
        assert db_customer_to_customer_dict(latestCustomer) == newCustomer
        click_by_id(driver, latestCustomer['ID'])

    def test_edit_customer_shown(self, db_clean, customers, driver):
        time.sleep(sleep_time)
        click_by_id(driver, customers[0]['ID'])
        click_by_id(driver, 'edit_customer_btn')
        # edit all the values.
        newCustomer = get_new_customer()
        edit_customer(driver, newCustomer)
        # click save
        click_by_id(driver, 'save_customer_btn')
        time.sleep(sleep_time)
        # verify the customer list has been updated
        latestCustomer = get_latest_customer()
        click_by_id(driver, latestCustomer['ID'])
        # verify customer displayed correctly
        displayed_values = get_gui_customer_values(driver)
        assert displayed_values == newCustomer

    def test_edit_device(self, db_clean, customers, driver):
        time.sleep(sleep_time)
        click_by_id(driver, customers[0]['ID'])
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[4]/button').click()

        newDevice = get_new_device()
        edit_device(driver, newDevice)

        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[4]/button[3]').click()
        displayed_values = get_gui_device_values(driver)
        assert displayed_values == newDevice
