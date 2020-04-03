from rest_framework import serializers

from shirts.models import Shirts

class ShirtsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Shirts
        fields = ['shirt_type', 'shirt_size', 'color']
