#!/usr/bin/python
list = ["a", "ab", "abc"]
#print list
for li in list:
	print "current li: ", li

print range(len(list)) 
for li in range(len(list)):
	print "current li: ", list[li], "index is: ", li
