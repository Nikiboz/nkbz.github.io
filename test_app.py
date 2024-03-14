import unittest
from flask import Flask, render_template
from app import app  # Replace 'your_main_app_file' with the actual name of your main app file

class TestAppRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_blog_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome', response.data)

    def test_projects_route(self):
        response = self.app.get('/projects')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'projects', response.data)

    def test_photos_route(self):
        response = self.app.get('/photos')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'photos', response.data)

    def test_cv_route(self):
        response = self.app.get('/cv')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'cv', response.data)

if __name__ == '__main__':
    unittest.main()
