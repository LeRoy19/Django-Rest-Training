from rest_framework import status
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from ..models import *
from ..api.serializers import ManufacturerSerializer, ProductSerializer


class ManufacturerListAPIView(APIView):

    @staticmethod
    def get(request):
        manufactures = Manufacturer.objects.all()
        serializer = ManufacturerSerializer(manufactures, many=True, context={'request': request})
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = ManufacturerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManufacturerDetailAPIView(APIView):

    @staticmethod
    def get_object(pk):
        manufacturer = get_object_or_404(Manufacturer, pk=pk)
        return manufacturer

    @staticmethod
    def get(request, pk):
        manufacturer = ManufacturerDetailAPIView.get_object(pk)
        serializer = ManufacturerSerializer(manufacturer, context={'request': request})
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        manufacturer = ManufacturerDetailAPIView.get_object(pk)
        serializer = ManufacturerSerializer(manufacturer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        manufacturer = ManufacturerDetailAPIView.get_object(pk)
        manufacturer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductListAPIView(APIView):

    @staticmethod
    def get(request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailAPIView(APIView):

    @staticmethod
    def get_object(pk):
        product = get_object_or_404(Product, pk=pk)
        return product

    @staticmethod
    def get(request, pk):
        product = ProductDetailAPIView.get_object(pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data)

    @staticmethod
    def put(request, pk):
        product = ProductDetailAPIView.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        product = ProductDetailAPIView.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(["GET", "POST"])
# def manufacturer_list_create_api_view(request):
#
#     if request.method == "GET":
#         manufactures = Manufacturer.objects.all()
#         serializer = ManufacturerSerializer(manufactures, many=True)
#         return Response(serializer.data)
#
#     if request.method == "POST":
#         serializer = ManufacturerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def manufacturer_detail_api_view(request, pk):
#
#     try:
#         manufacturer = Manufacturer.objects.get(pk=pk)
#     except Manufacturer.DoesNotExist:
#         return Response({"error": {
#             "code": 404,
#             "message": "Article not found!",
#
#         }}, status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = ManufacturerSerializer(manufacturer)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = ManufacturerSerializer(manufacturer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         manufacturer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


