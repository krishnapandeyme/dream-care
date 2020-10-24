from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from dreamcare.apps.service import views

app_name = 'myadmin'
urlpatterns = [
    path('v1/service-category', views.ServiceCategoryListAPIView.as_view()),
    path('v1/service-category/<int:pk>', views.ServiceCategoryDetailAPIView.as_view()),
    path('v1/service-category/<int:pk>/<str:is_category>', views.ServiceCategoryDetailAPIView.as_view()),
    path('v1/service-subcategory', views.ServiceCategoryListAPIView.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)