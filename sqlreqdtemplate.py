#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect("localhost","root","tuneer")
cursor = db.cursor()
cursor.execute("USE tuneer")
sql = "select * from employee"
try:
	cursor.execute(sql)
	db.commit()
	print "success"
	result = cursor.fetchall()
	for row in result:
		id = row[0]
		name = row[1]
		print "id is %d, name is %s" % (id, name)
except:
	print "error"
	db.rollback()
db.close()
