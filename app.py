from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class Person(db.Model):
    name = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)

class TaskForm(FlaskForm):
    content =  StringField('Enter Task')
    submit = SubmitField('Add Task')



@app.route('/', methods=["POST", "GET"])
def hello_internet():
    message = ""
    form = TaskForm()

    if request.method == 'POST':
        
        new_task = Todo(content=form.content.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('hello_internet'))
    else:
        all_tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', form=form, message=message, all_tasks=all_tasks)

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    task = Todo.query.get(id)
    if request.method == 'POST':
        task.content = request.form['content']
        db.session.commit()
        return redirect('/')
    else:
        return render_template('update.html', task=task)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_be_deleted = Todo.query.get(id)
    db.session.delete(task_to_be_deleted)
    db.session.commit()
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)