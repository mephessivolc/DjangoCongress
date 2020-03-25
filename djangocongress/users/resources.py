from import_export import resources
from .models import Users


class UsersNameResources(resources.ModelResource):
    class Meta:
        model = Users
        fields = ['name']

class UsersNameEmailResources(resources.ModelResource):
    class Meta:
        model = Users
        fields = ['name', 'email']
