from django.views.generic import ListView, DetailView
from rest_framework import viewsets
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer


class CategoriesMixin(object):
    def get_context_data(self, **kwargs):
        context = super(CategoriesMixin, self).get_context_data(**kwargs)
        context['categories'] = Category.with_count.all()
        return context


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Post.published_posts.all()
    serializer_class = PostSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Category.with_count.all()
    serializer_class = CategorySerializer


class HomePage(ListView):
    context_object_name = "posts"
    template_name = "home.html"
    queryset = Post.published_posts.all()[:6]


class CategoryDetail(CategoriesMixin, DetailView):
    template_name = "blog/category_detail.html"
    context_object_name = "category"
    model = Category


class PostList(CategoriesMixin, ListView):
    paginate_by = 10
    template_name = "blog/index.html"
    context_object_name = "posts"
    queryset = Post.published_posts.all()


class PostDetail(CategoriesMixin, DetailView):
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    model = Post

    def get_queryset(self):
        if self.request.user.is_staff:
            queryset = Post.objects.all()
        else:
            queryset = Post.published_posts.all()
        return queryset
