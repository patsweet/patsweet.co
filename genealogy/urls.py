from django.conf.urls import patterns, url, include
from .views import FamilyMemberViewSet, IndexView, FamilyList
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'members', FamilyMemberViewSet)

urlpatterns = patterns('',
    # API
    url(r'^api/', include(router.urls)),
    url(r'^$', FamilyList.as_view(), name='family-index'),
)