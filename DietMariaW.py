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


sql1="INSERT INTO DietComplyW(Patient,rfsdata,rfsevent,rfstime,esfdata,efsevent,efstimerecdata,recevent,rectime,genistein,daidzein,glycitein,secoisolariciresinol,total_isoflavones,total_lignans,total_phytoestrogens,lngenistein,lndaidzein,lnglycitein,lnsecoisolariciresinol,lntotal_isoflavones,lntotal_lignans,lntotal_phytoestrogens,lymphnode,tumourgrade,tumoursize,prechemo,preradiotherapy,tamoxaroma,Herceptin,timesincediagnosis,ageatdiagnosis,year1date1,lastdatefitandwell1,datedistantmets1,datelocalregionalrecurrence1,datenewprimary1,dateofdeath1,causeofdeath,rfstime1,rfstime2,rfstime3,ageatdiagnosisrfstime1,ageatdiagnosisrfstime2,ageatdiagnosisrfstime3,efstime1,efstime2,efstime3,ageatdiagnosisefstime1,ageatdiagnosisefstime2,ageatdiagnosisefstime3,tamoxaromaefstime1,tamoxaromaefstime2,tamoxaromaefstime3) VALUES('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}'','{8}'','{9}'','{10}'','{11}'','{12}'','{13}'','{14}'','{15}'','{16}'','{17}'','{18}'','{19}'','{20}'','{21}'','{22}'','{23}'','{24}'','{25}'','{26}'','{27}'','{28}'','{29}'','{30}'','{31}'','{32}'','{33}'','{34}'','{35}'','{36}'','{37}'','{38}'','{39}'','{40}'','{41}'','{42}'','{43}'','{44}'','{45}'','{46}'','{47}'','{48}'','{49}'','{50}'','{51}'','{52}'','{53}'','{54}'','{55}')"

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
        for cx in range(55):
            cell_value = sh.cell_value(rowx=rx, colx=cx)
            row.append(cell_value)
        i += 1
        print(*row)
        cursor.execute(sql1.format(*row))
        if i == 2:
            break
