import sqlite3
from flask import *

#load models/verify.py
from verify import *

'''
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:/Users/Student/Desktop/edutech/db.db3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
'''
app=Flask(__name__)
app.secret_key = "edutechhasasecretS"

con = sqlite3.connect('db.db3',  check_same_thread=False)
cur = con.cursor()

#1st Merge
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/teacher')
def teacher():
    return render_template('teacher.html')


@app.route("/static/<path:path>")
def static_dir(path):
    print(path)
    return send_from_directory("templates/ylearn2", path)

'''@app.route("/")
def index():
    print(session)
    return render_template('ylearn2/index.html')'''

@app.route("/signupstudent")
def signupstudent():
    return render_template("ylearn2/signupstudent.html")

@app.route("/pay")
def pay():
    return render_template("payment.html")

@app.route('/verify')
def verify():
    return verify_trans(request.args.get('transaction_id'))



@app.route("/signup", methods=["POST"])
def signup():
    #Get thew user submitted form data
    username = request.form.get("username")
    fullname = request.form.get("yrname")
    email    =    request.form.get("email")
    passkey  =  request.form.get("psw")

    classid = request.form.get("class")
    dob = request.form.get("DOB")
    gender = request.form.get("gender")
    parentid = request.form.get("parentid")

    #store data in database
    #cur.execute(f'INSERT INTO parents ("Username", "Name", "Email", "Children", "Pass") VALUES ("{username}","{fullname}", "{email}", "[]", "{passkey}");')

    cur.execute(f'INSERT INTO children ("Username", "Name", "Class", "DOB", "Gender", "Parent") VALUES'
                f' ("{username}","{fullname}", "{classid}", "DOB", "{gender}", "{parentid}");')

    con.commit()
    return "success"

#cur.execute(''' ''')

def login(username, passkey):
    #username = request.form.get("username")
    #passkey  =  request.form.get("password")
     
    '''SQL LOGIN WITH USERNAME AND PASSWORD THEN FETCH ROWS FROM DATABASE'''
    cur.execute(f'SELECT * FROM parents WHERE Username="{username}" AND Pass="{passkey}";')
    user = cur.fetchall()
    if len(user) == 1:
        return "success"
    else:
        return "fail"

#flask debug mode
if __name__ == "__main__":
    app.run(debug=True)

    




