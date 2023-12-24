import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_about_page(self):
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)

    def test_how_to_order_page(self):
        result = self.app.get('/how-to-order')
        self.assertEqual(result.status_code, 200)

    def test_flower_profile(self):
        result = self.app.get('/flower/1')
        self.assertEqual(result.status_code, 200)
        # Убедитесь, что строка ниже исправлена
        self.assertNotIn('Цветок с таким ID не найден', result.data.decode('utf-8'))

    def test_flower_profile_not_found(self):
        result = self.app.get('/flower/9999')  # ID, которого точно нет
        self.assertEqual(result.status_code, 404)
        self.assertIn('Цветок с таким ID не найден', result.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()