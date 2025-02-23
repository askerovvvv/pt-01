from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from account.views import RegisterApiView

urlpatterns = [
    path('register/', RegisterApiView.as_view()),
    # path('authenticate/', LoginApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]


