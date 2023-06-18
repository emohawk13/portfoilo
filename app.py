from flask import Flask, render_template
from connections import connect_db, get_social_menu_items

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
        {'name': 'Contact', 'url': '/home', 'class': 'contact-button'}
    ]
    socialMenu_items = get_social_menu_items()
    return render_template('index.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items)


if __name__ == '__main__':
    app.run(debug=True)
