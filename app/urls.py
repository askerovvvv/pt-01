from django.urls import path

from app import views

urlpatterns = [
    path('create/car/', views.create_car),
    path('get/cars/', views.get_all_cars),
    path('get/car/<int:car_id>', views.get_car_by_id),
    path('update/car/<int:car_id>', views.update_car),
]
