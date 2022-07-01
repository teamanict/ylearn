import sqlite3, datetime
from flask import *
import resources.modules.users as users

# load models/verify.py
from resources.modules.ylearnmodules import *

app = Flask(__name__)
app.secret_key = "edutechhasasecretS"

con = sqlite3.connect('resources/databank/users/db.db3',
                      check_same_thread=False)
con.row_factory = dict_factory
cur = con.cursor()


@app.route('/')
def index():
    print(session)
    return render_template("index.html")

@app.route('/a/<path>')
def subpath(path):
    return subPathsOfA(path)

@app.route('/dashboard')
def dashboard():
    return render_template('/ParentDashboard/dash.html')

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
    return signup_(cur=cur, request=request)

#cur.execute(''' ''')

@app.route('/login', methods=['GET', 'POST'])
def login():
    account_type = request.args.get('as'); username = request.form.get("username"); passkey  =  request.form.get("password")
    return users.login(cur=cur, account_type=account_type, username=username, passkey=passkey)

# flask debug mode
if __name__ == "__main__":
    app.run(debug=True)


