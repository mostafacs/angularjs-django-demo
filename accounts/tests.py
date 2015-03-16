from django.test import TestCase

# Create your tests here.

class TestCalls(TestCase):
    def test_call_view_denies_anonymous(self):
        response = self.client.post('http://127.0.0.1:8000/users/', user='{"first_name":"angular","last_name":"angualr","email":"ang@angular.com","password":"123","gender":"M"}')
        print(str(response))
        self.assertRedirects(response, '/login/')