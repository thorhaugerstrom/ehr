from flask import Blueprint, jsonify, request
from .models import get_db_connection

bp = Blueprint('api', __name__)

@bp.route('/patients', methods=['GET'])
def get_patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    conn.close()
    return jsonify([dict(row) for row in patients])

    