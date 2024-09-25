from flask import Blueprint, jsonify, request
from .models import get_db_connection

bp = Blueprint('api', __name__)

@bp.route('/patients', methods=['GET'])
def get_patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    conn.close()
    return jsonify([dict(row) for row in patients])

@bp.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    conn = get_db_connection()
    patient = conn.execute('SELECT * FROM patients WHERE id = ?', (id,)).fetchone()
    conn.close()
    if patient is None:
        return jsonify({'error': 'Patient not found'}), 404
    return jsonify(dict(patient))

@bp.route('/patients', methods=['POST'])
def create_patient():
    new_patient = request.get_json()
    conn = get_db_connection()
    conn.execute('INSERT INTO patients (name, age, condition, admission_date) VALUES (?, ?, ?, ?)',
                 (new_patient['name'], new_patient['age'], new_patient['condition'], new_patient['admission_date']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Patient created successfuly'}, 201)

@bp.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM patients WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Patient deleted successfully'})
    