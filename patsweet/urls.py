from django.conf.urls import patterns, include, url
from django.contrib import admin
from filebrowser.sites import site
from blog.views import HomePage

admin.autodiscover()

urlpatterns = patterns('',
    # ADMIN and FILEBROWSER
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # API Auth
    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),
    # Main Site
    url(r'^$', HomePage.as_view(), name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^contact/', include('contact_form.urls')),
    # Family Tree Project
    url(r'^family/', include('genealogy.urls')),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
)