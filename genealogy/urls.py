from django.conf.urls import patterns, url, include
from .views import FamilyMemberViewSet, IndexView, FamilyList, FamilyTreeList, FamilyDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'members', FamilyMemberViewSet)

urlpatterns = patterns('',
    # API
    url(r'^api/', include(router.urls)),
    url(r'^$', FamilyList.as_view(), name='family-index'),
    url(r'^tree/$', FamilyTreeList.as_view(), name='family-tree'),
    url(r'^(?P<pk>\d+)/$', FamilyDetail.as_view(), name="family-detail"),
)
