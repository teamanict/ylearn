from flask import *
import resources.modules.database as db


def storeFeedback_(request):
    # Get Data from all contact forms
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('Subject')
    message = request.form.get('message')
    db.runDBQuery(
        db.users_db, f'INSERT INTO FeedBack ("email", "Subject", "message", "Name") VALUES' f' ("{email}", "{subject}", "{message}", "{name}");')

    return render_template('/ParentDashboard/success.html')

