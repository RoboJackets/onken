from django.urls import path
import onken.workspace.views
from django.conf.urls import url, include
from rest_framework import routers
import onken.workspace.api_views
import django_cas_ng.views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', onken.workspace.api_views.UserViewSet)
router.register(r'groups', onken.workspace.api_views.GroupViewSet)

urlpatterns = [
    path('admin/login/', onken.workspace.views.login),
    path('admin/logout/', django_cas_ng.views.logout),
    path('admin/', admin.site.urls),

    path('', onken.workspace.views.index, name="workspace_index"),

    path('login', django_cas_ng.views.login),
    path('logout', django_cas_ng.views.logout),

    url(r'^api/', include(router.urls)),
]
