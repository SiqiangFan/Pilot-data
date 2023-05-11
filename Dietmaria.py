
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


sql1="INSERT INTO DietComply(Patient,rfsdata,rfsevent,rfstime,esfdata,efsevent,efstime) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}')"

os.chdir("/home/siqfan/PHENOTYPE")
file="DietCompLyf_RFS_EFS_REC_Data_3Jul2014_PE_with_add_foods.xls"


with open(file) as f:
    #xls = pd.ExcelFile(r"DietCompLyf_RFS_EFS_REC_Data_3Jul2014_PE_with_add_foods.xls")
    book = xlrd.open_workbook("DietCompLyf_RFS_EFS_REC_Data_3Jul2014_PE_with_add_foods.xls")
    sh = book.sheet_by_index(0)
    i = 0
    for rx in range(sh.nrows):
        row = []
        if rx == 0:
            continue
        for cx in range(7):
            cell_value = sh.cell_value(rowx=rx, colx=cx)
            row.append(cell_value)
        i += 1
        print(*row)
        cursor.execute(sql1.format(*row))
        if i == 6:
            break
    #f = xls.parse()
    #reader = csv.reader(f,delimiter=" ")
    #next(reader, None) 
    #for row in reader:
    #    print(row)
        #cursor.execute(sql1.format(*row)) 


