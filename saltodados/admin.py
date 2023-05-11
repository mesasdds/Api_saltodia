from django.contrib import admin
from .models import ArtigoPrincipal, ArtigoSecundario, ArtigoTerceiro, ArtigosRecommends, ArtigosGenericos


class ArtigoPrincipalAdmin(admin.ModelAdmin):
    list_display = ("titulo", "texto", "create_at", "update_at", "imagem")

class ArtigoSecundarioAdmin(admin.ModelAdmin):
    list_display = ("titulo", "texto", "create_at", "update_at", "imagem")

class ArtigoTerceiroAdmin(admin.ModelAdmin):
    list_display = ("titulo", "texto", "create_at", "update_at", "imagem")

class ArtigosRecommendsAdmin(admin.ModelAdmin):
    list_display = ("titulo", "texto", "create_at", "update_at", "imagem")

class ArtigosGenericosAdmin(admin.ModelAdmin):
    list_display = ("titulo", "texto", "create_at", "update_at", "imagem")

admin.site.register(ArtigoPrincipal, ArtigoPrincipalAdmin)
admin.site.register(ArtigoSecundario, ArtigoSecundarioAdmin)
admin.site.register(ArtigoTerceiro, ArtigoTerceiroAdmin)
admin.site.register(ArtigosRecommends, ArtigosRecommendsAdmin)
admin.site.register(ArtigosGenericos, ArtigosGenericosAdmin)