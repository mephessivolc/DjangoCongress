from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from .api_rest.viewsets import MinicoursesViewsets, SubscribeMinicoursesViewsets

router = routers.DefaultRouter()
router.register(r'minicursos', MinicoursesViewsets)
router.register(r'inscritos', SubscribeMinicoursesViewsets)

app_name = 'minicourses'
urlpatterns = [
    path('api_rest/', include(router.urls)),

]
