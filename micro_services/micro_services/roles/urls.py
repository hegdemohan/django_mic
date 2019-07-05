from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('roles',views.rolesView)
router.register('sendMail',views.sendMail,basename="roles")
router.register('checkUserRole',views.checkUserRole,basename="roles")

urlpatterns = [
    path('',include(router.urls))
]