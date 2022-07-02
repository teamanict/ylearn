import sqlite3, datetime
from flask import *
from flask_cors import CORS
from resources.modules.ylearnmodules import *

app = Flask(__name__)
app.secret_key = "edutechhasasecretS"
CORS(app)


@app.route('/')
def index():
    print(session)
    return render_template("index.html")

@app.route('/a/<path>')
def subpath(path):
    return subPathsOfA(path)

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        children = getAllChildren(session.get('user'))
        return render_template("ParentDashboard/dash.html", children=children)
    else:
        return redirect(url_for('login'))

@app.route("/signupstudent")
def signupstudent():
    return render_template("Landing Website/pages-register.html")


@app.route("/pay")
def pay():
    return render_template("Landing Website/payment.html")


@app.route('/verify')
def verify():
    return verify_trans(request.args.get('transaction_id'))


@app.route("/signup", methods=["GET","POST"])
def signup():
    return signup_(request=request)

#cur.execute(''' ''')

@app.route('/login', methods=['GET', 'POST'])
def login():
    account_type = request.args.get('as'); username = request.form.get("username"); passkey  =  request.form.get("password")
    return login_(account_type=account_type, username=username, passkey=passkey)

@app.route('/sendMessage')
def sendMessage():
    return sendMessage_(request.args.get('method'), session['user'], request.args.get('receiver'), request.args.get('message'))

@app.route('/studentlogin')
def studentLogin():
    return studentLogin_(request)

@app.route('/changepassword')
def changePassword():
    return changePassword_(request.args.get('oldpass'), request.args.get('newpass'))

@app.route('/chat')
def chat():
    print(session['user'])
    return chat_(session['user'], request.args.get('receiver'), request.args.get('page'))

# flask debug mode
if __name__ == "__main__":
    app.run(debug=True)
    app.host = '0.0.0.0'


