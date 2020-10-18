from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dreamcare.apps.service import views

app_name = 'service'
urlpatterns = [
    path('v1/category', views.ServiceCategoryListAPIView.as_view()),
    path('v1/category/<int:pk>', views.ServiceCategoryDetailAPIView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)