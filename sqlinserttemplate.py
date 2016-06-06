#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect("localhost","root","tuneer")
cursor = db.cursor()
cursor.execute("USE tuneer")
sql = "insert into employee VALUES('%d', '%s')" % (1, 'tuneer')
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()
