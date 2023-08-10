#   projectConnection
import datetime
import pymysql
import config as config
import logging
from flask import current_app
from config import *


def execute_query(query, params=None):
    conn = None
    try:
        conn = pymysql.connect(
            host=config.MYSQL_HOST,
            port=config.MYSQL_PORT,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            db=config.MYSQL_DB,
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
        
        with conn.cursor() as cur:
            if params:
                cur.execute(query, params)
            else:
                cur.execute(query)
            
            results = cur.fetchall()
        
        return results

    except Exception as e:
        logging.error(f"An error occurred while executing the query: {str(e)}")
        return []
    finally:
        if conn:
            conn.close()

def get_courseData(course_class_type, course_progress):
    query = courseData + " WHERE courseClassType = %s AND courseProgress = %s ORDER BY courseId"
    results = execute_query(query, (course_class_type, course_progress))
    course_data = []
    for row in results:
        subTitle = row["projectName"]
        projectDisc = row["projectDisc"]
        course_data.append({"subTitle": subTitle, "projectDisc": projectDisc})
    
    return course_data

def get_links():
    results = execute_query(allLinks)
    return results
    
def insert_contact(first_name, last_name, email, about, pressed):
    current_time = datetime.datetime.now()
    insert_query = insertQuery
    execute_query(insert_query, (first_name, last_name, email, about, current_time), fetch_results=False)    

def get_contact_form_fields():
    results = execute_query(contQuery)
    return results

def get_social_menu_items():
    results = execute_query(socialQuery)
    return results

def get_main_menu_items():
    results = execute_query(mainQuery)
    return results

def get_edu_menu_items():
    results = execute_query(eduQuery)
    return results

def get_in_edu_menu_items():
    results = execute_query(inPEduQuery)
    return results

def get_in_project_menu_items():
    results = execute_query(projectQuery)
    return results

def get_personal_project_menu_items():
    results = execute_query(inPMenuQuery)
    return results

def get_personal_project_items():
    results = execute_query(pItemQuery)
    return results

def get_edu_project_items():
    results = execute_query(eduItemQuery)
    return results


def main_menu():
    main_menu_items = get_main_menu_items()
    social_menu_items = get_social_menu_items()
    contact_form_fields = get_contact_form_fields()
    comboMenu = main_menu_items + social_menu_items
    return {
        "main_menu_items": main_menu_items,
        "social_menu_items": social_menu_items,
        "comboMenu": comboMenu,
        "contact_form_fields": contact_form_fields,
    }

def prepare_data(project_func, additional_data_func=None):
    project_items = project_func()
    social_menu_items = get_social_menu_items()
    contact_form_fields = get_contact_form_fields()
    comboMenu = project_items + social_menu_items

    data = {
        "project_items": project_items,
        "social_menu_items": social_menu_items,
        "comboMenu": comboMenu,
        "contact_form_fields": contact_form_fields
    }

    if additional_data_func:
        data.update(additional_data_func())

    return data

def in_edu():
    return prepare_data(get_edu_menu_items)

def in_project():
    return prepare_data(get_in_project_menu_items)

def in_edu_project():
    return prepare_data(get_in_edu_menu_items, get_courseData)

def in_personal_project():
    return prepare_data(get_personal_project_menu_items)

print(social_menu_items())