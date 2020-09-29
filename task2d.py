#!usr/bin/python3
print('content-type:text/html')
print()

import subprocess as sp
import cgi

form=cgi.FieldStorage()
osname=form.getvalue('n')
osimage=form.getvalue('i')

cmd='sudo docker run -dit --name {0} {1}'.format(osname,osimage)
output=sp.getstatusoutput(cmd)
status=output[0]
out=output[1]
if status==0:
	print('OS launcher with name {} and image {}'.format(osname,osimage))
else:
	print("some error")