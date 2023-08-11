import config as config
from flask import jsonify, Flask, render_template, request
from connections import get_data, push_contact

app = Flask(__name__)
app.config.from_pyfile('config.py')

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

    return render_template('contact.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                          contact_form_fields=contact_form_fields)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    data = get_data()
    mainMenu_items = data['in_project']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']

    return render_template('projects.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                            contact_form_fields=contact_form_fields)

@app.route('/projectBlog', methods=['GET', 'POST'])
def projectBlog():
    data = get_data()
    mainMenu_items = data['main']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']

    return render_template('projectBlog.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                           contact_form_fields=contact_form_fields)

@app.route('/personalProjects', methods=['GET', 'POST'])
def personalProjects():
    data = get_data()
    mainMenu_items = data['main']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    project_data = data['in_personal_project']['personal_project']
    
    return render_template('personalProjects.html', project_data=project_data, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)

@app.route('/eduProjects', methods=['GET', 'POST'])
def eduProjects():
    data = get_data()
    mainMenu_items = data['edu']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']
    courseData = data['in_edu_project']['edu_project']
    
    return render_template('eduProjects.html', courseData=courseData, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
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
    
    return render_template('takenCourses.html', courseData=courseData, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)
 
@app.route('//test', methods=['GET', 'POST'])
def test():
    data = get_data()
    mainMenu_items = data['main']['menu_items']
    socialMenu_items = data['main']['social_menu_items']
    contact_form_fields = data['main']['contact_form_fields']   
    course_data = data['in_personal_project']['personal_project']
    
    return render_template('test.html', course_data=course_data, mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                            contact_form_fields=contact_form_fields)
    
if __name__ == '__main__':
    app.run(debug=True)
    
    
    