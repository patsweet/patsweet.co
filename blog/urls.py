from django.conf.urls import patterns, url, include
from .views import PostList, PostDetail, CategoryDetail, PostViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = patterns('',
    url(r'^$', PostList.as_view(), name='blog-home'),
    url(r'^category/(?P<slug>[-_\w]+)/(?P<pk>\d+)/$', CategoryDetail.as_view(), name="blog-category-detail"),
    url(r'^post/(?P<slug>[-_\w]+)/(?P<pk>\d+)/$', PostDetail.as_view(), name='blog-post-detail'),
    # API
    url(r'^api/', include(router.urls)),
)
