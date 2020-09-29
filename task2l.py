#!usr/bin/python3
print('content-type:text/html')
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
i=form.getvalue('l')

if 'date' in i:
	o=sp.getoutput('date')
	print(o)
elif 'calender' in i:
	o=sp.getoutput('cal')
	print(o)
elif 'ip' in i:
	o=sp.getoutput('ifconfig enp0s3')
	print(o)

