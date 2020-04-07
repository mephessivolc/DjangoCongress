from rest_framework.viewsets import ModelViewSet

from .serializers import MinicoursesSerializers, SubscribeMinicoursesSerializers

from minicourses.models import Minicourses, SubscribeMinicourses

class MinicoursesViewsets(ModelViewSet):

    queryset = Minicourses.objects.all()
    serializer_class = MinicoursesSerializers

class SubscribeMinicoursesViewsets(ModelViewSet):

    queryset = SubscribeMinicourses.objects.all()
    serializer_class = SubscribeMinicoursesSerializers
