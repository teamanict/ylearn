from resources.modules.ylearnmodules import *

def study_(subject, classid):
    subject = request.args.get('subject')
    classid = int(request.args.get('class'))

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