import os
import config as config
from flask import Flask, render_template, request, redirect, url_for, jsonify
from connections import get_data, push_contact
from projectData.CEIS412.math import *
from projectData.CEIS412.Wk3math import *


app = Flask(__name__)

app.config.from_pyfile('config.py')

@app.before_request
def check_route_status():
    path = request.path
    data = get_data()
    keys_to_check = ['main','edu','work']
    for key in keys_to_check:
        menu_items = data[key]['menu_items']
        for item in menu_items:
            if item.get("toRoute") == path and item.get("active", 0) == 0:
                return redirect(url_for("goHome"))

@app.route('/')
def home():
    data = get_data()
    mainMenu_items = data['main']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']

    return render_template('index.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)

@app.route('/goHome')
def goHome():
    return home()

@app.route('/contact_submitted', methods=['POST'])
def contact_submitted():
    data = get_data()
    mainMenu_items = data['main']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('contactEmail')
    about = request.form.get('tellMeAboutYou')

    try:
        push_contact(first_name, last_name, email, about, True)
    except:
        return "There was an error submitting your data, please try again.", 500

    return render_template('childTemplates/contact.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                          contact_form_fields=contact_form_fields)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    data = get_data()
    mainMenu_items = data['project']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    projectData = data['project']['allProjects']
    
    return render_template('childTemplates/projects.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                            contact_form_fields=contact_form_fields, projectData=projectData)

@app.route('/projectAdmin', methods=['GET', 'POST'])
def projectAdmin():
    data = get_data()
    mainMenu_items = data['main']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']

    return render_template('childTemplates/projectAdmin.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                           contact_form_fields=contact_form_fields)

@app.route('/edu', methods=['GET', 'POST'])
def edu():
    data = get_data()
    mainMenu_items = data['edu']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    otherEduData = data['edu']['otherEduProjects'] 
    eduProjectData = data['edu']['eduProjects']
    eduPast = data['edu']['eduProjectsPast']

    return render_template('childTemplates/edu.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                            contact_form_fields=contact_form_fields, otherEduData=otherEduData, eduProjectData=eduProjectData,
                            eduPast=eduPast)

@app.route('/takenCourses', methods=['GET', 'POST'])
def takenCourses():
    data = get_data()
    mainMenu_items = data['edu']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    courseData = data['edu']['course_data']
    
    return render_template('childTemplates/takenCourses.html', courseData=courseData, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)
 
@app.route('/work', methods=['GET', 'POST'])
def work():
    data = get_data()
    mainMenu_items = data['work']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    work_data = data['work']['work']
    
    return render_template('childTemplates/work.html',work_data=work_data, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)

@app.route('/ceis420', methods=['GET', 'POST'])
def ceis420():
    monthArray = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    if request.method == 'POST':
        monthlySales = [0] * len(monthArray)

        get_sales(monthArray, monthlySales)
        totalSales = compute_total_sales(monthlySales)
        averageSales = compute_average_sales(monthlySales)
        highestMonth = compute_highest_month(monthlySales)
        highestSales = monthlySales[highestMonth]
        lowestMonth = compute_lowest_month(monthlySales)
        lowestSales = monthlySales[lowestMonth]

        return render_template('projects/edu/CEIS420/output.html', totalSales=totalSales, averageSales=averageSales, highestMonth=monthArray[highestMonth], highestSales=highestSales, lowestMonth=monthArray[lowestMonth], lowestSales=lowestSales, monthArray=monthArray)

    return render_template('projects/edu/CEIS420/input.html', monthArray=monthArray)

@app.route('/ceis420wk2_default', methods=['GET', 'POST'])
def ceis420wk2_default():
    rows = 10
    pattern_A = patA(rows)
    pattern_B = patB(rows)
    pattern_C = patC(rows)
    pattern_D = patD(rows)
    return render_template('projects/edu/CEIS420/week2.html', pattern_A=pattern_A, pattern_B=pattern_B, pattern_C=pattern_C, pattern_D=pattern_D)

@app.route('/ceis420wk2/<string:pattern_type>/<int:numRows>', methods=['GET', 'POST'])
def ceis420wk2(pattern_type, numRows):
    pattern_functions = {
        'patA': patA,
        'patB': patB,
        'patC': patC,
        'patD': patD
    }
    
    pattern_function = pattern_functions.get(pattern_type)
    
    if pattern_function is None:
        return jsonify(error="Invalid pattern type"), 400
    
    return jsonify(pattern=generate_pattern(pattern_function, numRows))

@app.route('/ceis420wk3', methods=['GET', 'POST'])
def ceis420wk3():
    result = None
    if request.method == 'POST':
        phone_num = request.form['phone_num']
        is_valid = is_valid_phone_number(phone_num)

        if is_valid:
            result = 'Valid number'
        else:
            result = 'Not valid'

    return render_template('projects/edu/CEIS420/week3.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
    
