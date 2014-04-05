from rest_framework import viewsets
from .models import FamilyMember
from .serializers import FamilyMemberSerializer
from rest_framework import permissions
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
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

    @method_decorator(staff_member_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class FamilyList(ListView):
    paginate_by = 10
    template_name = "genealogy/index.html"
    context_object_name = "family"
    model = FamilyMember


class FamilyTreeList(ListView):
    template_name = "genealogy/tree.html"
    context_object_name = "family"
    queryset = FamilyMember.objects.all().order_by('pk')


class FamilyDetail(DetailView):
    template_name = "genealogy/family_detail.html"
    model = FamilyMember
    context_object_name = "member"
