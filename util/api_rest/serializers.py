from rest_framework import serializers

from util.models import LuckyNumber

class LuckyNumberSerializers(serializers.ModelSerializer):

    class Meta:
        model = LuckyNumber
        fields = ['congress', 'user', 'number']
