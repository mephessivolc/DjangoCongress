from rest_framework.viewsets import ModelViewSet

from .serializers import LuckyNumberSerializers

from util.models import LuckyNumber

class LuckyNumberViewsets(ModelViewSet):

    queryset = LuckyNumber.objects.all()
    serializer_class = LuckyNumberSerializers
