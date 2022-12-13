import cgi
from http import cookies
import os

form = cgi.FieldStorage()

first_input = form.getfirst("input-1", "not said")
second_input = form.getfirst("input-2", "not said")

if form.getvalue("math"):
    math = form.getvalue("math")
else:
    math = ""


if form.getvalue("biology"):
    biology = form.getvalue("biology")
else:
    biology = ""


if form.getvalue("chemistry"):
    chemistry = form.getvalue("chemistry")
else:
    chemistry = ""


if form.getvalue("history"):
    history = form.getvalue("history")
else:
    history = ""


if form.getvalue("language"):
    language = form.getvalue("language")
else:
    language = "I don't want to study, haha"


cs = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
cookies_counter = cs.get("cookies_counter")

if cookies_counter is None:
    print("Set-cookie: cookies_counter=0")
else:
    amount_of_cookie = int(cookies_counter.value)
    amount_of_cookie += 1

HTML = f'''<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width" />
    <title>Обробка даних форми</title>
  </head>
  <body style="background-color:#FAEBD7; font-size: 30px">
  <h1 style="color:blueviolet">Обробка даних форми!</h1>
  <p style="color:blue">First text: {first_input}</p>
  <p style="color:red">Second text: {second_input}</p>
  <p>So, your choice...: [ {math}  {biology}  {chemistry}  {history} ]</p>
  <p style="color:blue">You want to study: {language}</p> 
  <p style="color:red">Cookie: Number of completed forms: {amount_of_cookie} </p> 
  </body>
</html>'''

print("Content-type: text/html\r\n\r\n")
print()
print(HTML)
