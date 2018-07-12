from django.contrib import admin

from .models import Workspace, Domain

admin.site.register(Workspace)
admin.site.register(Domain)
