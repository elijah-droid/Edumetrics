# blog/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Lesson

class NewLessonTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.post_data = {
            'title': 'Test Post',
            'content': 'This is a test post.',
            'author': self.user.id,
        }

    def test_create_post_view(self):
        # Log in as the test user
        self.client.login(username='testuser', password='testpass')

        # Send a POST request to the view
        response = self.client.post(reverse('create_post'), data=self.post_data)

        # Verify that the post was created successfully
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEqual(post.title, 'Test Post')
        self.assertEqual(post.content, 'This is a test post.')
        self.assertEqual(post.author, self.user)
