from django.urls import path
from . import views


urlpatterns = [
    path('', views.CandidatoList.as_view(), name='candidato-list'),
    path('<int:pk>', views.CandidatoDetail.as_view(), name='candidato-detail'),
    path('resumed/<int:pk>', views.CandidatoResumed.as_view(), name='candidato-resumed'),
]
