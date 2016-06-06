#!/usr/bin/python
import re
import sys
line = "lets play with python"
matchline = re.match( r'(.*)ab?(.*)', line)

if matchline:
	print "matched"
	print matchline.group()
	print matchline.group(1)
	name = raw_input('enter your name')
	print name
	print len(sys.argv)
	print str(sys.argv[0])
	#print argc
else:
	print "not matched"
