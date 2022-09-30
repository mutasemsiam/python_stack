from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display_checker():
    return render_template("index.html", a = 8, b = 8, paint = "red", paint2 = "black")

@app.route('/4')
def display_a_checker():
    return render_template("index.html", a = 8, b = 4, paint = "red", paint2 = "black")

@app.route('/<x>/<y>')
def display_your_checker(x, y):
    return render_template("index.html", a = int(x), b = int(y), paint = "red", paint2 = "black")

@app.route('/<x>/<y>/<color>/<color2>')
def display_colored_checker(x, y, color, color2):
    return render_template("index.html", a = int(x), b = int(y), paint = color, paint2 = color2)

@app.errorhandler(404)
def handle_bad_request(e):
    return "URL is invalid. Please enter a valid URL!"


if __name__ =="__main__":
    app.run(debug=True)
