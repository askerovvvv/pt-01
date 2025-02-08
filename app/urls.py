from django.urls import path

from app import views

urlpatterns = [
    path('create/car/', views.create_car),
    path('get/cars/', views.get_all_cars),
    path('get/car/<int:car_id>', views.get_car_by_id),
    path('update/car/<int:car_id>', views.update_car),
    path('delete/car/<int:car_id>', views.delete_car),
    path('car/list/', views.CarListView.as_view()),
    path('car/create/', views.CarCreateView.as_view()),
    path('car/<pk>', views.CarByIdApiView.as_view()),
    path('car/update/<pk>', views.CarUpdateApiView.as_view()),
    path('car/delete/<pk>', views.CarDeleteApiView.as_view()),
]

