from django.contrib import admin
from django.urls import path, include, re_path
import django_cas_ng.views
import onken.public.api_views
import onken.public.views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', onken.public.api_views.UserViewSet)
router.register(r'groups', onken.public.api_views.GroupViewSet)
router.register(r'workspaces', onken.public.api_views.WorkspaceViewSet)
router.register(r'domains', onken.public.api_views.DomainViewSet)
router.register(r'permissions', onken.public.api_views.PermissionViewSet)


urlpatterns = [
    path('admin/login/', onken.public.views.login),
    path('admin/logout/', django_cas_ng.views.logout),
    path('admin/', admin.site.urls),

    path('', onken.public.views.index, name='public_index'),

    path('login', django_cas_ng.views.login),
    path('logout', django_cas_ng.views.logout),

    re_path(r'^api/', include(router.urls)),
]
