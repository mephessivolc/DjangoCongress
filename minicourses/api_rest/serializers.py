from rest_framework import serializers

from minicourses.models import Minicourses, SubscribeMinicourses

class MinicoursesSerializers(serializers.ModelSerializer):

    class Meta:
        model = Minicourses
        fields = ['congress', 'teacher', 'name', 'quantity_places']

class SubscribeMinicoursesSerializers(serializers.ModelSerializer):

    class Meta:
        model = SubscribeMinicourses
        fields = ['minicourse', 'user']
