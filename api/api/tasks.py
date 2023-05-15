from django.core.mail import send_mail

from api.celery import app


@app.task
def put_email(email):
    send_mail('Warning', 'Your status was changed!', 'mail@mailto.plus', [email])
    print('Hello World')
