import unittest
import json
from app import create_app, init_db

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()
        init_db()

    def test_get_all_patients(self):
        response = self.client.get('/patients')
        self.assertEqual(response.status_code, 200)

    def test_delete_patient(self):
        new_patient = {
            "name": "Test Patient",
            "age": 40,
            "condition": "Heart attack",
            "admission_date": "2023-09-20"
        }
        self.client.post('/patients', data=json.dumps(new_patient), content_type='application/json')
        response = self.client.delete('/patients/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Patient deleted successfully', str(response.data))