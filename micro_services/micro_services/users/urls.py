from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users',views.usersView)
router.register('login',views.loginView,basename='users')

urlpatterns = [
    path('',include(router.urls))
]