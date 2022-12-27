from flask import render_template

from app.home import home_bp


@home_bp.route('/')
def main():
    return render_template('home.html', page=1)


@home_bp.route('/about')
def about():
    hobies = ("Programming", "Computer Games", "Board Games", "Tennis", "Basketball", "Reading", "Watching movies")
    return render_template('about.html', hobies=hobies, page=2)
