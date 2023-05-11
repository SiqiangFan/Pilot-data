import csv
import mariadb
import os
import configparser

config=configparser.ConfigParser(allow_no_value=True)
config.read_file(open(r'/etc/mysql/my.cnf'))



try:
	db=mariadb.connect(user="admin",password="root",host="localhost",port=3306,database='bcac')

except mariadb.Error as e:
	print(f"Error connecting to MariaDB Platform: {e}")
	sys.exit(1)

cursor = db.cursor(dictionary=True)
