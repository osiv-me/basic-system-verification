import pytest
from fixtures import db_clean, customers
from selenium import webdriver
import time
from customer_data import get_other_customer_webb, get_other_customer_db, isCustomerDisplayed, get_customers, get_full_customer


class TestNewCustomer:
    def dbClean(self, db_clean):
        print("reseting DB")

    def test_create_new_customers(self, db_clean, customers):
        driver = webdriver.Firefox()
        driver.get('http://127.0.0.1')
        time.sleep(1)  # yes this will slow the suite down.

        new_customer_btn = driver.find_element_by_tag_name('button')
        assert new_customer_btn is not None
        new_customer_btn.click()
        time.sleep(1)  # yes this will slow the suite down.

        # fill in the blanks
        new_customer = get_other_customer_webb()
        for key, value in new_customer.items():
            element = driver.find_element_by_id(key)
            element.clear()
            element.send_keys(value)
            time.sleep(0.1)  # yes this will slow the suite down.

        # click save
        save_btn = driver.find_element_by_id('save_customer_btn')
        save_btn.click()
        time.sleep(0.5)  # yes this will slow the suite down.

        # get the new customer from the DB
        all_customers = get_customers()
        print(all_customers)
        customer_from_db = all_customers.pop()
        other_customer = get_other_customer_db()

        # check that the customer is the same as the customer added.
        for key, value in other_customer.items():
            element = driver.find_element_by_id(key)
            element.clear()
            element.send_keys(value)
        assert other_customer == customer_from_db
        # yes this will slow the suite down.

        # click new customer
        created_customer = driver.find_element_by_id(customer_from_db['ID'])
        assert created_customer is not None
        assert created_customer.text == '{} {}'.format(
            new_customer['firstname'], new_customer['lastname'])
        created_customer.click()
        time.sleep(0.5)

        # check that each of the fields have been filled in correctly
        customerShownCorrect = isCustomerDisplayed(
            get_other_customer_db(), driver)
        driver.close()
        self.dbClean(self)
        assert customerShownCorrect == True
