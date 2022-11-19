from rest_framework import serializers

from .models import User


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    ),

    token = serializers.CharField(max_length=255, read_only=True),

    def create(self, validated_data):
        print(validated_data)
        # user = User.objects.create_user(
        #     username=validated_data['username'],
        #     nickname=validated_data['nickname'],
        #     password=validated_data['password']
        # )
        # return user
        return User.objects.create_user(**validated_data)

    class Meta:
        model = User
        fields = [
            'username',
            'nickname',
            'password',
            'token'
        ]
