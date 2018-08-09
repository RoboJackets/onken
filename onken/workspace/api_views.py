from onken.workspace.models import Vendor
from onken.workspace.serializers import VendorSerializer
from rest_framework import viewsets


class VendorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows vendors to be viewed or edited.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
