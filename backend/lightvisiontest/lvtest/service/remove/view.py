__all__ = ['Remove']

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
    image_id = serializers.UUIDField(required=True)


class Remove(APIView):
    def __init__(self):
        super().__init__()

    def post(self, request: Request):

        input_data = InputSerializer(data=request.data)
        if input_data.is_valid() is not True:
            return JsonResponse({
                'message': 'Invalid param!'
            }, status=status.HTTP_400_BAD_REQUEST)
        image_id = input_data.validated_data['image_id']

        try:
            with transaction.atomic():
                image = Image.objects.get(
                    text_id=image_id
                )
                image.delete()
        except Exception as e:
            return JsonResponse({
                'status': 'Fail',
                'error': e
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return JsonResponse({
            'status': 'Success!',
        }, status=status.HTTP_200_OK)
