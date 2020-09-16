from django.urls import path

from .views import UserProfileView

app_name = 'account'
urlpatterns = [
    path('see', UserProfileView.as_view()),
]