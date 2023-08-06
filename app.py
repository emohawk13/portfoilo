# app.py
import config as config
from flask import Flask, redirect, url_for, render_template, request
from connections import connect_db, get_social_menu_items, get_contact_form_fields, insert_contact, generate_menu_items
#from projectConnection import get_personal_project_items

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Define the function to generate contact form fields
def generate_contact_form_fields():
    return get_contact_form_fields()

@app.route('/')
def home():
    # Call the functions to get the menu items and contact form fields
    mainMenu_items, socialMenu_items, comboMenu = generate_menu_items()
    contact_form_fields = generate_contact_form_fields()

    return render_template('index.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)

@app.route('/goHome')
def goHome():
    # Call the functions to get the menu items and contact form fields
    mainMenu_items, socialMenu_items, comboMenu = generate_menu_items()
    contact_form_fields = generate_contact_form_fields()

    return render_template('index.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)

@app.route('/contact_submitted', methods=['POST'])
def contact_submitted():
    mainMenu_items, socialMenu_items, comboMenu = generate_menu_items()
    contact_form_fields = generate_contact_form_fields()
    
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('contactEmail')
    about = request.form.get('tellMeAboutYou')
    
    try:
        insert_contact(first_name, last_name, email, about)
    except:
        return "There was an error submitting your data, please try again.", 500

    return render_template('contact.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items, comboMenu=comboMenu, contact_form_fields=contact_form_fields)

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return render_template('projects.html')

if __name__ == '__main__':    app.run(debug=True)

