from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework import generics, filters, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django_filters.rest_framework import DjangoFilterBackend

from .models import Candidato
from .serializers import CandidatoSerializer, CandidatoSerializerResumed, UserSerializer
from .permissions import IsAdminUserOrReadOnly


class CandidatoList(generics.ListCreateAPIView):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['habilidades']
    filterset_fields = ['status']
    permission_classes = [IsAuthenticated]


class CandidatoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]
    http_method_names = ['get', 'put', 'delete'] 


class CandidatoResumed(generics.RetrieveAPIView):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializerResumed


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CandidateDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

    def delete(self, request, pk):
        candidato = get_object_or_404(Candidato, pk=pk)
        candidato.delete()
        return Response({"message": "Candidato excluído"}, status=status.HTTP_204_NO_CONTENT)


class MyTokenObtainPairView(TokenObtainPairView):
    pass


class MyTokenRefreshView(TokenRefreshView):
    pass
