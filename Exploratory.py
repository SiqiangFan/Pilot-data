import pandas as pd
import openpyxl
import xlrd
import os



os.chdir("/home/siqfan/PHENOTYPE")
xls = pd.ExcelFile(r"Exploratory covariates 09102014.xlsx")
sheetX = xls.parse(0)
print(sheetX)
