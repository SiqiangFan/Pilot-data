import csv
import mariadb
import os
import configparser
import sys
import pandas as pd
import openpyxl
import xlrd

config=configparser.ConfigParser(allow_no_value=True)
config.read_file(open(r'/etc/mysql/my.cnf'))

try:
     db=mariadb.connect(user="admin", password="root", host="0.0.0.0", port=3306, database="bcac")

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)


cursor=db.cursor(dictionary=True)


sql_mode=""
#sql1="INSERT INTO Ecovariates(Patient,ER,PR,HER2,AlcoholStatusY1,SmokedY1) VALUES($Patient,$ER,$PR,$HER2,$AlcoholStatusY1,$SmokedY1)"
#sql1="INSERT INTO Ecovariates(Patient,ER,PR,HER2,AlcoholStatusY1,SmokedY1) VALUES('Positive','Negative','Yes','No','Not Known','Current','Never')"
#sql1="INSERT INTO Ecovariates(Patient,ER,PR,HER2,AlcoholStatusY1,SmokedY1) VALUES(%s,%s,%s,%s,%s,%s)"
sql1="INSERT INTO Ecovariates(Patient,ER,PR,HER2,AlcoholStatusY1,SmokedY1) VALUES('{0}','{1}','{2}','{3}','{4}','{5}')"



os.chdir("/home/siqfan/PHENOTYPE")
file="Exploratory covariates 09102014.xls"


with open(file) as f:
    #xls = pd.ExcelFile(r"DietCompLyf_RFS_EFS_REC_Data_3Jul2014_PE_with_add_foods.xls")
    book = xlrd.open_workbook("Exploratory covariates 09102014.xls")
    
    sh = book.sheet_by_index(0)
    i = 0
    for rx in range(sh.nrows):
        row = []
        if rx == 0:
            continue
        for cx in range(6):
            cell_value = sh.cell_value(rowx=rx, colx=cx)
            row.append(cell_value)
        i += 1
        print(*row)
        cursor.execute(sql1.format(*row))
        if i == 2:
            break
    #f = xls.parse()
    #reader = csv.reader(f,delimiter=" ")
    #next(reader, None)
    #for row in reader:
    #    print(row)
        #cursor.execute(sql1.format(*row))
