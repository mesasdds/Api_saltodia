from django.contrib import admin
from django.urls import path, include
from saltodados import views
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'ArtigoPrincipal', views.ArtigoPrincipalView, 'ArtigoPrincipal')
router.register(r'ArtigoSecundario', views.ArtigoSecundarioView, 'ArtigoSecundario')
router.register(r'ArtigoTerceiro', views.ArtigoSecundarioView, 'ArtigoTerceiro')
router.register(r'ArtigosGenericos', views.ArtigosGenericosView, 'ArtigosGenericos')
router.register(r'ArtigosRecommends', views.ArtigosRecommendsView, 'ArtigosRecommends')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
