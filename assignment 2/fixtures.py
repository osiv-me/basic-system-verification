import pytest
import shutil

@pytest.fixture()
def db_clean():
	shutil.copy('/home/pft/restapi/point-of-sale/pos_bak.db', '/home/pft/restapi/point-of-sale/pos.db')