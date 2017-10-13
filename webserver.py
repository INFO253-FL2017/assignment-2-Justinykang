"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template, request
import os
import requests

# Create application, and point static path (where static resources like images, css, and js files are stored) to the
# "static folder"
app = Flask(__name__,static_url_path="/static")

@app.route('/')
def hello_world():
    """
    If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
    returns will be sent to the browser
    """
    return render_template("index.html") # Render the template located in "index.html"

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("aboutUs.html")

@app.route('/contact', methods=['get', 'post'])
def contact():
    name = request.form.get("name")
    message = request.form.get("message")
    subject = request.form.get("subject")
    data = {
        "from": os.environ["INFO253_MAILGUN_FROM_EMAIL"],
        "to": os.environ["INFO253_MAILGUN_TO_EMAIL"],
        "subject": subject,
        "text": message,
    }
    auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])

    r = requests.post(
        "https://api.mailgun.net/v3/{}/messages".format(os.environ["INFO253_MAILGUN_DOMAIN"]),
        auth=auth,
        data=data)

    if r.status_code == requests.codes.ok:
        error = "Hi " + name + ", your message has been sent!"
    else:
        error = "Your email was not sent. Please try again!"

    return render_template("contactUs.html", error=error)

@app.route('/blog/8-experiments-in-motivation')
def page1():
    return render_template("page1.html")

@app.route('/blog/a-mindful-shift-of-focus')
def page2():
    return render_template("page2.html")

@app.route('/blog/how-to-develop-an-awesome-sense-of-direction')
def page3():
    return render_template("page3.html")

@app.route('/blog/training-to-be-a-good-writer')
def page4():
    return render_template("page4.html")

@app.route('/blog/what-productivity-systems-wont-solve')
def page5():
    return render_template("page5.html")




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)