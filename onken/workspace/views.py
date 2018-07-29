from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return HttpResponse("This is the workspace app. This workspace is %s." % request.tenant.name)
