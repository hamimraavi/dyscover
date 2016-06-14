import json

from django.test import TestCase


class DyscoverViewsTestCase(TestCase):
    def test_valid_request(self):
        resp = self.client.get('/api/search/', {'q': 'delhi'})
        self.assertEqual(resp.status_code, 200)

    def test_bad_request(self):
        resp = self.client.get('/api/search/', {'x': 'delhi'})
        self.assertEqual(resp.status_code, 400)

    def test_data_not_found(self):
        resp = self.client.get('/api/search/', {'q': 'lmklaaoq'})
        self.assertEqual(resp.status_code, 404)

    def test_json_contains_list(self):
        resp = self.client.get('/api/search/', {'q': 'mumbai'})
        resp = json.loads(resp.content)
        flag = True if "Restaurants" in resp else False
        self.assertEquals(flag, True)

    def test_json_contains_name(self):
        resp = self.client.get('/api/search/', {'q': 'mumbai'})
        resp = json.loads(resp.content)
        flag = True if "Name" in resp["Restaurants"][0] else False
        self.assertEquals(flag, True)

    def test_json_contains_url(self):
        resp = self.client.get('/api/search/', {'q': 'mumbai'})
        resp = json.loads(resp.content)
        flag = True if "Url" in resp["Restaurants"][0] else False
        self.assertEquals(flag, True)
