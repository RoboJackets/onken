from django.urls import path
import onken.workspace.views

urlpatterns = [
    path('', onken.workspace.views.index, name="workspace_index")
]
