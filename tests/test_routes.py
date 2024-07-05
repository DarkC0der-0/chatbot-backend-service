import unittest
from app import create_app, db
from app.models import User, Conversation

class RoutesTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('app.config.Config')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register(self):
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)

    def test_chat(self):
        self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        login_response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        token = login_response.get_json()['access_token']
        response = self.client.post('/chat', json={'message': 'Hello'}, headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)

    def test_history(self):
        self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        login_response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        token = login_response.get_json()['access_token']
        self.client.post('/chat', json={'message': 'Hello'}, headers={'Authorization': f'Bearer {token}'})
        response = self.client.get('/history', headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 200)
