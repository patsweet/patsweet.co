from django.test import TestCase
from .models import Post, Category
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class BlogModelTestCase(TestCase):
    def test_unicode(self):
        post = Post(headline='Testing a headline')
        self.assertEqual(str(post), 'Testing a headline')


class CategoryModelTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='tester', password='tester',
            first_name='Test', last_name='User',
            email='test@example.com')
        category = Category.objects.create(title='Hello World',
            slug='hello-world')
        Post.objects.create(
            headline='Testing', body='Hello World!',
            pub_date=timezone.now() - datetime.timedelta(minutes=5),
            published=False, author=user, slug='testing', category=category)

    def test_unicode(self):
        category = Category(title='Hello World')
        self.assertEqual(str(category), 'Hello World')

    def test_get_published_related_posts(self):
        category = Category.objects.get(title='Hello World')
        posts = Post.objects.filter(category=category)
        self.assertTrue(list(category.published_posts()) != list(posts))
        posts.update(published=True, pub_date=timezone.now() - datetime.timedelta(days=1))
        self.assertTrue(list(category.published_posts()) == list(posts))


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
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue(resp.context['posts'].count() == 0)
        Post.objects.all().update(published=True)
        resp = self.client.get('/blog/')
        self.assertTrue(resp.context['posts'].count() > 0)

    def test_blog_detail(self):
        resp = self.client.get(Post.objects.get().get_absolute_url())
        # All posts are published, should return 200.
        self.assertEqual(resp.status_code, 404)
        # Set all posts to "unpublished"
        Post.objects.all().update(published=True)
        resp = self.client.get(Post.objects.get().get_absolute_url())
        # Login required redirects user to login page, so 302 expected
        self.assertEqual(resp.status_code, 200)