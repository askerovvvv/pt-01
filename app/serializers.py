from rest_framework import serializers

from app.models import Car, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name", "full_name"]


class CarSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    category = CategorySerializer()

    class Meta:
        model = Car
        fields = "__all__"

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


"""
1) Логика фотографий
2) Регистрация\аутенфикация -->  Избранные, лайки
3) выбор валют
4) добавитм тг бота, 
5) поиск
"""
