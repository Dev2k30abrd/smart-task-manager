from flask import Flask, redirect
from config import Config
from extensions import db, login_manager, socketio

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Extensions
db.init_app(app)
login_manager.init_app(app)
socketio.init_app(app)

login_manager.login_view = 'auth.login'

# Import Models
from models.user import User
from models.task import Task

# User Loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Route
@app.route('/')
def home():
    return redirect('/login')

# Import Blueprints
from routes.auth_routes import auth
from routes.task_routes import task_routes
from analytics.analytics_routes import analytics
from routes.api_routes import api

# Register Blueprints
app.register_blueprint(auth)
app.register_blueprint(task_routes)
app.register_blueprint(analytics)
app.register_blueprint(api)

# Create Database Tables
with app.app_context():
    db.create_all()

# Run App
if __name__ == "__main__":
    socketio.run(app, debug=True)