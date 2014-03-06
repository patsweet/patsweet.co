from django.test import TestCase
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

class BlogViewsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='tester', password='tester',
            first_name='Test', last_name='User',
            email='test@example.com')
        Post.objects.create(
            headline='Testing', body='Hello World!',
            pub_date=timezone.now() - datetime.timedelta(minutes=5),
            published=False, author=user, slug='testing')

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('posts' in resp.context)
        self.assertTrue('FACEBOOK_APP_ID' in resp.context)
        self.assertTrue(resp.context['posts'].count() == 0)
        Post.objects.all().update(published=True)
        second_resp = self.client.get('/')
        self.assertTrue(second_resp.context['posts'].count() > 0)

    def test_blog_home(self):
        Post.objects.all().update(published=False)
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['posts'].count() == 0)
        Post.objects.all().update(published=True)
        resp = self.client.get('/blog/')
        self.assertTrue(resp.context['posts'].count() > 0)

    def test_blog_detail(self):
        resp = self.client.get(Post.objects.get().get_absolute_url())
        # All posts are published, should return 200.
        self.assertEqual(resp.status_code, 200)
        # Set all posts to "unpublished"
        Post.objects.all().update(published=False)
        resp = self.client.get(Post.objects.get().get_absolute_url())
        # Login required redirects user to login page, so 302 expected
        self.assertEqual(resp.status_code, 302)