from lab import app
import unittest

class LabratTestCase(unittest.TestCase):
    def test_login_response_code(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue('Please login' in response.data)

    def test_login_correct_credentials(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn('You were just logged in.', response.data)

    def test_login_required(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_home_page_content(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn('Welcome to Home page', response.data)

    def test_login_incorrect_credentials(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn('Invalid credentials. Please try again', response.data)

    def test_logout(self):
        tester = app.test_client(self)
        tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        response = tester.get(
            'logout',
            content_type="html/text",
            follow_redirects=True
        )
        self.assertIn('You were just logged out', response.data)

    def test_home_posts(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login',
            data=dict(username="admin", password="admin"),
            follow_redirects=True
        )
        self.assertTrue('Good' in response.data and 'Well' in response.data)

if __name__ == '__main__':
    unittest.main()
