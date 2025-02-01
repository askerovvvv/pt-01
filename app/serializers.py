from rest_framework import serializers

from app.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=30)
    model = serializers.CharField(max_length=30)
    date = serializers.DateField()
    description = serializers.CharField()
    price = serializers.IntegerField()

    created_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

