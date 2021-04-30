import requests
from fixtures import db_clean
from environmentVariables import localhost_port


class TestClass():
    def test_get_customers(self, db_clean):
        response = requests.get(localhost_port+'customers')
        customers = response.json()
        assert len(customers) == 1
        assert response.status_code == 200

    # Create a new Customer (without Equipment and SIM card).
    def test_create_customer_empty(self, db_clean):
        payload = {
            'Firstname': "Emil",
            'Lastname': "Erlandsson",
            'Age': "69",
            'Sex': "Male",
            'Street': "Streety McStreet Street",
            'Zip':  "37141",
            'City': "Karlskrona",
            'Nationality': "Sweden",
            'Email': "emil.erlandsson@gmail.com",
            'Password': "secret_word"
        }
        response = requests.post(
            localhost_port+'customers', json=payload)
        assert response.status_code == 201
        customer = response.json()
        assert type(customer["ID"]) == int
        payload["ID"] = customer["ID"]
        payload["SubscriptionPtr"] = None
        payload["IMSIPtr"] = None
        payload["IMEIPtr"] = None
        for key, value in customer.items():
            # show error that age is increased by 1,
            if key == "Age":
                assert payload[key] == str(value)
                continue
            assert payload[key] == value
    # Create new SIM card

    def test_create_SIM(self, db_clean):
        payload = {
            "IMSI": "IMSI_0123456789",
            "MSISDN": "+46723580953"
        }
        response = requests.post(
            localhost_port+'sims', json=payload)
        assert response.status_code == 201
        sim = response.json()
        assert type(sim["ID"]) == int
        payload["ID"] = sim["ID"]
        for key, value in sim.items():
            assert payload[key] == value

    # Update Customer and the ‘IMSIPtr’ with the new SIM card ID.
    def test_update_customer(self, db_clean):
        response = requests.get(localhost_port+'customers')
        customers = response.json()
        customer_id = customers[0]['ID']
        sim_id = customers[0]['IMSIPtr']
        print(customers)
        payload = {
            'Firstname': "Emil",
            'Lastname': "Erlandsson",
            'Age': "69",
            'Sex': "Male",
            'Street': "Streety McStreet Street",
            'Zip':  "37141",
            'City': "Karlskrona",
            'Nationality': "Sweden",
            'Email': "emil.erlandsson@gmail.com",
            'Password': "secret_word",
            'IMSIPtr': str(sim_id),
            'IMEIPtr': None
        }
        response = requests.put(
            localhost_port+'customers/%d' % (customer_id), json=payload)
        assert response.status_code == 200
        customer = response.json()
        print(customer)
        assert type(customer) is dict  # is not a dict
        assert type(customer["ID"]) == int

        payload["ID"] = customer_id
        payload["SubscriptionPtr"] = None
        payload["Age"] = int(payload["Age"])
        payload["IMSIPtr"] = int(payload["IMSIPtr"])

        for key, value in customer.items():
            assert payload[key] == value

    # Create a new Equipment, reference the already existing ProductID.
    def test_create_equipment(self, db_clean):
        response = requests.get(localhost_port+'products')
        assert response.status_code == 200

        product = response.json()
        assert len(product) == 1
        product_id = int(product[0]["ID"])
        payload = {
            'IMEI': "IMEI_1337",
            'ProductPtr': product_id
        }
        response = requests.post(
            localhost_port+'equipments', json=payload)
        assert response.status_code == 201

        equipment = response.json()
        assert type(equipment["ID"]) == int
        payload["ID"] = equipment["ID"]
        for key, value in equipment.items():
            assert payload[key] == value

    # Update Customer and the IMEIPtr with the new EquipmentID.

    def test_update_customer_equipment(self, db_clean):
        response = requests.get(localhost_port+'customers')
        customers = response.json()
        customer_id = customers[0]['ID']
        response = requests.get(localhost_port+'equipments')
        assert response.status_code == 200
        equipment = response.json()
        assert len(equipment) == 1
        equipment_id = int(equipment[0]["ID"])
        payload = {
            'Firstname': "Emil",
            'Lastname': "Erlandsson",
            'Age': "69",
            'Sex': "Male",
            'Street': "Streety McStreet Street",
            'Zip':  "37141",
            'City': "Karlskrona",
            'Nationality': "Sweden",
            'Email': "emil.erlandsson@gmail.com",
            'Password': "secret_word",
            'IMEIPtr': str(equipment_id)
        }
        response = requests.put(
            localhost_port+'customers/%d' % (customer_id), json=payload)
        assert response.status_code == 200
        customer = response.json()

        payload["ID"] = customer_id
        payload["SubscriptionPtr"] = None
        payload["Age"] = int(payload["Age"])
        payload["IMEIPtr"] = int(payload["IMEIPtr"])
        payload["IMSIPtr"] = customer["IMSIPtr"]

        for key, value in customer.items():
            assert payload[key] == value
