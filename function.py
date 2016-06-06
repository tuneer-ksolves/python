#!/usr/bin/python
def func(str):
	print "entered string is : ", str
	list = ["abc says :"]
	list.append(str)
	print list
#func("hi")
import sys
if (len(sys.argv) < 2):
	print "usage: <filename> <string>"
	exit()
abc = str(sys.argv[1])
func(abc)
sum = lambda arg1, arg2: arg1+arg2
print sum(1,2)
