from flask import Flask, redirect,render_template, request,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#need to swith to python terimanl to install db packages -- python3
#run these commands in the terminal to create the database:
#python3
#from app_db5 import app,db
#with app.app_context():
#...     db.create_all() --Which Flask application and database configuration am I working with?    
#>>> exit()
#(env) shravanibadadha@Shravanis-MacBook-Pro PythonFlask % ls instance
#this will list the contents of the instance folder, which should include the created database file

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) #need to store user content(nullable=false)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    #need to return a string representation of the user object present in the table.
    def __repr__(self):
        return f"<Task {self.id}>" #It tells Python:"When you display this object, represent it using its task ID."SQLAlchemy turns that row into a Python object.
    

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        #put it in db
        task_content=request.form['content'] #get the content from the form 'submit ' using id='content'
        #create a model for class user
        new_task = User(content=task_content)

        #commit to database
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        #its gonna fetch all tasks from the database and display them
        tasks = User.query.order_by(User.date_created).all()
        return render_template("index_db5.html" , tasks=tasks)
        #tasks=tasks--Send the Python variable tasks to index_db5.html and make it available there under the name tasks.
        #tasks in HTML = tasks from Python.

@ app.route('/delete/<int:id>')
def delete(id):
    task_to_delete= User.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@ app.route('/update/<int:id>',methods=['GET', 'POST'])
def update(id):
    #getting the task to update from the database based on the provided id
    task = User.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'

    #if the request method is not POST, render the update form with the current task content
    else:
        return render_template('update_db5.html',task=task)

    
if __name__ == '__main__':
    app.run(debug=True)