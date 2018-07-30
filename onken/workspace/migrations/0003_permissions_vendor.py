from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from onken.workspace.models import Vendor


def forwards(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    # Create the new permission
    content_type = ContentType.objects.get_for_model(Vendor)
    perm_request_vendor = Permission.objects.create(codename='request_vendor',
                                                    name='Can request vendor', content_type=content_type)
    perm_view_sales_contact = Permission.objects.create(codename='view_vendor_sales_contact',
                                                        name='Can view vendor sales contact', content_type=content_type)
    perm_view_customer_id = Permission.objects.create(codename='view_vendor_customer_id',
                                                      name='Can view vendor customer ID', content_type=content_type)

    # Get the groups that need this permission
    group_administrator = Group.objects.get(name='administrator')
    group_pm = Group.objects.get(name='project_manager')
    group_requestor = Group.objects.get(name='requestor')

    # Add the permission to the groups
    group_administrator.permissions.add(perm_request_vendor, perm_view_sales_contact, perm_view_customer_id)
    group_pm.permissions.add(perm_request_vendor)
    group_requestor.permissions.add(perm_request_vendor, perm_view_sales_contact)


def reverse(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    Permission.objects.get(codename='request_vendor').delete()
    Permission.objects.get(codename='view_vendor_sales_contact').delete()
    Permission.objects.get(codename='view_vendor_customer_id').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_groups')
    ]

    operations = [
        migrations.RunPython(forwards, reverse),
    ]
