from flask import *
def login(cur=None, account_type=None, username=None, passkey=None):
    #Return login forms
    if request.method == "GET":
        return render_template("/landing website/pages-login.html")

    #Authicate user
    elif request.method == "POST":

        #Parent Account
         if account_type == "parent":
            '''SQL LOGIN WITH USERNAME AND PASSWORD THEN FETCH ROWS FROM DATABASE'''
            cur.execute(f'SELECT * FROM parents WHERE Username="{username}" AND Pass="{passkey}";')
            user = cur.fetchall()
            if len(user) == 1:
                print(user)
                session['username'] = user[0]['Username']
                session['name'] = user[0]['Name']
                return render_template("/parent's dashboard/dash.html")
            else:
                return "fail"
        #Student Account
         elif account_type == "student":
            cur.execute(f'SELECT * FROM children WHERE Username="{username}" AND Pass="{passkey}";')
            user = cur.fetchall()
            if len(user) == 1:
                session['user'] = user[0]['Username']
                return "success"
            else:
                return "fail"
                
        #Account type not specified
         else:
            return "Account type not specified" 

def signup_(cur=None, request=None):
    #Return signup forms
    if request.method == "GET": 
        return render_template("pages-register.html")

    #Signup user
    elif request.method == "POST":

        #Parent Account
         if account_type == "parent":
            #SQL SIGNUP WITH USERNAME AND PASSWORD THEN STORE USER IN DATABASE'''

            # Get thew user submitted form data
            username = request.form.get("email"); fullname = request.form.get("name"); passkey = request.form.get("password")
            # Store data in database
            cur.execute(f'INSERT INTO parents ("Username", "Name", "Email", "Children", "Pass") VALUES ("{username}","{fullname}", "fwack.rod", "[]", "{passkey}");')
            print(con.commit())
            return "Success"

        #Student Account
         elif account_type == "student":
            #SQL SIGNUP WITH USERNAME AND PASSWORD THEN STORE USER IN DATABASE'''

            # Get thew user submitted form data
            #classid = request.form.get("class")
            # #dob = request.form.get("DOB")#
            # gender = request.form.get("gender")
            # parentid = request.form.get("parentid") 

            cur.execute(f'INSERT INTO children ("Username", "Name", "Class", "DOB", "Gender", "Parent") VALUES' f' ("{username}","{fullname}", "{classid}", "DOB", "{gender}", "{parentid}");')
            print(con.commit())
            return "Success"

        #Account type not specified
         else:
            return "Account type not specified"

