import config as config
from flask import jsonify, Flask, render_template, request, redirect, url_for
from connections import get_data, push_contact

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

    return render_template('childTemplates/projects.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                            contact_form_fields=contact_form_fields)

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
    courseData = data['in_edu_project']['edu_project']
    
    return render_template('childTemplates/eduProjects.html', courseData=courseData, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)

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
 
@app.route('/underConstruction', methods=['GET', 'POST'])
def underConstruction():
    return render_template('childTemplates/underConstruction.html')
 
@app.route('/test', methods=['GET', 'POST'])
def test():
    data = get_data()
    mainMenu_items = data['main']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']   
    course_data = data['in_personal_project']['personal_project']
    
    return render_template('childTemplates/test.html', course_data=course_data, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)
    
if __name__ == '__main__':
    app.run(debug=True)
    
