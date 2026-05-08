from flask import Blueprint, render_template

from models.task import Task

import pandas as pd
import numpy as np


analytics = Blueprint('analytics', __name__)


@analytics.route('/analytics')
def analytics_dashboard():

    tasks = Task.query.all()

    data = []

    for task in tasks:

        data.append({

            'title': task.title,

            'priority': task.priority,

            'status': task.status

        })

    # SAFE DATAFRAME
    if len(data) > 0:

        df = pd.DataFrame(data)

        total_tasks = len(df)

        completed_tasks = len(
            df[df['status'] == 'Completed']
        )

        pending_tasks = len(
            df[df['status'] == 'Pending']
        )

        high_priority = len(
            df[df['priority'] == 'High']
        )

        completion_percentage = np.round(
            (completed_tasks / total_tasks) * 100,
            2
        )

    else:

        total_tasks = 0

        completed_tasks = 0

        pending_tasks = 0

        high_priority = 0

        completion_percentage = 0


    return render_template(

        'analytics.html',

        total_tasks=total_tasks,

        completed_tasks=completed_tasks,

        pending_tasks=pending_tasks,

        high_priority=high_priority,

        completion_percentage=completion_percentage

    )