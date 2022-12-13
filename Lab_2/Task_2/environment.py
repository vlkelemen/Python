from wsgiref.simple_server import make_server
from html import escape
from urllib.parse import parse_qs
from datetime import datetime

html = b"""
<html>
    <body style="background-color:#FAEBD7; font-size: 30px">
    
        <form method="get" action="">
        
            <p style="color:red">
                x: <input type="number" name="first_value" value="%(x)s">
            </p>
            
            <p style="color:blue">
                y: <input type="number" name="second_value" value="%(y)s">
            </p>
            
            <p>
                <input style="background:#3630a3;color:white;font-size:25px" type="submit" value="Submit">
            </p>
            
        </form>
        
        
        <p style="color:blueviolet">
            Summary of x and y:  %(sum)s<br>
        </p>
        
        <p style="color:blueviolet">
            Date: %(date)s<br>
        </p>
              
    </body>
</html>
"""


def application(environment, start_response):

    # Get value from the form
    d = parse_qs(environment['QUERY_STRING'])
    x = d.get('first_value', [''])[0]
    y = d.get('second_value', [''])[0]

    date = datetime.now()

    # Convert the characters &, < and > in string to HTML-safe sequences
    x = escape(x)
    y = escape(y)

    # If x and y are numeric (0-9)
    if x and y:
        x = int(x)
        y = int(y)
        sum = x + y
        sum = int(sum)
    else:
        sum = ''

    response_body = html % {
        b'x': str.encode(str(x)),
        b'y': str.encode(str(y)),
        b'sum': str.encode(str(sum)),
        b'date': str.encode(str(date))
    }

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]


# Create a new WSGI server listening on host and port, accepting connections for app
with make_server('', 8000, application) as server:
    print('Serving on port 8000...')
    server.serve_forever()
