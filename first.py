#!/usr/bin/env python
str = "this is first file"
print str
class employee:
	__salary = 2000
	def __init__(self, name, eid):
		self.name = name
		self.eid = eid
	def displayEmp(self):
		print "name is: %s " , self.name
		print "id is : %d " , self.eid
	def setsalary(self, salary):
		self.__salary = salary
	def getsalary(self):
		print "salary is %d ", self.__salary
	
print employee.__salary
emp1 = employee("tuneer", 22)
emp1.displayEmp()
class employeeChild(employee):
	def __init__(self):
		print "employeechild constructor"
	
child = employeeChild()
child.setsalary(1000)
child.getsalary()
print child.__salary
