import pytest
import shutil
from environmentVariables import *


@pytest.fixture()
def db_clean():
    shutil.copy(db_backup_path, db_path)
    yield None
    shutil.copy(db_backup_path, db_path)
