from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArtigoPrincipalSerializer, ArtigoSecundarioSerializer, ArtigoTerceiroSerializer, ArtigosGenericoSerializer, ArtigosRecommendSerializer
from .models import ArtigoPrincipal, ArtigoSecundario, ArtigoTerceiro, ArtigosGenericos, ArtigosRecommends




class ArtigoBaseView(viewsets.ModelViewSet):
    pass

class ArtigoPrincipalView(ArtigoBaseView):
    serializer_class = ArtigoPrincipalSerializer
    queryset = ArtigoPrincipal.objects.all()

class ArtigoSecundarioView(ArtigoBaseView):
    serializer_class = ArtigoSecundarioSerializer
    queryset = ArtigoSecundario.objects.all()

class ArtigoTerceiroView(ArtigoBaseView):
    serializer_class = ArtigoTerceiroSerializer
    queryset = ArtigoTerceiro.objects.all()

class ArtigosRecommendsView(ArtigoBaseView):
    serializer_class = ArtigosRecommendSerializer
    queryset = ArtigosRecommends.objects.all()

class ArtigosGenericosView(ArtigoBaseView):
    serializer_class = ArtigosGenericoSerializer
    queryset = ArtigosGenericos.objects.all()
