from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
import django_cas_ng.views
import onken.public.views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', onken.public.views.UserViewSet)
router.register(r'groups', onken.public.views.GroupViewSet)


urlpatterns = [
    path('admin/login/', onken.public.views.login),
    path('admin/logout/', django_cas_ng.views.logout),
    path('admin/', admin.site.urls),

    path('', onken.public.views.index, name='public_index'),

    path('login', django_cas_ng.views.login),
    path('logout', django_cas_ng.views.logout),

    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
