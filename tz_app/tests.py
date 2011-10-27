from django.test import TestCase

class AppTest(TestCase):

    def test_home(self):
        """Tests that the home page works."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
