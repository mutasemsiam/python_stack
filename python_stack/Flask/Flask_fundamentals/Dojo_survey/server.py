from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def display_form():
    name_form = request.form['name']
    email_form = request.form['email']
    password_form = request.form['password']
    address_form = request.form['address']
    city_form = request.form['city']
    language_form = request.form['language']
    comment_form = request.form['comment']
    check_form = request.form['check']


    return render_template("show.html", name_r = name_form, email_r = email_form, password_r = password_form,
    address_r = address_form, city_r = city_form, language_r = language_form, comment_r = comment_form, 
    check_r = check_form)

if __name__ == "__main__":
    app.run(debug=True)
