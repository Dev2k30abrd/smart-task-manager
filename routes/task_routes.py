from flask import Blueprint, render_template, request, redirect, jsonify
from flask_login import login_required
from models.task import Task
from extensions import db, socketio

task_routes = Blueprint('task_routes', __name__)


# Dashboard
@task_routes.route('/dashboard')
@login_required
def dashboard():

    tasks = Task.query.all()

    return render_template(
        'dashboard.html',
        tasks=tasks
    )


# Add Task
@task_routes.route('/add_task', methods=['POST'])
@login_required
def add_task():

    title = request.form['title']
    description = request.form['description']
    priority = request.form['priority']
    due_date = request.form.get('due_date')

    task = Task(
        title=title,
        description=description,
        priority=priority,
        due_date=due_date,
        status='Pending'
    )

    db.session.add(task)
    db.session.commit()

    # WebSocket Event
    socketio.emit(
        'task_added',
        {'message': f'New task added: {title}'}
    )

    return redirect('/dashboard')


# Toggle Task Status
@task_routes.route('/toggle_status/<int:id>')
@login_required
def toggle_status(id):

    task = Task.query.get(id)

    if task.status == 'Pending':
        task.status = 'Completed'
    else:
        task.status = 'Pending'

    db.session.commit()

    return redirect('/dashboard')


# Delete Task
@task_routes.route('/delete_task/<int:id>')
@login_required
def delete_task(id):

    task = Task.query.get(id)

    db.session.delete(task)
    db.session.commit()

    return redirect('/dashboard')


# REST API
@task_routes.route('/api/tasks')
def api_tasks():

    tasks = Task.query.all()

    task_list = []

    for task in tasks:

        task_list.append({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'priority': task.priority,
            'status': task.status,
            'due_date': str(task.due_date)
        })

    return jsonify(task_list)