#!/usr/bin/env python3
import os, json
print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World cmput404 class!</p>")


#Q1: Print environment all variables
#print(os.environ)


#json_object = json.dumps(dict(os.environ), indent = 2)
#print(json_object)

#Q2: Print out QUERY_STRING = parameter
if "QUERY_STRING" in os.environ:
    print(f"<p>QUERY_STRING={os.environ['QUERY_STRING']}</p>")

#Q3: Print out user's browser information
if "HTTP_USER_AGENT" in os.environ:
    print(f"<p>BROWSER={os.environ['HTTP_USER_AGENT']}></p>")

'''
for param in os.environ.keys():
    if(param=="QUERY_STRING"):
        #print(f"<em>{param}</em> = {os.environ[param]}</li>")
        print("<b>%20s</b>: %s<br>" %(param, os.environ[param]))


#Q3 - ?

for param in os.environ.keys():
    if (param=="HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))
'''
