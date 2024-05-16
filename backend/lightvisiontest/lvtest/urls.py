
from django.urls import path
from lvtest.service.get.view import Get

urlpatterns = [
    path('get/', Get.as_view())
]
