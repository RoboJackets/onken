from django.contrib.auth.models import User, Group
from rest_framework import serializers
from onken.workspace.models import Vendor
from onken.workspace.mixins import FieldPermissionsMixin


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class VendorSerializer(FieldPermissionsMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ('url', 'name', 'nationality', 'billing_address',
                  'gt_vendor_id', 'status', 'sales_contact', 'customer_id',
                  'web_account', 'website', 'part_url_schema', 'shipping_quote_required',
                  'tax_exempt', 'requisition_guidance')

        field_permissions = {
            'sales_contact': ['workspace.view_vendor_sales_contact'],
            'customer_id': ['workspace.view_vendor_customer_id'],
        }

    # Override create() to enforce custom attribute permission logic
    def create(self, validated_data):
        # Get authenticated user
        user = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            user = request.user

        # If they can't create a vendor *but* can request one, override the status
        if not user.has_perm('create_vendor') & user.has_perm('request_vendor'):
            validated_data.pop('status', None)

            # Set the admin_notes custom value...
            validated_data['status'] = 'unapproved'

        instances = [
            Vendor(**attrs) for attrs in validated_data
        ]
        return Vendor.objects.bulk_create(instances)