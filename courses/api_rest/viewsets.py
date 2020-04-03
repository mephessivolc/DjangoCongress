from rest_framework.viewsets import ModelViewSet
from .serializers import InstituteSerializers, CoursesSerializers

from courses.models import Institute, Courses

class InstituteViewsets(ModelViewSet):

    queryset = Institute.objects.all()
    serializer_class = InstituteSerializers

class CoursesViewsets(ModelViewSet):

    queryset = Courses.objects.all()
    serializer_class = CoursesSerializers
