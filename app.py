from flask import Flask, render_template, request
import config
from connections import (
    main_menu,
    in_edu,
    in_project,
    in_edu_project,
    in_personal_project,
    insert_contact,
    get_personal_project_items,
    get_edu_project_items,
    get_courseData,
)

app = Flask(__name__)
app.config.from_pyfile("config.py")


def render_page(template_name, menu_function, **kwargs):
    menu_data = menu_function()
    mainMenu_items = menu_data.get("main_menu_items", [])
    socialMenu_items = menu_data.get("social_menu_items", [])
    comboMenu = menu_data.get("comboMenu", [])
    contact_form_fields = menu_data.get("contact_form_fields", [])

    return render_template(
        template_name,
        mainMenu_items=mainMenu_items,
        socialMenu_items=socialMenu_items,
        comboMenu=comboMenu,
        contact_form_fields=contact_form_fields,
        **kwargs
    )



@app.route("/")
@app.route("/goHome")
def home():
    return render_page("index.html", main_menu)

@app.route("/contact_submitted", methods=["POST"])
def contact_submitted():
    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    email = request.form.get("contactEmail")
    about = request.form.get("tellMeAboutYou")

    try:
        insert_contact(first_name, last_name, email, about, True)
    except:
        return "There was an error submitting your data, please try again.", 500

    return render_page("contact.html", main_menu)

@app.route("/projects")
def projects():
    return render_page("projects.html", main_menu, in_project)

@app.route("/edu")
def edu():
    return render_page("edu.html", main_menu, in_edu)

@app.route("/projectBlog")
def projectBlog():
    return render_page("projectBlog.html", main_menu)

@app.route("/eduProjects")
def eduProjects():
    course_data = get_courseData()
    edu_items = get_edu_project_items()
    return render_page(
        "eduProjects.html", main_menu, in_edu_project, courseData=course_data, eduItems=edu_items
    )

@app.route("/takenCourses")
def takenCourses():
    course_data = get_courseData()
    edu_items = get_edu_project_items()
    return render_page(
        "takenCourses.html",main_menu, in_edu_project, courseData=course_data, eduItems=edu_items
    )

@app.route("/personalProjects", methods=["GET", "POST"])
def personalProjects():
    message = "personal projects page,"
    if request.method == "POST":
        message = request.form.get("message")
    projects = get_personal_project_items()
    return render_page(
        "personalProjects.html", main_menu, in_edu_project, message=message, projects=projects
    )

@app.route("/test", methods=["GET", "POST"])
def test():
    message = "personal projects page,"
    if request.method == "POST":
        message = request.form.get("message")
    projects = get_personal_project_items()
    return render_page("test.html", main_menu, in_edu_project, message=message, projects=projects)

if __name__ == "__main__":
    app.run(debug=True)
