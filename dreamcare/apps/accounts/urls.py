from django.urls import path
from dreamcare.apps.accounts.views import CheckInAPIView, OnBoardAPIView

app_name = 'account'
urlpatterns = [
    path('users/checkin', CheckInAPIView.as_view()),
    path('users/onboard', OnBoardAPIView.as_view()),
]