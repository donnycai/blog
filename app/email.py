from flask_mail import Message
from app import mail, app
from flask import render_template
from threading import Thread
import os


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(app, msg)).start()


def send_password_reset_email(user):
    print(app.config['ADMINS'])
    print(os.environ.get('ADMINS'))
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               sender=app.config['ADMINS'],
               recipients=[user.email],
               text_body=render_template(
                   'email/reset_password.text', token=token, user=user),
               html_body=render_template(
                   'email/reset_password.html', token=token, user=user))
