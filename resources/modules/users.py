from flask import *
import resources.modules.database as db

def login_(account_type=None, username=None, passkey=None):
    #Return login forms
    if request.method == "GET":
        return render_template("/landing website/pages-login.html")

    #Authicate user
    elif request.method == "POST":

        #Parent Account
         if account_type == "parent":
            '''SQL LOGIN WITH USERNAME AND PASSWORD THEN FETCH ROWS FROM DATABASE'''
            user = db.runDBQuery(db.users_db, f'SELECT * FROM parents WHERE Email="{username}" AND Pass="{passkey}";')
            if len(user) == 1:
                # Store Student info in session cookies
                session['name'] = user[0]['Name']; session['user'] = user[0]['Email']
                return redirect(url_for('dashboard') + '?for=parent')
            else:
                return "fail"
        #Student Account
         elif account_type == "student":
            user = db.runDBQuery(db.users_db, f'SELECT * FROM children WHERE Username="{username}" AND Pass="{passkey}";')
            if len(user) == 1:
                # Store Student info in session cookies
                session['name'] = user[0]['Name']; session['user'] = user[0]['Username']
                return redirect(url_for('dashboard') + '?for=student')
            else:
                return "fail"

        #Account type not specified
         else:
            return "Account type not specified" 

def signup_(request=None):
    #Return signup forms
    if request.method == "GET": 
        return render_template("pages-register.html")

    #Signup user
    elif request.method == "POST":
        account_type = request.form['as']
        #Parent Account
        if account_type == "parent":
            #SQL SIGNUP WITH USERNAME AND PASSWORD THEN STORE USER IN DATABASE'''

            # Get the user submitted form data
            email = request.form.get("email"); fullname = request.form.get("name"); passkey = request.form.get("password")
            # Store data in database
            db.runDBQuery(db.users_db, f'INSERT INTO parents ("Email", "Name", "Children", "Pass") VALUES ("{email}","{fullname}", "[]", "{passkey}");')
            return "Success"

        #Student Account
        elif account_type == "student":
            #SQL SIGNUP WITH USERNAME AND PASSWORD THEN STORE USER IN DATABASE'''

            # Get the form submitted data
             classid = request.form.get("class");
             username = request.form.get("username"); 
             passkey = request.form.get("password"); 
             gender=request.form.get('gender')
             dob = request.form.get("dob")
             parentid = session[username] 
             
             db.runDBQuery(db.users_db, f'INSERT INTO children ("Username", "Name", "Class", "DOB", "Gender", "Parent") VALUES' f' ("{username}","{fullname}", "{classid}", "DOB", "{gender}", "{parentid}");')
             return "Success"

        #Account type not specified
        else:
            return "Account type not specified"

# Student login from Parent's Dashboard
def studentLogin_(request):
    # Get children registered under parent account
    childrenUnderParent = db.runDBQuery(db.users_db, f'''SELECT children FROM parents WHERE Username="{session['username']}";''')[0]['Children']
    childrenUnderParent = json.loads(childrenUnderParent)
     
    # Find if child is registered under parent
    if request.args.get('studentID') in childrenUnderParent:
        # Store Student info in session cookies
        session['user'] = request.args.get('studentId')
        session['Name'] = db.runDBQuery(db.users_db, f'''SELECT Name FROM children WHERE Username="{session['user']}";''')[0]['Name']
        return redirect(url_for('dashboard') + '?for=student')
    else:
        return "Error while logging in your child. Try agin in a while."


def sendMessage_(method, sender, receiver, message):
    if method == 'send':
        # Store Message in database
        sql_query = f'INSERT INTO chats (sender, receiver, message) VALUES ("{sender}", "{receiver}", "{message}");'
        db.runDBQuery(db.users_db, sql_query)
        return "Success"

    elif method == 'get':
        # Get Messages/Chat History from database
        sql_query = f'SELECT * FROM chats WHERE (sender="{sender}" AND receiver="{receiver}") OR (sender="{receiver}" AND receiver="{sender}");'
        messages = db.runDBQuery(db.users_db, sql_query)
        return render_template('Chat/index.html', messages=messages, sender=sender, receiver=receiver)

    


