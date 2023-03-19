from django.test import TestCase, Client
from django.urls import reverse
from Parents.models import Parent
from django.contrib.auth.models import User

class LoginParentViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.parent = Parent.objects.create(user=self.user)

    def test_login(self):
        response = self.client.post(reverse('login-parent'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('parent_dashboard'))
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_message_view(self):
        response = self.client.get(reverse('login-parent'))
        self.assertEqual(response.status_code, 200)