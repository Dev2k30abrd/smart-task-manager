# Smart Task Manager

Smart Task Manager is a full-stack web application developed using Flask and PostgreSQL. The project helps users manage daily tasks efficiently with authentication, task tracking, analytics, REST APIs, and a responsive dashboard.


## Features

- User Registration and Login
- Secure Password Hashing
- Add, Update, and Delete Tasks
- Task Status Toggle (Pending / Completed)
- Due Date Support
- Task Priority Management
- Search Tasks
- Analytics Dashboard
- REST API Integration
- PostgreSQL Database Support
- Responsive Bootstrap UI


## Tech Stack

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- Flask-Login
- Flask-SocketIO
- Pandas
- NumPy
- HTML
- CSS
- Bootstrap


## Project Structure

```text
smart-task-manager/
│
├── analytics/
├── models/
├── routes/
├── templates/
├── static/
│
├── app.py
├── config.py
├── extensions.py
├── requirements.txt
├── schema.sql
└── README.md
```


## Setup Instructions

### 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

#### Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```


### 4. Setup PostgreSQL Database

Create a PostgreSQL database named:

```text
smart_task_db
```

Update PostgreSQL credentials inside `config.py`.


### 5. Run the Project

```bash
python app.py
```

Application will run on:

```text
http://127.0.0.1:5000
```


## REST API

Get all tasks:

```text
/api/tasks

Returns task data in JSON format.


## Analytics

The analytics dashboard uses:
- Pandas for data processing
- NumPy for statistical calculations

Displays:
- Total Tasks
- Completed Tasks
- Pending Tasks
- High Priority Tasks
- Completion Percentage


## Database Schema

The project database schema is available in:

```text
schema.sql



## Future Improvements

- AI-based Task Recommendations
- Email Notifications
- Calendar Integration
- Dark Mode
- Real-time Collaboration


## Conclusion

This project demonstrates full-stack web development using Flask and PostgreSQL with authentication, REST APIs, analytics, responsive UI, and database integration.
