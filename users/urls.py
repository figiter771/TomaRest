from django.urls import path, include
from rest_framework import routers
from users import views



router = routers.DefaultRouter()
router.register(r'users',  views.UserCreate)
urlpatterns = [
    path('', include(router.urls)),
]