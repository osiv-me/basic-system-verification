import requests
from fixtures import db_setup

class TestClass():
	def test_get_customers(self,db_setup):
		response=requests.get('http://localhost:6399/customers')
		customers=response.json()		
		assert len(customers)==1
		assert response.status_code == 200

	