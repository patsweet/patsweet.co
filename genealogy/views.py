from rest_framework import viewsets
from .models import FamilyMember
from .serializers import FamilyMemberSerializer


class FamilyMemberViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = FamilyMember.objects.all().order_by('birthday')
    serializer_class = FamilyMemberSerializer
