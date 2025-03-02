from rest_framework import serializers

from account.models import CustomUser
from account.send_mail import send_activation_code


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(min_length=6, write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ("email", "password", "password2", "birthDate")

    def validate(self, attrs):
        password2 = attrs.pop('password2')
        password = attrs.get('password')

        if password != password2:
            raise serializers.ValidationError('Password do not match')
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        code = user.activation_code
        send_activation_code(user.email, code)
        return user