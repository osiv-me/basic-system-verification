import pytest
import shutil

@pytest.fixture()
def db_setup():
	shutil.copy('/home/pft/restapi/point-of-sale/pos_bak.db', '/home/pft/restapi/point-of-sale/pos.db')