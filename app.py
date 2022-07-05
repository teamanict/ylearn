import sqlite3, datetime
from flask import *
from resources.modules.ylearnmodules import *

app = Flask(__name__)
app.secret_key = "edutechhasasecretS"

# admin/exercise_FORM
@app.route('/exerciseform')
def exercise_FORM():
    return render_template('admin/exercise_form.html')


@app.route('/')
def index():
    print(session)
    return render_template("index.html")

@app.route('/a/<path>')
def subpath(path):
    return subPathsOfA(path)

@app.route('/u/<path>')
def userpath(path):
    if 'user' in session:
        return subPathsOfUser(path)
    else:
        return redirect(url_for('login') + '?as=parent')
   

@app.route('/dashboard')
def dashboard():
    account_type = request.args.get('for')
    print(session)
    if 'user' in session and account_type == 'parent' and session['usertype'] == 'parent':
        children = getAllChildren(session.get('user'))
        return render_template("ParentDashboard/dash.html", children=children)
    elif 'user' in session and account_type == 'student' and session['usertype'] == 'student':
        child = getChild(session.get('user'))
        print(child)
        return render_template("ChildDashboard/childdash.html", child=child)
    else: 
        return redirect(f'/login?as={account_type}')
  
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
    account_type = request.args.get('as'); userfromdash=request.args.get('username'); username = request.form.get("username"); passkey  =  request.form.get("password")
    return login_(account_type=account_type, username=username, userfromdash=userfromdash, passkey=passkey)

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
    if 'user' in session and session.get('usertype') == 'parent':
        return chat_(session['user'])
    else:
        return redirect('/login?as=parent')


@app.route('/storeFeedback', methods=['POST', 'GET'])
def storeFeedback():
    return storeFeedback_(request)

@app.route
('/study')
def study():
    subject = request.args.get('subject'); classid=request.args.get('class');
    return study_(subject, classid)

@app.route('/bookshopapi', methods=['POST', 'GET'])
def bookshopapi():
      return storeInventory_(request)


# flask debug mode
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)


