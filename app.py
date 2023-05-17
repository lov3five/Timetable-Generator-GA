import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, request, redirect, url_for, flash, session


app = Flask(__name__)

# TEST
@app.route('/test')
def test():
    print("Hello World")

# GET Homepage
@app.route('/')
def index():
    return render_template('index.html')

# Chạy ứng dụng
if __name__ == '__main__':
    app.run()
