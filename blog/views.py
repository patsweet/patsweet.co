from django.views.generic import ListView, DetailView
from .models import Post, Category
from django.utils import timezone
import os


class HomePage(ListView):
    context_object_name = "posts"
    template_name = "home.html"
    queryset = Post.published_posts.all()[:6]


class CategoryDetail(DetailView):
    template_name = "blog/category_detail.html"
    context_object_name = "category"
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.with_count.all()
        return context


class PostList(ListView):
    paginate_by = 10
    template_name = "blog/index.html"
    context_object_name = "posts"
    queryset = Post.published_posts.all()

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        context['categories'] = Category.with_count.all()
        return context


class PostDetail(DetailView):
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.with_count.all()
        return context