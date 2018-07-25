from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from onken.public.serializers import UserSerializer, GroupSerializer, WorkspaceSerializer, DomainSerializer
from onken.public.models import Workspace, Domain


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


class WorkspaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows workspaces to be viewed or edited
    """
    queryset = Workspace.objects.all()
    serializer_class = WorkspaceSerializer


class DomainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows domains to be viewed or edited
    """
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
