import flask
import sqlite3

def create_app():
    app = Flask(__name__)

    from .routes import bp as api_bp
    app.register_blueprint(api_bp)

    return app

def get_db_connection():
    conn = sqlite3.connect('patients.db')
    conn.row_factory = sqlite3.Row
    return conn

