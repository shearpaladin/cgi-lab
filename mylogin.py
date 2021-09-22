#!/usr/bin/env python3
import cgi, cgitb
import secret
import os

from http import cookies
from templates import login_page, secret_page, after_login_incorrect

cgitb.enable()


#Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
username = form.getvalue('username')
password = form.getvalue('password')



# Q5: SHOW Cookie If Login is correct
cookie_valid = False
cookie = cookies.SimpleCookie()
cookie_username = secret.username
cookie_password = secret.password

# Set cookie flag to true if secret user and pass match
if (cookie_username == username and cookie_password == password):
    cookie_valid = True



print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Hello - Second CGI Program </title>")
print("</head>")
print("<body>")

# Check if Cookie is Set to display login is correct
if cookie_valid:
    print("Set-Cookie: username={username}")
    print("Set-Cookie: password={password}")




print("<p><b>Username</b> %s <b>password</b> %s</p>" % (username, password))
#Q6
if not username and not password:
    print(login_page())

elif username == secret.username and password == secret.password:
    print(secret_page(username, password))

else: 
    print(after_login_incorrect())

print("</body>")
print("</html>")
