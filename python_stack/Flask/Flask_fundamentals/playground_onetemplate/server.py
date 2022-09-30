from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play_boxes():
    
    return render_template('index.html', times = 3, y = "first_page")

@app.route('/play/<x>')
def play_boxes_by_num(x):
    
    return render_template('index.html', times = int(x), paint = "skyblue", y = "second_page")

@app.route('/play/<x>/<color>')
def play_boxes_by_num_painted(x, color):
    
    return render_template('index.html', times = int(x), paint = color, y = "third_page")

@app.errorhandler(404)
def page_not_found(e):
    return "page not found"

if __name__ == "__main__":
    app.run(debug=True)
