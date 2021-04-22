import pytest
from fixtures import db_clean, customers
from selenium import webdriver
import time
from customer_data import get_other_customer_webb, get_other_customer_db, assertCustomerShown
# should test diffrent browsers :(


class TestEditCustomer:
    def dbClean(self, db_clean):
        print("reset DB")

    def test_edit_customer(self, db_clean, customers):
        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1')
        time.sleep(1)  # yes this will slow the suite down.
        first_customer = driver.find_element_by_id(customers[0]['ID'])

        assert first_customer is not None
        assert first_customer.text == '{} {}'.format(
            customers[0]['Firstname'], customers[0]['Lastname'])
        first_customer.click()
        time.sleep(1)  # yes this will slow the suite down.
        edit_btn = driver.find_element_by_id('edit_customer_btn')
        edit_btn.click()
        time.sleep(1)  # yes this will slow the suite down.

        # edit all the fields
        new_customer = get_other_customer_webb()
        for key, value in new_customer.items():
            element = driver.find_element_by_id(key)
            element.clear()
            element.send_keys(value)
            time.sleep(0.1)  # yes this will slow the suite down.
        save_btn = driver.find_element_by_id('save_customer_btn')
        save_btn.click()
        time.sleep(0.5)  # yes this will slow the suite down.
        edited_customer = driver.find_element_by_id(customers[0]['ID'])

        assert edited_customer is not None
        assert edited_customer.text == '{} {}'.format(
            new_customer['firstname'], new_customer['lastname'])
        edited_customer.click()
        time.sleep(1)

        # validate data is correctly displayed, compare saved values to what we send in:
        customerShownCorrect = assertCustomerShown(
            get_other_customer_db(), driver)
        driver.close()
        self.dbClean(self)
        assert customerShownCorrect == True
