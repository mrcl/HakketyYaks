import os
import re
from glob import glob
from app import app
from flask import render_template, request, flash, redirect, url_for
from .pages import pages
from .forms import GrantForm


@app.route('/')
def index():
    return render_template('index.html',
                           active='/',
                           pages=pages)



@app.route('/nz-revenue')
def revenue():

    path = url_for('static', filename='data/revenue')
    report_files = glob('app%s/*json'%path)

    reports = {}
    for rf in report_files:
        reports['year'] = re.findall('201\d', rf)[0]
        reports['json_file'] = rf.replace('app', '')

    route = 'nz-revenue'

    return render_template(pages[route]['template'],
                           active=route,
                           page=pages[route],
                           pages=pages,
                           reports=reports)


@app.route('/<route>', methods=['GET', 'POST'])
def generic_view(route):

    if route == 'grant-hunter':
        return render_template(pages[route]['template'],
                               active=route,
                               page=pages[route],
                               pages=pages,
                               form=GrantForm())

    else:
        return render_template(pages[route]['template'],
                               active=route,
                               page=pages[route],
                               pages=pages)



@app.route('/partition')
def partition_chart():
    return render_template('widgets/partition_chart.html',
                           active='tab-info',
                           pages=pages)


@app.route('/tree')
def collapsible_tree():
    return render_template('widgets/collapsible_tree.html',
                           active='tab-info',
                           pages=pages)
