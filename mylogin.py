#!/usr/bin/env python3
import cgi, cgitb

#Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
password = form.getvalue('password')

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program </title>")
print("</head>")
print("<body>")
print("<p><b>Username</b> %s <b>password</b> %s</p>" % (username, password))
print("</body>")
print("</html>")
