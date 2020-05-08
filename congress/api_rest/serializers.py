from rest_framework import serializers

from congress.models import Congress, TypeCongress, Subscriptions

class CongressSerializers(serializers.ModelSerializer):

    class Meta:
        model = Congress
        fields = ['username', 'name']

class TypeCongressSerializers(serializers.ModelSerializer):

    class Meta:
        model = TypeCongress
        fields = ['type_congress']

class SubscriptionsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Subscriptions
        fields = ['congress', 'user', 'is_staff', 'is_payment']
