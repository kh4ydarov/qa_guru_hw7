import os
import csv
import zipfile
from pypdf import PdfReader
from path import RESOURCE, ZIP_FILE
from openpyxl import load_workbook

def test_pdf():
    with zipfile.ZipFile(os.path.join(ZIP_FILE)) as zip_file:
        with zip_file.open('Python Testing with Pytest (Brian Okken).pdf') as pdf_file:
            reader = PdfReader(pdf_file)
            page = reader.pages[256]
            text = reader.pages[2].extract_text()
            assert 'Python Testing with pytest' in text

def test_csv():
    with zipfile.ZipFile(os.path.join(ZIP_FILE)) as zip_file:
        with zip_file.open('Sample-Spreadsheet-100-rows.csv') as csv_file:
            content = csv_file.read().decode('latin-1')  # читаем содержимое файла
            csvreader = list(csv.reader(content.splitlines()))
            second_row = csvreader[1]  # получаем вторую строку

            assert second_row[0] == '1.7 Cubic Foot Compact ""Cube"" Office Refrigerators",Barry French,293,457.81,208.16,68.02,Nunavut,Appliances,0.58'
            assert second_row[1] == 'b'
    pass

def test_xlsx():
    with zipfile.ZipFile(os.path.join(ZIP_FILE)) as zip_file:
        with zip_file.open('file_example_XLS_10.xlsx') as xlsx_file:
            workbook = load_workbook(xlsx_file)
            sheet = workbook.active

            assert sheet.ceell(row=2, column=8).value == 'Dulce'




