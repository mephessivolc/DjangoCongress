from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from .api_rest.viewsets import InstituteViewsets, CoursesViewsets

router = routers.DefaultRouter()
router.register(r'instituto', InstituteViewsets)
router.register(r'courses', CoursesViewsets)

app_name = 'courses'
urlpatterns = [
    path('api_rest/', include(router.urls)),

]
