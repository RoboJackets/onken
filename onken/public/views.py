from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import django_cas_ng.views
from django.core.exceptions import PermissionDenied


@login_required
def index(request):
    return HttpResponse("This is the public app.")


def login(request):
    if(request.user.is_authenticated and not request.user.is_staff):
        raise PermissionDenied
    else:
        return django_cas_ng.views.login(request)
