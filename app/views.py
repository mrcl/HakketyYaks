import os
import re
from glob import glob
from app import app
from flask import render_template, request, flash, redirect, url_for
from .pages import pages
from .value_ink_vars import FACTS
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
    report_files = glob('app%s/old/*.json'%path)

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
    form = GrantForm()
    if form.validate_on_submit() and request.method == 'POST':
    #if request.method == 'POST':
        pool = form.pool.data
        area = form.area.data
        age = form.age.data
        group = form.group.data
        amount = form.amount.data
        percent = form.percent.data

        result = ghv.calc_approve(pool,area,age,group,amount,percent)

        return render_template('grant-hunter-results.html',
                               pages=pages,
                               method=request.method,
                               form=GrantForm(),
                               result=result,
                               list_pool=ghv.list_pool)

    return render_template('grant-hunter-form.html',
                           pages=pages,
                           form=GrantForm(),
				list_pool=ghv.list_pool,
				list_area=ghv.list_area,
				list_age=ghv.list_age,
				list_group=ghv.list_group,
				list_amount=ghv.list_amount,
				list_percent=ghv.list_percent
				)



@app.route('/value-ink', methods=['GET', 'POST'])
def value_ink():
    form = ValueInkForm()

    if form.validate_on_submit() or request.method == 'POST':

        p_budget_values = [
            1.084671616,
            0.348805923,
            0.081447637,
            0.009242686,
            0.013894476,
            0,
            0,
            0.039521726,
            0.309450566,
            35.37391036,
        ]

        check_box_list_results = [
            form.checkbox_1.data,
            form.checkbox_2.data,
            form.checkbox_3.data,
            form.checkbox_4.data,
            form.checkbox_5.data,
            form.checkbox_6.data,
            form.checkbox_7.data,
            form.checkbox_8.data,
            form.checkbox_9.data,
            form.checkbox_10.data,
        ]

        selection_based_result = 0
        for cb, v in zip(check_box_list_results, p_budget_values):
            if cb:
                selection_based_result += v

        print('age_group', form.age_group.data)
        return render_template('value-ink.html',
                               pages=pages,
                               method=request.method,
                               form=form,
                               selection_based_result='%3.2f' % selection_based_result,
                               facts=FACTS[form.age_group.data])


    return render_template('value-ink.html',
                           pages=pages,
                           form=form,
                           selection_based_result=None)


@app.route('/mind-the-gap')
def generic_view():
    route = 'mind-the-gap'
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
