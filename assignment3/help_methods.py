import requests
from fixtures import customers


def get_full_customer(id):
    # this is what prints the a in the firstname
    result = requests.get('http://127.0.0.1:6399/' +
                          'full_customer/%d' % (id))
    if result.status_code == 200:
        customer = result.json()
    else:
        raise Exception('error when fetching customers')
    # fixing the bug for this test suite.
    customer['Firstname'] = customer['Firstname'][:-1]
    return customer


def get_latest_customer():
    result = requests.get('http://127.0.0.1:6399/' + "customers")
    if result.status_code == 200:
        customers = result.json()
    else:
        raise Exception('error when fetching customers')
    return customers.pop()


def click_by_id(driver, id):
    try:
        driver.find_element_by_id(id).click()
        return True
    except:
        print('invalid id or could not click id')
    return False


def get_gui_customer_ids():
    return {
        'Firstname': 'firstname',
        'Lastname': 'lastname',
        'Age': 'age',
        'Sex': 'gender',
        'Street': 'street',
        'Zip': 'zipcode',
        'City': 'city',
        'Nationality': 'nationality',
        'Email': 'email',
    }


def get_gui_device_ids():
    return {
        "MSISDN": 'phone',
        "IMSI": 'imsi',
    }


def get_gui_ids():
    customer = get_gui_customer_ids()
    device = get_gui_device_ids()
    customer.update(device)
    return customer


def get_new_customer():
    return {
        'Firstname': "Emil",
        'Lastname': "Erlandsson",
        'Age': "69",
        'Sex': "Male",
        'Street': "Streety McStreet Street",
        'Zip':  "37141",
        'City': "Karlskrona",
        'Nationality': "Sweden",
        'Email': "emil.erlandsson@gmail.com",
    }


def get_new_device():
    return {
        "IMEI": "IMEI_9876543210",
        "ImageURL": "/products/images/452.jpeg",
        "Model": "Google Pixel 2 XL",
        "Type": "Phone",
        "IMSI": "IMSI_9876543210",
        "MSISDN": "+46701234567"
    }


def get_new_customer_full():
    customer = get_new_customer()
    device = get_new_device()
    customer.update(device)
    return customer


def get_new_customer_full_empty():
    customer = get_new_customer_full()
    for key, value in customer.items():
        customer[key] = ''
    return customer


def get_gui_customer_values(driver):
    gui_id = get_gui_customer_ids()
    values = {}
    for key, value in gui_id.items():
        try:
            values[key] = driver.find_element_by_id(
                value).get_attribute('value')
        except:
            print("error when adding gui values to dictionary")
    return values


def get_gui_device_values(driver):
    gui_id = get_gui_device_ids()
    values = {}
    for key, value in gui_id.items():
        try:
            values[key] = driver.find_element_by_id(
                value).get_attribute('value')
        except:
            print("error when adding gui values to dictionary")
    try:
        values['IMEI'] = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[4]/table/tbody/tr[5]/td[2]').get_attribute('innerHTML')
    except:
        values['IMEI'] = ''
        print('could not find element IMEI')
    try:
        # here we have to remove the host address.done by using [a:b]
        values['ImageURL'] = driver.find_element_by_tag_name(
            'img').get_attribute('src')[21:]
    except:
        values['ImageURL'] = ''
        print('could not find element ImageURL')
    try:
        values['Model'] = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[4]/table/tbody/tr[3]/td[2]').get_attribute('innerHTML')
    except:
        values['Model'] = ''
        print('could not find element Model')
    try:
        values['Type'] = driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[4]/table/tbody/tr[4]/td[2]').get_attribute('innerHTML')
    except:
        values['Type'] = ''
        print('could not find element Type')
    return values


def get_gui_values(driver):
    customer = get_gui_customer_values(driver)
    device = get_gui_device_values(driver)
    customer.update(device)
    return customer


def db_customer_to_customer_dict(customer):
    dictmodel = get_new_customer()
    for key, value in dictmodel.items():
        dictmodel[key] = customer[key]
    dictmodel['Age'] = str(dictmodel['Age'])
    return dictmodel


def db_customer_to_device_dict(customer):
    dictmodel = get_new_device()
    customer['IMEI'] = customer['equipment']['IMEI']
    customer['ImageURL'] = customer['equipment']['product']['ImageURL']
    customer['Model'] = customer['equipment']['product']['Model']
    customer['Type'] = customer['equipment']['product']['Type']
    customer['IMSI'] = customer['sim']['IMSI']
    customer['MSISDN'] = customer['sim']['MSISDN']

    for key, value in dictmodel.items():
        dictmodel[key] = customer[key]
    return dictmodel


def db_customer_to_full_dict(customer):
    dictmodel = db_customer_to_customer_dict(customer)
    device = db_customer_to_device_dict(customer)
    dictmodel.update(device)
    return dictmodel


def edit_customer(driver, newCustomer):
    gui_id = get_gui_customer_ids()
    for key, value in newCustomer.items():
        try:
            element = driver.find_element_by_id(gui_id[key])
            element.clear()
            element.send_keys(value)
        except:
            print('could not edit '+key)


def edit_device(driver, newDevice):
    gui_id = get_gui_device_ids()
    for key, value in newDevice.items():
        try:
            element = driver.find_element_by_id(gui_id[key])
            element.clear()
            element.send_keys(value)
        except:
            FAIL = '\033[91m'
            print(
                f"{FAIL}Failure, could not edit: {FAIL}" + key)
