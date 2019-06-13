from . import views
from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jobs',views.jobsView)
router.register('getPublishedJobs',views.getPublishedJobs,basename='jobs')

urlpatterns = [
    path('',include(router.urls))
]

# urlpatterns = format_suffix_patterns(urlpatterns)