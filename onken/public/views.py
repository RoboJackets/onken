from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import django_cas_ng.views
from django.http import HttpResponseForbidden
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from onken.public.serializers import UserSerializer, GroupSerializer


@login_required
def index(request):
    return HttpResponse("This is the public app.")


def login(request):
    if request.user.is_authenticated and not request.user.is_staff:
        return HttpResponseForbidden()
    else:
        return django_cas_ng.views.login(request)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer