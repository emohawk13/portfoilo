from flask import Flask, render_template
from flask_mysqldb import MySQL
from connections import connect_db, get_social_menu_items

app = Flask(__name__)
app.config.from_pyfile('config.py')
mysql = MySQL(app)

@app.route('/')
def index():
    mainMenu_items = ['Home', 'About', 'Services']
    socialMenu_items = get_social_menu_items()
    return render_template('index.html', mainMenu_items=mainMenu_items, socialMenu_items=socialMenu_items)


if __name__ == '__main__':
    with app.app_context():
        connect_db(app)  # Pass the app object as an argument to connect_db()
    app.run(debug=True)


