from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import CustomUser
from account.serializers import RegisterSerializer


# Create your views here.
class RegisterApiView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = "Вы успешно прошли регистрацию на нашу платформу!"
            return Response(message, status=201)

        return Response(serializer.errors, status=400)


class ActivateUserApiView(APIView):
    def get(self, request, activation_code):
        try:
            user = CustomUser.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return HttpResponse("Your account have been successfully activated!")
        except CustomUser.DoesnotExist:
            return HttpResponse('Your activation code is not valid please check it again and try')

