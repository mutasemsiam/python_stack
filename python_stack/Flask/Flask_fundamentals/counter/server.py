from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'This is a secret key that you shoud NOT know'

@app.route('/')
def counter():
    if "count" not in session:
        session["count"] = 0
    else:    
        session["count"] += 1
    
    return render_template("counter.html")

@app.route("/count", methods=["POST"])
def count_by_2():
    session["count"] += 1
   
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset_count():
    session.clear()
   
    return redirect("/")
@app.route("/destroy_session")
def destroy():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)