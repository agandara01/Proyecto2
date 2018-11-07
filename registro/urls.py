

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.formulario, name="formulario"),
    path('registro/crear',views.crear,name="crear"),
    path('registro/eliminar/<int:id>',views.eliminar,name="eliminar"),
    path('registro/editar',views.editar,name="editar"),
    path('login',views.login,name="login"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),
    path('login/iniciar',views.login_iniciar,name="iniciar"),
    path('inicio',views.inicio,name="inicio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

