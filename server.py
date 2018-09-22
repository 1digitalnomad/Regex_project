from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app =  Flask(__name__)
app.secret_key = "This is top secret."

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    if len(request.form['email']) < 1:
        flash("Email can not be blank.")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("This is not a valid email. Try again.")

    else:
        flash("Success! Way to go!")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)