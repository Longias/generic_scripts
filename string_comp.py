#!/usr/bin/python
# this function will accept two parameters and generate regex for the same
# remove main call of function to externalize allow import to this script
# replace print regex to return regex 
# and ready to call this function as generic comparison of any two strings

import sys
str1=sys.argv[1]
str2=sys.argv[2]
def str_compare(str1,str2):
#	str1="abcdefghi this is abc"
#	str2="abcdef this is just another abc"
	counter=0
	regex=""
	for i, j in zip(str1, str2):
		if(i==j):
			regex=regex+i
			counter=0
		elif(counter==0):
			regex=regex+'*'
			counter=1
	print regex
str_compare(str1,str2)
