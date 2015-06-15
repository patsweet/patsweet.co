from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from .views import FamilyMemberViewSet, IndexView, FamilyList, FamilyTreeList, FamilyDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'members', FamilyMemberViewSet)

urlpatterns = patterns('',
    # API
    url(r'^api/', include(router.urls)),
    url(r'^$', login_required(FamilyList.as_view()), name='family-index'),
    url(r'^tree/$', login_required(FamilyTreeList.as_view()), name='family-tree'),
    url(r'^(?P<pk>\d+)/$', login_required(FamilyDetail.as_view()), name="family-detail"),
)
