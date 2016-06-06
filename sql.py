#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect("localhost","root","tuneer")
cursor = db.cursor()
cursor.execute("USE tuneer")
cursor.execute("")
b.close()
