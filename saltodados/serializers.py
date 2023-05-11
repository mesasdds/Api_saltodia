
from rest_framework import serializers
from .models import ArtigoPrincipal, ArtigoSecundario, ArtigoTerceiro, ArtigosRecommends, ArtigosGenericos


class ArtigoBaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'titulo', 'texto', 'create_at', 'update_at', 'imagem')


class ArtigoPrincipalSerializer(ArtigoBaseSerializer):
    class Meta(ArtigoBaseSerializer.Meta):
        model = ArtigoPrincipal


class ArtigoSecundarioSerializer(ArtigoBaseSerializer):
    class Meta(ArtigoBaseSerializer.Meta):
        model = ArtigoSecundario


class ArtigoTerceiroSerializer(ArtigoBaseSerializer):
    class Meta(ArtigoBaseSerializer.Meta):
        model = ArtigoTerceiro

class ArtigosRecommendSerializer(ArtigoBaseSerializer):
    class Meta(ArtigoBaseSerializer.Meta):
        model = ArtigosRecommends

class ArtigosGenericoSerializer(ArtigoBaseSerializer):
    class Meta(ArtigoBaseSerializer.Meta):
        model = ArtigosGenericos
