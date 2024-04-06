import os
import csv
import zipfile
from pypdf import PdfReader
from os_put import RESOURCE
from openpyxl import load_workbook

def test_pdf():
    with zipfile.ZipFile(os.path.join(RESOURCE, 'file.zip')) as zip_file:
        with zip_file.open('Python Testing with Pytest (Brian Okken).pdf') as pdf_file:
            reader = PdfReader(pdf_file)
            page = reader.pages[256]
            text = reader.pages[2].extract_text()
            assert 'Python Testing with pytest' in text




