from django.urls import path, include, re_path
import onken.workspace.views
from rest_framework import routers
from onken.public.api_views import UserViewSet, GroupViewSet
import django_cas_ng.views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', onken.workspace.views.index, name="workspace_index"),

    path('login', django_cas_ng.views.login),
    path('logout', django_cas_ng.views.logout),

    re_path(r'^api/', include(router.urls)),
]
