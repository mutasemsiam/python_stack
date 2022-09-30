from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/users')
def display_table():
    users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template("index.html", names = users)

@app.errorhandler(404)
def handle_bad_request(e):
    return "Unvalid URL. Please enter a valid URL"

if __name__=="__main__":
    app.run(debug=True)