from flask import Blueprint, jsonify
from models.task import Task

api = Blueprint('api', __name__)


@api.route('/api/tasks')
def get_tasks():

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