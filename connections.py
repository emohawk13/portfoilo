import pymysql
import config
import logging
from flask import current_app
from config import *

def execute_query(query):
    try:
        conn = current_app.mysql.connection
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()
        cur.close()
        return result
    except Exception as e:
        logging.error(f"An error occurred while executing the query: {query}")
        logging.error(f"Error details: {str(e)}")
        return []

def connect_db(app):
    db = app.config['MYSQL_DB']
    host = app.config['MYSQL_HOST']
    port = app.config['MYSQL_PORT']
    user = app.config['MYSQL_USER']
    password = app.config['MYSQL_PASSWORD']

    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        db=db,
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    app.mysql = conn

    @app.teardown_appcontext
    def close_db(error):
        if hasattr(app, 'mysql') and app.mysql.open:
            app.mysql.close()

    app.mysql.ping(reconnect=True)

def insert_contact(first_name, last_name, email, about):
    query = "INSERT INTO ContactMe (firstName, lastName, contactEmail, tellMeAboutYou) " \
            "VALUES (%s, %s, %s, %s)"
    try:
        conn = pymysql.connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            db=config.MYSQL_DB,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        cur = conn.cursor()
        cur.execute(query, (first_name, last_name, email, about))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logging.error(f"An error occurred while inserting contact: {str(e)}")

def get_contact_form_fields():
    field_labels = {
        'firstName': 'First Name: ',
        'lastName': 'Last Name: ',
        'contactEmail': 'Email: ',
        'tellMeAboutYou': 'Tell me about yourself: '
    }
    query = "SHOW COLUMNS FROM ContactMe"
    try:
        conn = pymysql.connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            db=config.MYSQL_DB,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()

        form_fields = []
        for row in results:
            field_name = row['Field']
            if field_name != 'contactId':
                field_label = field_labels.get(field_name, field_name)
                form_fields.append({'name': field_name, 'label': field_label})
        return form_fields

    except Exception as e:
        logging.error(f"An error occurred while fetching contact form fields: {str(e)}")
        return []


def insert_contact(first_name, last_name, email, about):
    query = "SELECT * FROM Links"
    try:
        conn = pymysql.connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            db=config.MYSQL_DB,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        cur = conn.cursor()
        cur.execute(query, (first_name, last_name, email, about))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        logging.error(f"An error occurred while inserting contact: {str(e)}")


def get_social_menu_items():
    query = "SELECT linkName, linkActual, linkIcon FROM Links WHERE linkRelation = 'Social'"
    try:
        conn = pymysql.connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            db=config.MYSQL_DB,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
        cur = conn.cursor()
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()

        social_menu_items = []
        for row in results:
            name = row['linkName']
            link = row['linkActual']
            icon = row['linkIcon']
            social_menu_items.append({'name': name, 'link': link, 'icon': icon})
        return social_menu_items

    except Exception as e:
        logging.error(f"An error occurred while fetching social menu items: {str(e)}")
        return []
  
def get_links():
    query = "SELECT * FROM Links"
    return execute_query(query)
    
#def get_course_data():
#    query = ""
