
from django.urls import path
from lvtest.service.get.view import Get
from lvtest.service.list.view import GetList
from lvtest.service.remove.view import Remove
from lvtest.service.save.view import Save
from lvtest.service.upload.view import Upload

urlpatterns = [
    path('get/', Get.as_view()),
    path('get-list/', GetList.as_view()),
    path('save/', Save.as_view()),
    path('upload/', Upload.as_view()),
    path('remove/', Remove.as_view())
]
