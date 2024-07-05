import unittest
from app import create_app, db, bcrypt
from app.models import User

class AuthTestCase(unittest.TestCase):
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

    def test_register_user(self):
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.query.count(), 1)

    def test_register_existing_user(self):
        self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        response = self.client.post('/register', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 400)

    def test_login_user(self):
        hashed_password = bcrypt.generate_password_hash('testpassword').decode('utf-8')
        user = User(username='testuser', password=hashed_password)
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_json())

    def test_login_invalid_user(self):
        response = self.client.post('/login', json={
            'username': 'nonexistent',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 401)

    def test_login_invalid_password(self):
        hashed_password = bcrypt.generate_password_hash('testpassword').decode('utf-8')
        user = User(username='testuser', password=hashed_password)
        db.session.add(user)
        db.session.commit()

        response = self.client.post('/login', json={
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 401)
