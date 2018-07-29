from django.urls import path, include, re_path
import onken.workspace.views
from rest_framework import routers
import onken.workspace.api_views
import django_cas_ng.views

router = routers.DefaultRouter()
router.register(r'users', onken.workspace.api_views.UserViewSet)
router.register(r'groups', onken.workspace.api_views.GroupViewSet)
router.register(r'vendors', onken.workspace.api_views.VendorViewSet)

urlpatterns = [
    path('', onken.workspace.views.index, name="workspace_index"),

    path('login', django_cas_ng.views.login),
    path('logout', django_cas_ng.views.logout),

    re_path(r'^api/', include(router.urls)),
]
