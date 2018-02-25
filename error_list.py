#!/usr/bin/python
import re
def error_parse_list():
	str1=""
	with open('data/Error','r') as e:
		for err in e:
			if (str1):
				str1=str1 + ' | ' 
			else:
				str1='r'
			str1=str1+'[\\b'+err.rstrip()+'\\b]'
		#	print str1
		return str1
	#	print str
