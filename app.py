# app.py
import pymysql
import connections.config as config
import logging
from flask import Flask, redirect, url_for, render_template, request
from connections.connections import connect_db, get_social_menu_items, get_contact_form_fields, insert_contact
from connections.projectConnection import connect_db, get_social_menu_items, get_contact_form_fields, insert_contact

app = Flask(__name__)
app.config.from_pyfile('config.py')

# Connect to the database
with app.app_context():
    connect_db(app)


@app.route('/')
def index():
    mainMenu_items = [
        {'name': 'Home', 'url': '/home'},
        {'name': 'About', 'url': '/home'},
        {'name': 'Services', 'url': '/home'},
        {'name': 'Contact', 'url': '#', 'class': 'contact-button', 'data-toggle': 'modal',
         'data-target': '#contactModal'}
    ]
    socialMenu_items = get_social_menu_items()
    comboMenu = mainMenu_items + socialMenu_items

    contact_form_fields = get_contact_form_fields()  # Get the contact form fields

    return render_template('index.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items,
                           comboMenu=comboMenu, contact_form_fields=contact_form_fields)


@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Retrieve the form data
    first_name = request.form.get('firstName')
    last_name = request.form.get('lastName')
    email = request.form.get('contactEmail')
    about = request.form.get('tellMeAboutYou')

    # Insert the data into the MySQL database
    insert_contact(first_name, last_name, email, about)

    # Handle successful submission (e.g., redirect to a thank you page)
    return redirect(url_for('index'))


if __name__ == '__main__':    app.run(debug=True)

