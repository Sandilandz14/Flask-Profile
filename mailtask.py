from flask import Flask, render_template


from flask_mail import Mail, Message

app = Flask(__name__)

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

# @app.route('/')
# def index():
#     return render_template("mail.html")
#
#
# @app.route('/send-email/', methods=["POST"])
# def send_email():
#     return "Email Sent."
#
# if __name__ == "__main__":
#     app.run(debug=True)
