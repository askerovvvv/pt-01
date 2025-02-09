from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView
from rest_framework.response import Response

from app.models import Car, Category
from app.serializers import CarSerializer, CategorySerializer


# Create your views here.

@api_view(["POST"])
def create_car(request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
        car = serializer.save()
        return Response(
            {
                "brand": car.brand,
                "model": car.model,
                "date": car.date,
                "description": car.description,
                "price": car.price,
                "created_at": car.created_at,
            }, status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_all_cars(request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_car_by_id(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    if not car:
        return Response({"message": "not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(car)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def update_car(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    if not car:
        return Response({"message": "Car Not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = CarSerializer(car, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_car(request, car_id):
    car = Car.objects.filter(id=car_id).first()
    if not car:
        return Response({"message": "Car Not found"}, status=status.HTTP_404_NOT_FOUND)
    car.delete()
    return Response({"message": "deleted"}, status=200)


# GET
class CarListView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# POST
class CarCreateView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarByIdApiView(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarUpdateApiView(UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarDeleteApiView(DestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CategoryListCreateApiView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


