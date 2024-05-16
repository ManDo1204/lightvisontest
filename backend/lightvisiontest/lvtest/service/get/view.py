__all__ = ['Get']

from rest_framework.views import APIView
import uuid
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework import serializers, status


# class InputSerializer(serializers.Serializer):
#     text_id = serializers.UUIDField(required=True)

class Get(APIView):
    def __init__(self):
        super().__init__()

    def get(self, request: Request):

        # input_data = InputSerializer(data=request.data)
        # if input_data.is_valid() is not True:
        #     return JsonResponse({
        #         'message': 'Invalid param!'
        #     }, status=status.HTTP_400_BAD_REQUEST)
        #
        # image_token = str(uuid.uuid4())
        #
        try:
            # image = Image.objects.get(text_id=input_data.validated_data['text_id'])
            # cache.set(image_token, image.image.path, timeout=3000)
            print('get image')

        except Exception as e:
            return JsonResponse({
                'status': 'Fail',
                'error': e
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return JsonResponse({
            'status': 'Success',
            'image_token': ""
        }, status=status.HTTP_200_OK)