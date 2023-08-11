import datetime
import pymysql
import config as config
import logging
from flask import current_app
from config import *


def connect_to_db():
    return pymysql.connect(
        host=config.MYSQL_HOST,
        port=config.MYSQL_PORT,
        user=config.MYSQL_USER,
        password=config.MYSQL_PASSWORD,
        db=config.MYSQL_DB,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )

def execute_query(query, params=None):
    with connect_to_db() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            results = cur.fetchall()
    return results

def push_contact(first_name, last_name, email, about, pressed):
    current_time = datetime.datetime.now()
    try:
        with connect_to_db() as conn:
            cur = conn.cursor()
            cur.execute(insertQuery, (first_name, last_name, email, about, current_time))
            conn.commit()
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        raise

def get_contact_form_fields():
    field_labels = {
        "firstName": "First Name: ",
        "lastName": "Last Name: ",
        "contactEmail": "Email: ",
        "tellMeAboutYou": "Tell me about yourself: ",
    }
    query = "SHOW COLUMNS FROM ContactMe"
    try:
        results = execute_query(query)
        return [{"name": row["Field"], "label": field_labels.get(row["Field"], row["Field"])} 
                for row in results if row["Field"] not in ["contactId", "suggestedProject", "timeOfContact"]]
    except Exception as e:
        logging.error(f"An error occurred while fetching contact form fields: {str(e)}")
        return []

def get_menu_items(query):
    try:
        results = execute_query(query)
        menu_items = []
        for row in results:
            item = {
                "name": row.get("routeName", row.get("linkName")),
                "toRoute": row.get("route", row.get("linkActual"))
            }
            if "linkIcon" in row:
                item["icon"] = row["linkIcon"]
            menu_items.append(item)
        return menu_items
    except Exception as e:
        logging.error(f"An error occurred while fetching menu items: {str(e)}")
        return []

def get_data():
    return {
        "main": {
            "menu_items": get_menu_items(mainQuery),
            "social_menu_items": get_menu_items(socialQuery),
            "contact_form_fields": get_contact_form_fields()
        },
        "in_project": {
            "menu_items": get_menu_items(projectQuery),
            "social_menu_items": get_menu_items(socialQuery),
            "contact_form_fields": get_contact_form_fields()
        },
        "edu": {
            "menu_items": get_menu_items(eduQuery),
            "social_menu_items": get_menu_items(socialQuery),
            "contact_form_fields": get_contact_form_fields()
        },
        "in_edu": {
            "menu_items": get_menu_items(inPEduQuery),
            "social_menu_items": get_menu_items(socialQuery),
            "course_data": execute_query(courseData),
            "contact_form_fields": get_contact_form_fields()
        },
        "in_edu_project": {
            "menu_items": get_menu_items(projectQuery),
            "social_menu_items": get_menu_items(socialQuery),
            "course_data": execute_query(courseData),
            "edu_project": execute_query(inPQuery),
            "contact_form_fields": get_contact_form_fields()
        },
        "in_personal_project": {
            "menu_items": execute_query(pItemQuery),
            "social_menu_items": get_menu_items(socialQuery),
            "personal_project": execute_query(pItemQuery),
            "contact_form_fields": get_contact_form_fields()
        }
    }

