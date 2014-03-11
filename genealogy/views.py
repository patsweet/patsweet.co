from rest_framework import viewsets
from .models import FamilyMember
from .serializers import FamilyMemberSerializer
from rest_framework import permissions
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class FamilyMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = FamilyMember.objects.all().order_by('birthday')
    serializer_class = FamilyMemberSerializer
    permission_classes = [permissions.IsAuthenticated]


class IndexView(TemplateView):
    template_name = 'genealogy/index.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)