from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the workspace app. This workspace is %s." % request.tenant.name)
