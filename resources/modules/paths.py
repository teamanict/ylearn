from flask import *
def subPathsOfA(path):
    if path == 'pricing':
        return send_file("templates/pricing.html")
    #about.html
    elif path == 'about':
        return send_file('templates/about.html')
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
    else: return "SOwi"