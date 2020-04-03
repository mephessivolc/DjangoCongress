from rest_framework.viewsets import ModelViewSet
from .serializers import ShirtsSerializers

from shirts.models import Shirts

class ShirtViewsets(ModelViewSet):

    queryset = Shirts.objects.all()
    serializer_class = ShirtsSerializers
