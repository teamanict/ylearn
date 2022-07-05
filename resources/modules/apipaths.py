from flask import *
from resources.modules.users import *

#=== Subpaths handler ===#
#Sub paths of A
def subPathsOfA(path):
    if path == 'pricing':
        return send_file("templates/Landing Website/pricing.html")
    #about.html
    elif path == 'about':
        return send_file('templates/Landing Website/about.html')
    #contact.html
    elif path == 'contact':
        return render_template('Landing Website/contact.html')
    #courses.html
    elif path == 'courses':
        return render_template('Landing Website/courses.html')
    #blog.html
    elif path == 'teacher':
        return render_template('Landing Website/teacher.html')
    # 404 Page Not Found
    else:
        return render_template('Landing Website/404.html')

#Sub paths of logined in user
def subPathsOfUser(path):

    #User profile
    if path == 'userprofile':
        if session['usertype'] == 'parent':
            return render_template('ParentDashboard/users-profile.html')
        elif session['usertype'] == 'student':
            return render_template('ChildDashboard/users-profile.html', child=getChild(session.get('user')))

    # Enroll child
    elif path == 'enrollchild':
        return render_template("ParentDashboard/Enroll Child.html")
    # Contact form
    elif path == 'contactform':
        return render_template("ParentDashboard/pages-contact.html")
    # Subscription
    elif path == 'subscription':
        children = getAllChildren(session.get('user'))
        return render_template("ParentDashboard/Subscription.html", children=children)
    # Sign out
    elif path == 'signout':
        session.clear()
        return redirect(url_for('index') + '?as=parent')
    # 404 Page Not Found
    else:
        return render_template('/ParentDashboard/pages-error-404.html')
#=== Subpaths handler ===#


def study_(subject, classid):
    print(subject)
    dbpath = '/Lessons/{subject}.db3'
    if subject == 'Math':
        return render_template('ChildDashboard/lesson.html')
    elif subject == 'Eng':
        return render_template('ChildDashboard/english.html')
    elif subject == 'Sst':
        return render_template('ChildDashboard/SocialStudies.html')
    elif subject == 'Sci':
        return render_template('ChildDashboard/science.html')

