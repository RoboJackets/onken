from django.urls import path
import onken.workspace.views
from django.conf.urls import url, include
from rest_framework import routers
import onken.workspace.api_views

router = routers.DefaultRouter()
router.register(r'users', onken.workspace.api_views.UserViewSet)
router.register(r'groups', onken.workspace.api_views.GroupViewSet)

urlpatterns = [
    path('', onken.workspace.views.index, name="workspace_index"),
    url(r'^api/', include(router.urls)),
]
