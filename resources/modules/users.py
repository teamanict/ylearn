from flask import *
def login_(account_type=None, username=None, passkey=None):
    #Return login forms
    if request.method == "GET": 
        return render_template("pages-login.html")

    #Authicate user
    elif request.method == "POST":

        #Parent Account
         if account_type == "parent":
            '''SQL LOGIN WITH USERNAME AND PASSWORD THEN FETCH ROWS FROM DATABASE'''
            cur.execute(f'SELECT * FROM parents WHERE Username="{username}" AND Pass="{passkey}";')
            user = cur.fetchall()
            if len(user) == 1:
                return "success"
            else:
                return "fail"
        #Student Account
         elif account_type == "student":
            cur.execute(
            f'SELECT * FROM children WHERE Username="{username}" AND Pass="{passkey}";')
            user = cur.fetchall()
            if len(user) == 1:
                return "success"
            else:
                return "fail"
                
        #Account type not specified
         else:
            return "Account type not specified" 
