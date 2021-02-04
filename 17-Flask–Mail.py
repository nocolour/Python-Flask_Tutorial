from flask import Flask
from flask_mail import Mail, Message  # Flask-Mail

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'mail.hwathai.my'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'desmond.phee@hwathai.my'
app.config['MAIL_PASSWORD'] = 'P@SS4392'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)


@app.route("/")
def index():
    msg = Message('Hello', sender='desmond.phee@hwathai.my', recipients=['nocolour@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run(debug=True)
