from django.urls import path
from .views import CloudServiceView

urlpatterns = [
    path('services/', CloudServiceView.as_view(), name='cloud_services'),
]
