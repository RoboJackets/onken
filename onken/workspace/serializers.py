from django.contrib.auth.models import User, Group
from rest_framework import serializers
from onken.workspace.models import Vendor


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ('url', 'name', 'nationality', 'billing_address',
                  'gt_vendor_id', 'status', 'sales_contact', 'customer_id',
                  'web_account', 'website', 'part_url_schema', 'shipping_quote_required',
                  'tax_exempt', 'requisition_guidance')
