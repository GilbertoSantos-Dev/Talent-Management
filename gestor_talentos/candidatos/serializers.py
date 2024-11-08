from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Candidato


class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'


class CandidatoSerializerResumed(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = ['id', 'nome_completo']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user
