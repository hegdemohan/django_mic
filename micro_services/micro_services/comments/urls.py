from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('comments',views.commentsView)
router.register('getComments',views.getComments,basename="comments")
urlpatterns = [
    path('',include(router.urls))
]