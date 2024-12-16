from django.contrib import admin
from django.urls import path, include
from app.views import CloudServiceView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/services/', CloudServiceView.as_view(), name='services'),
]
