from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import urllib.request
import socket
socket.getaddrinfo('localhost', 25)


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/dhairya'

db = SQLAlchemy(app)
#class Posts(db.Model):
    # sno=db.Column(db.Integer, primary_key=True)
    # name=db.Column(db.String(80),  nullable=False)
    # eaddress=db.Column(db.String(80),  nullable=False)
    # mno=db.Column(db.String(20),  nullable=False)
    # msg=db.Column(db.String(120), nullable=False)


import urllib.request
"""@app.route("/")
def hello():
    return "hello"""
app.config.update(
 MAIL_SERVER='smtp.gmail.com',
 MAIL_PORT= '465',
 MAIL_USE_SSL=True,
 MAIL_USERNAME='my4030070@gmail.com',
 MAIL_PASSWORD='Business@1311'
 #MAIL_USE_TLS=False

 )
mail=Mail(app)

"""@app.route("/blog.html")

def blog():
    return render_template('blog.html')"""
@app.route("/contact.html", methods=['GET','POST'])
def contact():
    if (request.method == 'POST'):
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        mno = request.form.get('mno')
        msg = request.form.get('msg')

        # entry = Posts(fname=fname,lname=lname,email=email,  mno=mno, msg=msg)
        db.session.add(entry)
        db.session.commit()
        # mail.send_message("New Message From" + name ,sender=email,recipients=['my4030070@gmail.com'],body=msg + "\n" + mno)



    return render_template('contact.html')

@app.route("/about.html")
def about():
    return render_template('about.html')
# @app.route("/contact.html")
# def contact():
#     return render_template('contact.html')
@app.route("/gallery.html")
def gallery():
    return render_template('gallery.html')
@app.route("/wedding.html")
def wedding():
    return render_template('wedding.html')
@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')
@app.route("/services.html")
def services():
    return render_template('services.html')
@app.route("/baby.html")
def baby():
    return render_template('baby.html')
@app.route("/pre.html")
def pre():
    return render_template('pre.html')
@app.route("/album.html")
def album():
    return render_template('album.html')
@app.route("/almain.html")
def almain():
    return render_template('almain.html')
@app.route("/cinema.html")
def cinema():
    return render_template('cinema.html')
@app.route("/maternity.html")
def maternity():
    return render_template('maternity.html')
@app.route("/two.html")
def two():
    return render_template('two.html')
@app.route("/three.html")
def three():
    return render_template('three.html')
@app.route("/four.html")
def four():
    return render_template('four.html')
@app.route("/five.html")
def five():
    return render_template('five.html')
@app.route("/six.html")
def six():
    return render_template('six.html')
@app.route("/seven.html")
def seven():
    return render_template('seven.html')






if __name__ == '__main__':
    app.run(debug=True)