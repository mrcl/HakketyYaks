from app import app
from flask import render_template, request, flash, redirect


@app.route('/')
def index():
    return render_template('index.html',
                           active='tab-info')


@app.route('/partition')
def partition_chart():
    return render_template('widgets/partition_chart.html',
                           active='tab-info')

@app.route('/tree')
def collapsible_tree():
    return render_template('widgets/collapsible_tree.html',
                           active='tab-info')


