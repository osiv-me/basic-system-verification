import requests


def get_other_customer_webb():
    return {
        'firstname': "Emil",
        'lastname': "Erlandsson",
        'age': "69",
        'gender': "Male",
        'street': "Streety McStreet Street",
        'zipcode':  "37141",
        'city': "Karlskrona",
        'nationality': "Sweden",
        'email': "emil.erlandsson@gmail.com"
    }


def get_other_customer_db():
    return {
        'Firstname': "Emil",
        'Lastname': "Erlandsson",
        'Age': "69",
        'Sex': "Male",
        'Street': "Streety McStreet Street",
        'Zip':  "37141",
        'City': "Karlskrona",
        'Nationality': "Sweden",
        'Email': "emil.erlandsson@gmail.com"
    }


def get_customers():
    result = requests.get('http://127.0.0.1:6399/' + "customers")
    if result.status_code == 200:
        customers = result.json()
    else:
        raise Exception('error when fetching customers')
    return customers


def assertCustomerShown(customer, driver):
    assertStatus = True
    try:
        firstname = driver.find_element_by_id('firstname')
        assert firstname.get_attribute('value') == customer['Firstname']
    except:
        print('firstname failed')
        assertStatus = False
    try:
        lastname = driver.find_element_by_id('lastname')
        assert lastname.get_attribute('value') == customer['Lastname']
    except:
        print('lastname failed')
        assertStatus = False
    try:
        age = driver.find_element_by_id('age')
        assert age.get_attribute('value') == str(customer['Age'])
    except:
        print('age failed')
        assertStatus = False
    try:
        gender = driver.find_element_by_id('gender')
        assert gender.get_attribute('value') == customer['Sex']
    except:
        print('gender failed')
        assertStatus = False
    try:
        nationality = driver.find_element_by_id('nationality')
        assert nationality.get_attribute(
            'value') == customer['Nationality']
    except:
        print('nationality failed')
        assertStatus = False
    try:
        street = driver.find_element_by_id('street')
        assert street.get_attribute('value') == customer['Street']
    except:
        print('street failed')
        assertStatus = False
    try:
        zipcode = driver.find_element_by_id('zipcode')
        assert zipcode.get_attribute('value') == customer['Zip']
    except:
        print('zipcode failed')
        assertStatus = False
    try:
        city = driver.find_element_by_id('city')
        assert city.get_attribute('value') == customer['City']
    except:
        print('city failed')
        assertStatus = False
    try:
        email = driver.find_element_by_id('email')
        assert email.get_attribute('value') == customer['Email']
    except:
        print('email failed')
        assertStatus = False
    return assertStatus
