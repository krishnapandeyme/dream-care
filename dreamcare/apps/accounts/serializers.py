from rest_framework import serializers

from .models import User
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CheckInSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        # List all of the fields that could possibly be included in a request
        # or response, including fields specified explicitly above.
        fields = ['mobile']


class OnBoardSerializer(serializers.Serializer):

    otp = serializers.CharField(max_length=4, write_only=True)
    otp_token = serializers.CharField(max_length=255, write_only=True)


