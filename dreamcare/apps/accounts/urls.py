from django.urls import path
from dreamcare.apps.accounts.views import CheckInAPIView, OnBoardAPIView

app_name = 'account'
urlpatterns = [
    path('v1/users/checkin', CheckInAPIView.as_view()),
    path('v1/users/onboard', OnBoardAPIView.as_view()),
]