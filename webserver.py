"""
webserver.py

File that is the central location of code for your webserver.
"""

from flask import Flask, render_template

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

@app.route('/contact')
def contact():
	return render_template("contactUs.html")

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