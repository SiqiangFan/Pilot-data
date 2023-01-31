import pandas as pd
import openpyxl
import xlrd
import os

os.chdir("/home/siqfan/PHENOTYPE")
xls = pd.ExcelFile(r"DietCompLyf_RFS_EFS_REC_Data_3Jul2014_PE_with_add_foods.xls")
sheetX = xls.parse(0)
print(sheetX)

