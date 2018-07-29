from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from onken.workspace.serializers import UserSerializer, GroupSerializer, VendorSerializer
from onken.workspace.models import Vendor


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class VendorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer