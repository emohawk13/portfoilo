# app.py
import config as config
from flask import Flask, render_template, request
from connections import main_menu, in_edu, in_project, project_items, insert_contact
#from projectConnection import get_personal_project_items

app = Flask(__name__)
app.config.from_pyfile('config.py')


@app.route('/')
def home():
    # Call the functions to get the menu items and contact form fields
    menu = main_menu()
    mainMenu_items = menu['main_menu_items']
    socialMenu_items = menu['social_menu_items']
    comboMenu = menu['comboMenu']
    contact_form_fields = menu['contact_form_fields']

    return render_template('index.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)

@app.route('/goHome')
def goHome():
    # Call the functions to get the menu items and contact form fields
    main_m = main_menu()
    mainMenu_items = main_m['main_menu_items']
    socialMenu_items = main_m['social_menu_items']
    comboMenu = main_m['comboMenu']
    contact_form_fields = main_m['contact_form_fields']

    return render_template('index.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)

@app.route('/contact_submitted', methods=['POST'])
def contact_submitted():
    main_m = main_menu()
    mainMenu_items = main_m['main_menu_items']
    socialMenu_items = main_m['social_menu_items']
    comboMenu = main_m['comboMenu']
    contact_form_fields = main_m['contact_form_fields']
    
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('contactEmail')
    about = request.form.get('tellMeAboutYou')
    
    try:
        insert_contact(first_name, last_name, email, about)
    except:
        return "There was an error submitting your data, please try again.", 500

    return render_template('contact.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    in_project_items = in_project()
    in_project_menu = in_project_items['project_items']
    socialMenu_items = in_project_items['social_menu_items']
    comboMenu = in_project_items['comboMenu']
    contact_form_fields = in_project_items['contact_form_fields']
    return render_template('projects.html', in_project_menu=in_project_menu, socialMenu_items=socialMenu_items, 
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)

@app.route('/edu', methods=['GET', 'POST'])
def edu():
    edu_menu = in_edu()
    in_edu_menu = edu_menu['in_edu_items']
    socialMenu_items = edu_menu['social_menu_items']
    comboMenu = edu_menu['comboMenu']
    contact_form_fields = edu_menu['contact_form_fields']
    return render_template('edu.html', in_edu_menu=in_edu_menu, socialMenu_items=socialMenu_items, 
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)

@app.route('/projectBlog', methods=['GET', 'POST'])
def projectBlog():
    main_menu = main_menu()
    mainMenu_items = main_menu['main_menu_items']
    socialMenu_items = main_menu['social_menu_items']
    comboMenu = main_menu['comboMenu']
    contact_form_fields = main_menu['contact_form_fields']
    return render_template('projectBlog.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, 
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)

@app.route('/eduProjects', methods=['GET', 'POST'])
def eduProjects():
    in_project_items = project_items()
    in_project_menu = in_project_items['in_project']
    socialMenu_items = in_project_items['social_menu_items']
    comboMenu = in_project_items['comboMenu']
    contact_form_fields = in_project_items['contact_form_fields']
    return render_template('eduProjects.html', in_project_menu=in_project_menu, socialMenu_items=socialMenu_items, 
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)
    
@app.route('/personalProjects', methods=['GET', 'POST'])
def personalProjects():
    in_project = project_items()
    in_project_menu = in_project['in_project']
    socialMenu_items = in_project['social_menu_items']
    comboMenu = in_project['comboMenu']
    contact_form_fields = in_project['contact_form_fields']
    return render_template('personalProjects.html', in_project_menu=in_project_menu, socialMenu_items=socialMenu_items, 
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)


if __name__ == '__main__':    app.run(debug=True)

