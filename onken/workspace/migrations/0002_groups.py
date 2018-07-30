from django.db import migrations
from django.contrib.auth.models import Group


def forwards(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    group_administrator = Group.objects.get_or_create(name='administrator')
    group_pm = Group.objects.get_or_create(name='project_manager')
    group_requestor = Group.objects.get_or_create(name='requestor')
    group_ro = Group.objects.get_or_create(name='read_only')


def reverse(apps, schema_editor):
    if schema_editor.connection.alias != 'default':
        return

    Group.objects.get(name='administrator').delete()
    Group.objects.get(name='project_manager').delete()
    Group.objects.get(name='requestor').delete()
    Group.objects.get(name='read_only').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial')
    ]

    operations = [
        migrations.RunPython(forwards, reverse),
    ]
