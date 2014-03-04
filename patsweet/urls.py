from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from filebrowser.sites import site

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('blog.urls')),
    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name="about"),

)
