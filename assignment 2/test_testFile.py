import requests
from fixtures import db_clean


class TestClass():
    def test_get_customers(self, db_clean):
        response = requests.get('http://localhost:6399/customers')
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
            'City': "Karlskrona"
        }
        response = requests.post(
            'http://localhost:6399/customers', json=payload)
        assert response.status_code == 201

        # Create new SIM card
    def test_create_SIM(self, db_clean):
        payload = {
            "IMSI": "IMSI_0123456789",
            "MSISDN": "+46723580953"
        }
        response = requests.post(
            'http://localhost:6399/sims', json=payload)
        assert response.status_code == 201
        sim = response.json()
        print(sim)
        assert type(sim["ID"]) is int

    # Update Customer and the ‘IMSIPtr’ with the new SIM card ID.
    def test_update_customer(self):
        SIM_id = 636
        customer_id = 513
        payload = {
            'Firstname': "Emil",
            'Lastname': "Erlandsson",
            'Age': "69",
            'Sex': "Male",
            'Street': "Streety McStreet Street",
            'Zip':  "37141",
            'City': "Karlskrona",
            'IMSIPtr': str(SIM_id)
        }
        response = requests.put(
            'http://localhost:6399/customers/%d' % (customer_id), json=payload)
        assert response.status_code == 200
        assert type(response.json()) is dict
        # we need to check what is returned, but the return data is poorly parsed. it is not a dict

    # Create a new Equipment, reference the already existing ProductID.
    # def test_create_equipment(self):

        # Update Customer and the IMEIPtr with the new EquipmentID.
