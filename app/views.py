from app import app
from flask import render_template, request, flash, redirect


@app.route('/')
def index():
    return render_template('index.html',
                           active='tab-info')
