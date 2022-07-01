import sqlite3, datetime
from flask import *
from resources.modules.ylearnmodules import *

app = Flask(__name__)
app.secret_key = "edutechhasasecretS"


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
<<<<<<< HEAD
        return render_template("ParentDashboard/dash.html")
=======
        return render_template("Parentdashboard/dash.html")
>>>>>>> 32c14ce81bc4cfb74fad3cee0d467de81b694a57
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
    return sendMessage_(request.args.get('method'), request.args.get('sender'), request.args.get('receiver'), request.args.get('message'))

@app.route('/studentlogin')
def studentLogin():
    return studentLogin_(request)



# flask debug mode
if __name__ == "__main__":
    app.run(debug=True)


