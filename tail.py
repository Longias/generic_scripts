#!/usr/bin/python
import re
import sys
from error_list import error_parse_list 
a=len(sys.argv)
print a
if(len(sys.argv)==2):
	print "ok"
else:
	print "sorry wrong parameters passed"
	sys.exit(-1)

error_list=error_parse_list()
print "this is main function"
print error_list
str1_m=re.compile(error_list)
with open('data/log','r') as l:
	for log in l:
		if(re.search("ERROR",log)):
			if(str1_m.search(log)):
				print log
			else:
				print "This is a new error will be logged for you to have a look and decide"
#		else:
#			print "MESSSSSSSSSSSAGE"+log
