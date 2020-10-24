from rest_framework import status
from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from dreamcare.apps.service.models import ServiceCategory, ServiceSubCategory
from dreamcare.apps.service.serializers import ServiceCategorySerializer, ServiceSubCategorySerializer
from rest_framework.pagination import LimitOffsetPagination


class ServiceCategoryListAPIView(generics.ListAPIView):
    """
    List all templates, or create a new template.
    """
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    category_serializer_class = ServiceCategorySerializer
    subcategory_serializer_class = ServiceSubCategorySerializer
    pagination_class = LimitOffsetPagination

    def get(self, request, format=None):
        service_categories = ServiceCategory.objects.all()
        if service_categories:
            for service_category in service_categories:
                subcategories = service_category.servicesubcategory_set.all()
                service_category.subcategories = subcategories
            category_serializer = self.category_serializer_class(service_categories, many=True)
            return Response(category_serializer.data, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response([], status=status.HTTP_404_NOT_FOUND)

    def post(self, request, format=None):
        if self.request.user.role == "ADMIN":
            is_category = self.request.data.get('is_category', None)
            if is_category is None:
                response = {
                    "detail": "Not a valid request"
                }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer_class = self.category_serializer_class if is_category else self.subcategory_serializer_class
                serializer = serializer_class(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {
                "detail": "You are not authorized to perform this operation"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


class ServiceCategoryDetailAPIView(APIView):
    """
    Retrieve, update or delete a vigyapan instance.
    """
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    serializer_class = ServiceCategorySerializer

    def get_object(self, pk, is_category=None):
        try:
            if is_category is None:
                return ServiceCategory.objects.get(pk=pk)
            return ServiceCategory.objects.get(pk=pk) if is_category == "category" else ServiceSubCategory.objects.get(pk=pk)
        except ServiceCategory.DoesNotExist:
            raise Http404
        except ServiceSubCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        service_category = self.get_object(pk)
        service_category.subcategories = service_category.servicesubcategory_set.all()
        serializer = self.serializer_class(service_category)
        return Response(serializer.data)

    # def put(self, request, pk, format=None):
    #     service_category = self.get_object(pk)
    #     service_category.subcategories = service_category.servicesubcategory_set.all()
    #     serializer = self.serializer_class(service_category, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, is_category, format=None):

        if self.request.user.role == "ADMIN":
            if is_category in ["category", "subcategory"]:
                obj = self.get_object(pk, is_category)
                obj.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                response = {
                        "detail": "Not a valid request"
                    }
                return Response(response, status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {
                "detail": "You are not authorized to perform this operation"
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)



