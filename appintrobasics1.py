from flask import Flask

#from flask import Flask — imports the Flask class from the Flask package.
#app = Flask(__name__) — creates your Flask application. __name__ helps Flask locate resources belonging to your application.
#@app.route('/') — maps the URL / to the function directly below it.
#def home(): — function executed when someone visits /.
#return "Hello, Flask!" — Flask sends this text back to the browser as the HTTP response.
#if __name__ == '__main__': — runs the server only when you execute this file directly, e.g. python app.py.
#app.run(debug=True) — starts Flask's development server with debugging/reloading features enabled.
#Security: debug=True is for development only. Don't enable Flask's debugger in production.
#The most important concept here is: route → function → response.

#basic Flask app setup
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)

