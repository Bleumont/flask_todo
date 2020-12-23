from flask import Flask, render_template, url_for, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import dotenv, os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('MYSQL_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    idtodo = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.idtodo

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Task(content=task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'Hubo un error'

    else:
        tasks = Task.query.order_by(Task.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Error borrando la entrada'

@app.route('/update/<int:idtodo>', methods=['GET', 'POST'])
def update(idtodo):
    task_update = Task.query.get_or_404(idtodo)
    if request.method == 'POST':
        task_update.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Error editando la entrada'
        
    else:
        return render_template('update.html', task=task_update)

if __name__ == "__main__":
    app.run(debug=True)