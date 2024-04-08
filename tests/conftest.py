import os
import shutil
import zipfile
import pytest
from path import TEMP, RESOURCE, ZIP_FILE


@pytest.fixture(scope='session', autouse=True)
def create_archive():
    if not os.path.exists(RESOURCE):
        os.mkdir(RESOURCE)  # Создаю папку resource

    with zipfile.ZipFile(ZIP_FILE, 'w') as zf:  # Создаю архив
        for files in os.listdir(TEMP):
            creating_file = os.path.join(TEMP, files)
            zf.write(creating_file, os.path.basename(creating_file))

    yield  # Вызов pytest.fixture завершен
    shutil.rmtree(RESOURCE)  # Удаляем папку resource
