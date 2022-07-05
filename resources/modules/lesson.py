import resources.modules.database as db
from flask import *

def addLesson():

    Topic = request.form.get('Topic')
    Subject = request.form.get('Subject')
    Class = request.form.get('Class')
    Description = request.form.get('description')
    Video = request.form.get('Video')

    if Class == '7':
        
        lesson = db.lesson_db(f'')