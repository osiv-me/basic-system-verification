import pytest
import shutil
import requests
from selenium import webdriver
from environmentVariables import db_backup_path,db_path,URL,localhost_port

@pytest.fixture()
def db_clean():
    shutil.copy(db_backup_path,
                db_path)


@pytest.fixture()
def customers():
    result = requests.get(localhost_port + "customers")
    if result.status_code == 200:
        customers = result.json()
    else:
        raise Exception('error when fetching customers')

    return customers


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(URL)
    yield driver
    driver.close()
