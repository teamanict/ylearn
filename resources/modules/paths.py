from flask import *
from resources.modules.ylearnmodules import *

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
    # Userprofile
    elif path == 'userprofile':
        if 'user' in session:
            children = getAllChildren(session.get('user'))
            return render_template("ParentDashboard/users-profile.html", children=children)
        else:
            return redirect(url_for('login'))
    # Enroll child
    elif path == 'enrollchild':
        if 'user' in session:
            children = getAllChildren(session.get('user'))
            return render_template("ParentDashboard/Enroll Child.html", children=children)
        else:
            return redirect(url_for('login'))
    # Contact form
    elif path == 'contactform':
        if 'user' in session:
            children = getAllChildren(session.get('user'))
            return render_template("ParentDashboard/pages-contact.html", children=children)
        else:
            return redirect(url_for('login'))
    # Subscription
    elif path == 'subscription':
        if 'user' in session:
            children = getAllChildren(session.get('user'))
            return render_template("ParentDashboard/Subscription.html", children=children)
        else:
            return redirect(url_for('login'))

    elif path == 'signout':
        session.clear()
        return redirect(url_for('index'))
    else: 
        return render_template('/ParentDashboard/pages-error-404.html')