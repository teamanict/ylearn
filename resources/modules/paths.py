from flask import *
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
        return render_template('ParentDashboard/users-profile.html')
    # Enroll child
    elif path == 'enrollchild':
        return render_template('ParentDashboard/Enroll child.html')
    # Contact form
    elif path == 'contactform':
        return render_template('ParentDashboard/pages-contact.html')
    # Subscription 
    elif path == 'subscription':
        return render_template('ParentDashboard/Subscription.html')
        
    elif path == 'signout':
        session.clear()
        return redirect(url_for('index'))
    else: return "SOwi"