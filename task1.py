from flask import Flask, render_template, url_for, redirect
from flask_mail import Mail, Message
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

mail = Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'stukani100@gmail.com'
app.config['MAIL_PASSWORD'] = 'sandilandz4teen'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'yourID@gmail.com', recipients = ['stukani100@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
# @app.route('/grading/<int:grades>')
# def marks(grades):
#     return render_template('index.html',mark=grades)


if __name__=='__main__':
    app.run(debug=True)
























# from flask import Flask
#
#
# app = Flask(__name__)
#
# @app.route('/Index/<user>')
# def index(user):
#     return "This is my landing page"
#
#
# if __name__=='__main__':
#         app.run(debug=True)
