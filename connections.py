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
    conn = connect_to_db()
    try:
        with conn.cursor() as cur:
            cur.execute(query, params)
            results = cur.fetchall()
        return results
    finally:
        conn.close()

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
    try:
        results = execute_query(contactQuery)
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
                item["name"] = row["linkName"]
                item["link"] = row["linkActual"]
                item["icon"] = row["linkIcon"]
            menu_items.append(item)
        return menu_items
    except Exception as e:
        logging.error(f"An error occurred while fetching menu items: {str(e)}")
        return []

def get_data():
    return {
        "main": {
            "menu_items": get_menu_items(inMain),
            "social_menu_items": get_menu_items(socialQuery),
            "contact_form_fields": get_contact_form_fields()
        },
        "project": {
            "menu_items": get_menu_items(inProject),
            "allProjects": execute_query(allProjectDataQuery),
        },
        "edu": {
            "menu_items": get_menu_items(inEdu),
            "eduProjects": execute_query(eduInProgress),
            "personalProjects": execute_query(personalProjectDataQuery),
            "otherEduProjects": execute_query(otherEduProjectDataQuery),
            "eduProjects": execute_query(eduInProgress),
            "eduProjectsPast": execute_query(eduProjectDataQuery),
            "course_data": execute_query(courseData),
        },
        "work": {
            "menu_items": get_menu_items(inWork),
            "social_menu_items": get_menu_items(socialQuery),
            "contact_form_fields": get_contact_form_fields(),
            "work": execute_query(jobQuery)
        }
    }
    
def get_test(): 
        return execute_query(allProjectDataQuery)

if __name__ == "__main__":
    data = get_test()
    print(data)

