from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__)


@app.route('/')
def main():
    user_agent = request.headers.get('User-Agent')
    time = datetime.now().strftime("%H:%M:%S")
    return render_template('home.html', page=1, footer_info={'os_name': os.uname(), 'user_agent': user_agent, 'time': time})


@app.route('/about')
def about():
    user_agent = request.headers.get('User-Agent')
    time = datetime.now().strftime("%H:%M:%S")
    hobies = ("Programming", "Computer Games", "Board Games", "Tennis", "Basketball", "Reading", "Watching movies")
    return render_template('about.html', hobies=hobies, page=2, footer_info={'os_name': os.uname(), 'user_agent': user_agent, 'time': time})


@app.route('/contact')
def contact():
    now = datetime.now()
    user_agent = request.headers.get('User-Agent')
    current_time = now.strftime("%H:%M:%S")
    minute = now.strftime("%M")
    return render_template('contact.html', time=current_time, minute=minute, page=3, footer_info={'os_name': os.uname(), 'user_agent': user_agent, 'time': current_time})

if __name__ == '__main__':
    app.run()
