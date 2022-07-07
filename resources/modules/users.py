from flask import *
import resources.modules.database as db
from resources.modules.verify import *


def login_(account_type=None, username=None, passkey=None, userfromdash=None):
    if (request.method == "GET"):
        # Login in from parents dashboard
        if account_type == "studentfromdash":
            return studentLogin_(username=userfromdash)
        else:
            # Return login forms
            return render_template("/landing website/pages-login.html")

    # Authenticate user
    elif request.method == "POST":

        # Parent Account
        if account_type == "parent":
            '''SQL LOGIN WITH USERNAME AND PASSWORD THEN FETCH ROWS FROM DATABASE'''
            user = db.runDBQuery(
                db.users_db, f'SELECT * FROM parents WHERE Email="{username}" AND Pass="{passkey}";')
            print(user)
            if len(user) == 1:
                # Store Parent info in session cookies
                session['name'] = user[0]['Name']
                session['user'] = user[0]['Email']
                session['usertype'] = 'parent'
                return redirect(url_for('dashboard') + '?for=parent')
            else:
                return "fail"
        # Student Account
        elif account_type == "student":
            # Get parent id of student
            parent_id = db.runDBQuery(
                db.users_db, f'SELECT Parent FROM children WHERE Username="{username}";')[0]['Parent']
            # Get children registered under parent account

            childrenUnderParent = db.runDBQuery(
                db.users_db, f'SELECT Children FROM parents WHERE Email="{parent_id}" AND Pass="{passkey}";')[0]['Children']
            child = getChild(username)
            if username in childrenUnderParent:
                # Checking Whether child is Subscribed
                if child['IsSubscribed']:
                    # Store Student info in session cookies
                    user = db.runDBQuery(
                        db.users_db, f'SELECT * FROM children WHERE Username="{username}";')
                    # Store Student info in session cookies
                    session['name'] = user[0]['Name']
                    session['user'] = user[0]['Username']
                    session['usertype'] = 'student'
                    return redirect('/dashboard?for=student')
                else:
                    # Inform Parent Child Is not subscribed
                    return render_template('ParentDashboard/Unsubscribed.html')
            else:
                return redirect('/login?as=student')

        # Account type not specified
        else:
            return "Account type not specified"


def signup_(request=None):
    # Return signup forms
    if request.method == "GET":
        return render_template("Landing Website/pages-register.html")

    # Signup user
    elif request.method == "POST":
        account_type = request.args.get('as')
        # Parent Account
        if account_type == "parent":
            # SQL SIGNUP WITH USERNAME AND PASSWORD THEN STORE USER IN DATABASE'''

            # Get the user submitted form data
            email = request.form.get("email")
            fullname = request.form.get("name")
            passkey = request.form.get("password")
            # Store data in database
            db.runDBQuery(
                db.users_db, f'INSERT INTO parents ("Email", "Name", "Children", "Pass") VALUES ("{email}","{fullname}", "[]", "{passkey}");')
            return redirect(url_for('login') + '?for=parent')

        # Student Account
        elif account_type == "student":
            # SQL SIGNUP WITH USERNAME AND PASSWORD THEN STORE USER IN DATABASE'''

            # Get the form submitted data
            dob = request.form.get("dob")
            name = request.form.get('name')
            gender = request.form.get('gender')
            classid = request.form.get('class')
            username = request.form.get('username')
            profile_pic = request.form.get('profile')

            parentid = session.get('user')
            if parentid != None:
             # Add Child to Database
                db.runDBQuery(
                    db.users_db, f'INSERT INTO children ("Username", "Name", "Class", "DOB", "Gender", "Parent", "Profile_Picture", "LastPayment") VALUES' f' ("{username}","{name}", "{classid}", "{dob}", "{gender}", "{parentid}", "{profile_pic}", "2000-01-01");')

             # Add child to parent's registered list
                newChildList = getChildrenIds(parentid)
                newChildList.append(username)
                newChildList = json.dumps(newChildList)
                print(newChildList)
             # Store new child list in sql
                db.runDBQuery(
                    db.users_db, f'''UPDATE parents SET Children='{newChildList}' WHERE Email="{parentid}";''')

                return redirect('/u/subscription')
            else:
                return redirect('/login?as=parent')

        # Account type not specified
        else:
            return "Account type not specified"

# Student login from Parent's Dashboard


def studentLogin_(username=None):
    # Get children registered under parent account
    child = getChild(username)
    childrenUnderParent = getChildrenIds(session.get('user'))

    # Find if child is registered under parent
    if username in childrenUnderParent:
        # Check For Subscription
        if child['IsSubscribed']:
            # Store Student info in session cookies
            session['user'] = username
            session['usertype'] = 'student'
            session['Name'] = db.runDBQuery(
                db.users_db, f'''SELECT Name FROM children WHERE Username="{session['user']}";''')[0]['Name']
            return redirect('dashboard?for=student')
        else:
            # Inform Parent Child is not subscribed
            return render_template('ChildDashboard/Unsubscribed.html')
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
        return json.dumps(messages)


def changePassword_(old_pass, new_pass):
    # Check if old password is correct
    if db.runDBQuery(db.users_db, f'SELECT * FROM parents WHERE Pass="{old_pass}" AND Email="{session["user"]}";')[0]['Pass'] == old_pass:
        # Change password
        db.runDBQuery(
            db.users_db, f'UPDATE parents SET Pass="{new_pass}" WHERE Email="{session["user"]}";')
        return "Success"
    else:
        return "Error"
#=== Children Accounts Api ===#


def getChildrenIds(parentid=None):
    # Get children registered under parent account
    childrenIds = db.runDBQuery(
        db.users_db, f'SELECT Children FROM parents WHERE Email="{parentid}";')[0]['Children']
    childrenIds = json.loads(childrenIds)
    return childrenIds


def getChild(child_id):
    # Get child info from database
    child = db.runDBQuery(
        db.users_db, f'''SELECT * FROM children WHERE Username="{child_id}";''')[0]
    child['IsSubscribed'] = isSubscribed(child_id)
    child['ExpiryDate'] = getSubscriptionExpiryDate(child_id)
    return child


def getAllChildren(parent_id):
    # Get children registered under parent account
    children = []
    childrenIds = getChildrenIds(parent_id)
    print(childrenIds)
    for child_id in childrenIds:
        print("Childt ID", child_id)
        child = getChild(child_id)
        children.append(child)
    return children
#=== End Children Accounts APi ===#


def chat_(sender):
    print(sender)
    # Show Messages/Chat History from database
    #   sql_query = f'SELECT * FROM chats WHERE (sender="{sender}" AND receiver="{receiver}") OR (sender="{receiver}" AND receiver="{sender}");'
    #  messages = db.runDBQuery(db.users_db, sql_query)
    return render_template('Chat/chat.html', sender=sender)


def getLessonData(subject, dbpath, classid):
    if classid <= 4:
        classid = '4'
    elif classid <= 7:
        classid = '5'

    if subject == 'Math':
        dbpath = '/lessons/math.db3'
    elif subject == 'Eng':
        dbpath = '/lessons/english.db3'
    elif subject == 'Sst':
        dbpath = '/lessons/sst.db3'
    elif subject == 'Sci':
        dbpath = '/lessons/science.db3'
    
    lessons = getLessonData(subject, dbpath, classid)
    return render_template('ChildDashboard/lesson.html', lessons = lessons, subject=subject, child = getChild(session.get('user')))
    # Get lesson data from database
    lessonData = db.runDBQuery(dbpath, f'SELECT * FROM P{classid};')
    return lessonData
