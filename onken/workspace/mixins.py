from pprint import pprint


class FieldPermissionsMixin(object):
    """
    https://gist.github.com/synotna/79f1e0128fb98394ceb6
    A Serializer mixin for controlling which fields are included based on user permissions

    Usage:
        class MySerializer(FieldPermissionsMixin, serializers.ModelSerializer):
            class Meta:
                model = MyModel
                field_permissions = {
                        'field': ['app.permission'],
                    }
    """

    class Meta:
        # field name: [list of permissions]
        field_permissions = {}

    def get_fields(self):
        fields = super().get_fields()
        user_permissions = self.context['request'].user.get_all_permissions()
        for field, permissions in self.Meta.field_permissions.items():
            # if user does not have one of the permissions to view the field, remove it
            if not any(permission in user_permissions for permission in permissions):
                fields.pop(field)
        return fields


class FieldGroupsMixin(object):
    """
    Based off of https://gist.github.com/synotna/79f1e0128fb98394ceb6
    A Serializer mixin for controlling which fields are included based on user groups

    Usage:
        class MySerializer(FieldGroupsMixin, serializers.ModelSerializer):
            class Meta:
                model = MyModel
                field_groups = {
                        'field': ['group'],
                    }
    """

    class Meta:
        # field name: [list of groups]
        field_groups = {}

    def get_fields(self):
        fields = super().get_fields()
        user_roles = self.context['request'].user.groups.values_list('name', flat=True)
        pprint(user_roles)
        for field, roles in self.Meta.field_groups.items():
            # if user does not have one of the roles to view the field, remove it
            if not any(role in user_roles for role in roles):
                fields.pop(field)
        return fields
