from django.contrib import admin
from .models import Workspace, Domain, User
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import PermissionDenied

admin.site.site_header = 'Onken Administration'
admin.site.site_title = 'Onken Administration'
admin.site.index_title = 'Home'
admin.site.site_url = None
admin.site.disable_action('delete_selected')


class DomainInline(admin.TabularInline):
    model = Domain
    extra = 1


@admin.register(Workspace)
class WorkspaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_primary_domain']
    search_fields = ['name']

    Workspace.get_primary_domain.short_description = 'Primary domain'

    inlines = [DomainInline]

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['domain', 'tenant']
    search_fields = ['domain']


@admin.register(User)
class UserAdmin(UserAdmin):
    def user_change_password(self, request, id):
        raise PermissionDenied
