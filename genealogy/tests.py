from django.test import TestCase
from django.contrib.auth.models import User


class FamilyMemberViewTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='tester',
            password='tester', first_name='Test',
            last_name='User', email='test@example.com',
            is_staff=True)

    def test_index(self):
        resp = self.client.get('/family/')
        self.assertEqual(resp.status_code, 404)
        self.client.login(username='tester', password='tester')
        resp = self.client.get('/family/')
        self.assertEqual(resp.status_code, 200)



