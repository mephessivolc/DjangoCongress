from rest_framework.viewsets import ModelViewSet
from .serializers import CongressSerializers, TypeCongressSerializers, SubscriptionsSerializers

from congress.models import Congress, TypeCongress, Subscriptions

class CongressViewsets(ModelViewSet):

    queryset = Congress.objects.all()
    serializer_class = CongressSerializers

class TypeCongressViewsets(ModelViewSet):

    queryset = TypeCongress.objects.all()
    serializer_class = TypeCongressSerializers

class SubscriptionsViewsets(ModelViewSet):

    queryset = Subscriptions.objects.all()
    serializer_class = SubscriptionsSerializers
