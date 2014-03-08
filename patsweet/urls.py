from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from filebrowser.sites import site
from rest_framework.routers import DefaultRouter
from blog.views import PostViewSet, CategoryViewSet

admin.autodiscover()


router = DefaultRouter(trailing_slash=False)
router.register(r'posts', PostViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('blog.urls', namespace="blog")),
    url(r'^api/', include(router.urls)),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),

)
