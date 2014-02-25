from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class PublishedPostManager(models.Manager):
    def get_queryset(self):
        return super(PublishedPostManager, self).get_queryset().filter(published=True).exclude(pub_date__gte=timezone.now())


class Post(models.Model):
    headline = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField(max_length=100)
    pub_date = models.DateTimeField('date published')
    published = models.BooleanField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)

    objects = models.Manager()
    published_posts = PublishedPostManager()

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return self.headline


class CategoryWithCountManager(models.Manager):
    def get_queryset(self):
        return super(CategoryWithCountManager, self).get_queryset().filter(post__published=True).annotate(num_posts=models.Count('post')).order_by('-num_posts')


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    objects = models.Manager()
    with_count = CategoryWithCountManager()

    class Meta:
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.title