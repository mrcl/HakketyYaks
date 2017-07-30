import os
import re
from glob import glob
from app import app
from flask import render_template, request, flash, redirect, url_for
from .pages import pages
from .forms import GrantForm, ValueInkForm
import app.grant_hunter_vars as ghv

@app.route('/')
def index():
    return render_template('index.html',
                           active='/',
                           pages=pages)

@app.route('/nz-revenue')
@app.route('/nz-revenue/<year>')
def revenue(year=None):
    path = url_for('static', filename='data/revenue')
    report_files = glob('app%s/*json'%path)

    reports = {}
    for rf in report_files:
        y = re.findall('201\d', rf)[0]
        reports[y] = rf.replace('app', '')

    years = list(reports.keys())
    years.sort()
    route = 'nz-revenue'

    return render_template(pages[route]['template'],
                           active=route,
                           page=pages[route],
                           pages=pages,
                           years=years,
                           report=reports[year] if year else None,
                           year=year
                           )


@app.route('/grant-hunter', methods=['GET', 'POST'])
def grant_hunter():

    if request.method == 'POST':
        return render_template('grant-hunter-results.html',
                               pages=pages,
                               method=request.method,
                               form=ValueInkForm(),
                               list_pool=ghv.list_pool)

    return render_template('form-view.html',
                           pages=pages,
                           form=ValueInkForm())


@app.route('/value-ink', methods=['GET', 'POST'])
def value_ink():
    form = ValueInkForm()

    if form.validate_on_submit() or request.method == 'POST':
        
        return render_template('value-ink.html',
                               pages=pages,
                               method=request.method,
                               form=form)


    return render_template('value-ink.html',
                           pages=pages,
                           form=form)


@app.route('/generic_view')
def generic_view(route):

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
