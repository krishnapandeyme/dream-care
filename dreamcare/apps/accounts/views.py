from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from dreamcare.utils.otp_utils import send_otp
from dreamcare.apps.accounts.serializers import CheckInSerializer, OnBoardSerializer
from dreamcare.apps.accounts.models import User
from dreamcare.utils.jwt_utils import decode


class OnBoardAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = OnBoardSerializer

    def post(self, request):
        user_data = request.data.get('user', {})
        otp_token = self.request.headers.get('Authorization', '')
        user_data['otp_token'] = otp_token
        serializer = self.serializer_class(data=user_data)
        serializer.is_valid(raise_exception=True)
        payload = decode(otp_token)
        if user_data.get('otp', '') == payload.get('otp', ''):
            try:
                user = User.objects.get(mobile=payload.get('mobile', ''))
            except User.DoesNotExist:
                validated_data = {
                    'mobile': payload.get('mobile', '')
                }
                user = User.objects.create_user(**validated_data)
                response = {
                    'mobile': str(user.mobile),
                    'token': user.token
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                if not user.is_active:
                    response = {
                        'detail': "User is deactivated"
                    }
                    return Response(response, status=status.HTTP_403_FORBIDDEN)
                else:
                    response = {
                        'mobile': str(user.mobile),
                        'token': user.token
                    }
                    return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'detail': "OTP doesn't match."
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class CheckInAPIView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = CheckInSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        otp, otp_token = send_otp(user)
        if otp_token:
            response = {
                "otp": otp,
                "otp_token": otp_token
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                "detail": "Couldn't process the request"
            }
            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
