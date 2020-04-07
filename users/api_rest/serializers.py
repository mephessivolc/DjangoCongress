from rest_framework import serializers

from users.models import Users

class UsersSerializers(serializers.ModelSerializer):

    class Meta:
        model = Users 
        fields = ['username', 'name', 'email', 'cpf']
