from django.contrib import admin
from django.urls import path
import django_cas_ng.views
import onken.public.views

urlpatterns = [
    path('admin/login/', django_cas_ng.views.login),
    path('admin/logout/', django_cas_ng.views.logout),

    path('admin/', admin.site.urls),

    path('', onken.public.views.index, name='public_index'),

    path('accounts/login/', django_cas_ng.views.login),
    path('accounts/logout/', django_cas_ng.views.logout),
]
