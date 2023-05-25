from django.urls import path
from usuarios.api.api import user_api_view , user_detail_view, rol_api_view , rol_detail_view

urlpatterns = [
    path('usuarios/',user_api_view, name = 'usuario_api'),
    path('usuario/<int:pk>',user_detail_view, name = 'usuario_detail_api'),
    path('roles/',rol_api_view, name = 'rol_api'),
    path('rol/<int:pk>',rol_detail_view, name = 'rol_detail_api')

]