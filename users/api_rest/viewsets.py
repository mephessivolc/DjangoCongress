from rest_framework.viewsets import ModelViewSet

from .serializers import UsersSerializers

from users.models import Users

class UsersViewsets(ModelViewSet):

    queryset = Users.objects.all()
    serializer_class = UsersSerializers
