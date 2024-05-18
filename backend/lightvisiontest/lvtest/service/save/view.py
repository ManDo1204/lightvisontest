__all__ = ['Save']

from datetime import datetime

from django.db import transaction
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework import serializers, status
from lvtest.models import Image
import requests
from django.core.files.images import ImageFile
import io


class InputSerializer(serializers.Serializer):
    image_url = serializers.URLField(max_length=200, min_length=None, allow_blank=False)


class Save(APIView):
    def __init__(self):
        super().__init__()

    def post(self, request: Request):

        input_data = InputSerializer(data=request.data)
        if input_data.is_valid() is not True:
            return JsonResponse({
                'message': 'Invalid param!'
            }, status=status.HTTP_400_BAD_REQUEST)
        image_url = input_data.validated_data['image_url']
        try:
            with transaction.atomic():
                file_ext, file_obj = self._get_image_from_url(image_url)

                image = Image.objects.create(
                    image=file_obj,
                    name=file_obj.name,
                    source=image_url,
                    filetype=file_ext
                )
        except Exception as e:
            return JsonResponse({
                'status': 'Fail',
                'error': e
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse({
            'image_name': image.name,
            'image_text_id': image.text_id
        }, status=status.HTTP_200_OK)

    def _get_image_from_url(self, url: str):
        get_image = requests.get(url)
        if get_image.status_code != 200:
            raise GetImageFail
        file = url.split("/")[-1]
        file_ext = file.split('.').pop()
        file_name = file.replace('.'+file_ext, '')

        # File name should have the rule to named
        dt_now = str(datetime.now())
        dt_object = datetime.strptime(dt_now, "%Y-%m-%d %H:%M:%S.%f")
        output_timestamp = dt_object.strftime("%Y-%m-%d_%H%M%S.%f")
        file_name = file_name + '_' + output_timestamp
        
        new_file = file_name + '.' + file_ext

        image_obj = ImageFile(io.BytesIO(get_image.content), name=new_file)
        return file_ext, image_obj
