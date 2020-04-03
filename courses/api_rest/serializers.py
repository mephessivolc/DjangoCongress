from rest_framework import serializers

from courses.models import Courses, Institute

class InstituteSerializers(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ['name']

class CoursesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ['name', 'institute']
