import os
import config as config
from flask import jsonify, Flask, render_template, request, redirect, url_for
from connections import get_data, push_contact
from projectData.CEIS412.math import *


app = Flask(__name__)


app.config.from_pyfile('config.py')

@app.before_request
def check_route_status():
    path = request.path
    data = get_data()
    keys_to_check = ['main', 'in_project', 'edu', 'in_edu', 'in_edu_project', 'in_personal_project', 'blog', 'work', 'in_work']
    for key in keys_to_check:
        menu_items = data[key]['menu_items']
        for item in menu_items:
            if item.get("toRoute") == path and item.get("active", 0) == 0:
                return redirect(url_for("underConstruction"))

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
    mainMenu_items = data['in_project']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    projectData = data['in_project']['allProjects']
    eduProjectData = data['in_project']['eduProjects']
    
    return render_template('childTemplates/projects.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                            contact_form_fields=contact_form_fields, projectData=projectData, eduProjectData=eduProjectData)

@app.route('/projectBlog', methods=['GET', 'POST'])
def projectBlog():
    data = get_data()
    mainMenu_items = data['blog']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']

    return render_template('childTemplates/projectBlog.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                           contact_form_fields=contact_form_fields)

@app.route('/personalProjects', methods=['GET', 'POST'])
def personalProjects():
    data = get_data()
    mainMenu_items = data['main']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    project_data = data['in_personal_project']['personal_project']
    
    return render_template('childTemplates/personalProjects.html', project_data=project_data, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)

@app.route('/eduProjects', methods=['GET', 'POST'])
def eduProjects():
    data = get_data()
    mainMenu_items = data['edu']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    eduProjectData = data['in_project']['eduProjects']
    
    return render_template('childTemplates/eduProjects.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                            contact_form_fields=contact_form_fields, eduProjectData=eduProjectData)

@app.route('/edu', methods=['GET', 'POST'])
def edu():
    data = get_data()
    mainMenu_items = data['edu']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']

    return render_template('childTemplates/edu.html',  mainMenu_items= mainMenu_items, socialMenu_items=socialMenu_items, 
                            contact_form_fields=contact_form_fields)

@app.route('/takenCourses', methods=['GET', 'POST'])
def takenCourses():
    data = get_data()
    mainMenu_items = data['edu']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    courseData = data['in_edu_project']['course_data']
    
    return render_template('childTemplates/takenCourses.html', courseData=courseData, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)
 
@app.route('/work', methods=['GET', 'POST'])
def work():
    data = get_data()
    mainMenu_items = data['in_work']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    work_data = data['work']['work']
    
    return render_template('childTemplates/work.html',work_data=work_data, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)

@app.route('/workProjects', methods=['GET', 'POST'])
def workProjects():
    data = get_data()
    mainMenu_items = data['in_work']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    
    return render_template('childTemplates/workProjects.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)
 
@app.route('/test', methods=['GET', 'POST'])
def test():
    data = get_data()
    mainMenu_items = data['main']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']   
    course_data = data['in_personal_project']['personal_project']
    
    return render_template('childTemplates/underConstruction.html', course_data=course_data, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)

@app.route('/currentProjects')
def currentProjects():
    data = get_data()
    mainMenu_items = data['in_project']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    projectData = data['in_project']['allProjects']
    eduProjectData = data['in_progress']['eduProjects']
    personal_projects = data['in_progress']['personalProjects']
    
    return render_template('childTemplates/currentProjects.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                            contact_form_fields=contact_form_fields, projectData=projectData, eduProjectData=eduProjectData, personal_projects=personal_projects)
    
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

if __name__ == '__main__':
    app.run(debug=True)
    
