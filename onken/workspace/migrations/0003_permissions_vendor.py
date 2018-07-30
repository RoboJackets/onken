from django.db import migrations
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from onken.workspace.models import Vendor


def forwards(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    # Create the new permission
    content_type = ContentType.objects.get_for_model(Vendor)
    permission = Permission.objects.create(codename='can_request_vendor', name='Can request vendor',
                                           content_type=content_type)

    # Get the groups that need this permission
    group_administrator = Group.objects.get(name='administrator')
    group_pm = Group.objects.get(name='project_manager')
    group_requestor = Group.objects.get(name='requestor')

    # Add the permission to the groups
    group_administrator.permissions.add(permission)
    group_pm.permissions.add(permission)
    group_requestor.permissions.add(permission)


def reverse(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    Permission.objects.get(codename='can_request_vendor').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_groups')
    ]

    operations = [
        migrations.RunPython(forwards, reverse),
    ]
