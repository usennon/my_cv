from flask import Flask, render_template, request, redirect, url_for
from forms import SendForm
from flask_bootstrap import Bootstrap
import smtplib
from email.message import EmailMessage

my_email = "progmvl@gmail.com"
PASSWORD = "N)SC#1rMLnKb8(Z"

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'asdadwqqkfelwl2k13k;m;sae2;1r'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/wall')
def blog():
    return render_template('blog.html')


@app.route('/contact-me', methods=['GET', 'POST'])
def contact():
    form = SendForm()
    if request.method == 'POST' and form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        body = request.form.get('body')
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=PASSWORD)
            msg = EmailMessage()
            msg['Subject'] = subject
            msg['From'] = my_email
            msg['To'] = 'usennon@mail.ru'
            msg.set_content(name + '\n' + body + f'\nMy email is {email}')
            connection.send_message(msg)
            return redirect(url_for('contact'))
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run()
