from django.conf.urls import patterns, url

from .views import HomePage, PostList, PostDetail, CategoryDetail

urlpatterns = patterns('',
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^blog/$', PostList.as_view(), name='blog'),
    url(r'^blog/category/(?P<slug>[-_\w]+)/(?P<pk>\d+)/$', CategoryDetail.as_view(), name="category-detail"),
    url(r'^blog/post/(?P<slug>[-_\w]+)/(?P<pk>\d+)/$', PostDetail.as_view(), name='post-detail'),
)
