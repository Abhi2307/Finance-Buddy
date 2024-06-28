import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:\\Users\\abhin\\portfolio' )))

from app import app  # Now this import should work

class BasicTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def register(self, username, password):
        return self.app.post('/register', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def test_index_page(self):
        # First, register a user
        self.register('testuser', 'testpass')
        
        # Then, log in
        response = self.login('testuser', 'testpass')
        
        # Check if login was successful by checking the session
        with self.app as c:
            with c.session_transaction() as sess:
                sess['username'] = 'testuser'
        
        # Now, access the index page
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register_page(self):
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
