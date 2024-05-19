__all__ = ['Upload']

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


class UploadImageFail(Exception):
    pass


class InputSerializer(serializers.Serializer):
    image = serializers.ImageField(required=True)


class Upload(APIView):
    def __init__(self):
        super().__init__()

    def post(self, request: Request):

        input_data = InputSerializer(data=request.data)
        if input_data.is_valid() is not True:
            return JsonResponse({
                'message': 'Invalid param!'
            }, status=status.HTTP_400_BAD_REQUEST)

        image_input = input_data.validated_data['image']
        file_name = image_input.name
        file_extension = file_name.split('.')[-1]
        file_name = file_name.replace('.'+file_extension, '')
        dt_now = str(datetime.now())
        dt_object = datetime.strptime(dt_now, "%Y-%m-%d %H:%M:%S.%f")
        output_timestamp = dt_object.strftime("%Y-%m-%d_%H%M%S.%f")
        file_name = file_name + '_' + output_timestamp
        new_file_name = file_name + '.' + file_extension

        image_input.name = new_file_name

        try:
            image = Image.objects.create(
                image=image_input,
                name=file_name,
                source='local upload',
                filetype=file_extension
            )
        except Exception as e:
            return JsonResponse({
                'message': e
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({
            'message': 'Upload Image Success',
            'image_name': image.name + '.' + image.filetype,
            'image_id': image.text_id
        }, status=status.HTTP_200_OK)
