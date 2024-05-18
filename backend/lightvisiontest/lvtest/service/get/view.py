__all__ = ['Get']

from rest_framework.views import APIView
from django.http import JsonResponse, FileResponse
from rest_framework.request import Request
from rest_framework import serializers, status
from lvtest.models import Image


class InputSerializer(serializers.Serializer):
    image_id = serializers.UUIDField(required=True)


class Get(APIView):
    def __init__(self):
        super().__init__()

    def get(self, request: Request):

        input_data = InputSerializer(data=request.query_params)
        if input_data.is_valid() is not True:
            return JsonResponse({
                'message': 'Invalid param!'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            image = Image.objects.get(text_id=input_data.validated_data['image_id'])
            image_url = image.image.path
            file_name = image.image.name

        except Exception as e:
            return JsonResponse({
                'status': 'Fail',
                'error': e
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return FileResponse(open(image_url, 'rb'), filename=file_name)
