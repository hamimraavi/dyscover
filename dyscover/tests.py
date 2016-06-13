from django.test import TestCase

class DyscoverViewsTestCase(TestCase):
    def test_correct_query(self):
        resp = self.client.get('/api/search/', {'q':'delhi'})
        self.assertEqual(resp.status_code, 200)
    
    
    def test_incorrect_parameter(self):
        resp = self.client.get('/api/search/', {'x':'delhi'})
        self.assertEqual(resp.status_code, 400)
    
    
    def test_invalid_data(self):
        resp = self.client.get('/api/search/', {'q':'lmklaaoq'})
        self.assertEqual(resp.status_code, 404)
