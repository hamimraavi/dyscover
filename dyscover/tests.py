from django.test import TestCase

class DyscoverViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/api/search/', {'q':'delhi'})
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/api/search/', {'x':'delhi'})
        self.assertEqual(resp.status_code, 400)
        resp = self.client.get('/api/search/', {'q':'lmklaaoq'})
        self.assertEqual(resp.status_code, 404)
