import pytest
import shutil
import requests

@pytest.fixture()
def db_clean():
	shutil.copy('/home/pft/restapi/point-of-sale/pos_bak.db', '/home/pft/restapi/point-of-sale/pos.db')

@pytest.fixture()
def customers():
	result = requests.get('http://127.0.0.1:6399/' + "customers")
	if result.status_code == 200:
		customers=result.json()
	else:
		raise Exception('error when fetching customers')

	return customers