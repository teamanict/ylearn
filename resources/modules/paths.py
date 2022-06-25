from flask import *
def subPathsOfA(path):
    if path == 'pricing':
        return render_template('pricing.html')
        #about.html
    elif path == 'about':
        return render_template('about.html')
        #contact.html
    elif path == 'contact':
        return render_template('contact.html')
        #courses.html
    elif path == 'courses':
        return render_template('courses.html')
        #blog.html
    elif path == 'teacher':
        return render_template('teacher.html')
        #login.html