from django.contrib import admin
from django.urls import path, include
from saltodados import views
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings



router = routers.DefaultRouter()

router.register(r'ArtigoPrincipal', views.ArtigoPrincipalView, 'ArtigoPrincipal')
router.register(r'ArtigoSecundario', views.ArtigoSecundarioView, 'ArtigoSecundario')
router.register(r'ArtigoTerceiro', views.ArtigoTerceiroView, 'ArtigoTerceiro')
router.register(r'ArtigosGenericos', views.ArtigosGenericosView, 'ArtigosGenericos')
router.register(r'ArtigosRecommends', views.ArtigosRecommendsView, 'ArtigosRecommends')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
] 
 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)