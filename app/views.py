from app import app
from flask import render_template, request, flash, redirect

from .pages import pages
from .forms import GrantForm

@app.route('/')
def index():
    return render_template('index.html',
                           active='/',
                           pages=pages)


@app.route('/<route>')
def generic_view(route):
    return render_template(pages[route]['template'],
                           active=route,
                           page=pages[route],
                           pages=pages,form=GrantForm())



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
