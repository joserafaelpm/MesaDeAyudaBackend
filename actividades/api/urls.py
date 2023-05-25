from django.urls import path
from actividades.api.api import actividad_api_view, actividad_detail_view, Categoria_api_view, Categoria_detail_view, Usuario_Actividad_api_view, Usuario_Actividad_detail_view

urlpatterns = [
    path('actividades/',actividad_api_view, name = 'actividad_api'),
    path('actividad/<int:pk>',actividad_detail_view, name = 'actividad_detail_api'),
    path('categorias/',Categoria_api_view, name = 'actividad_api'),
    path('categoria/<int:pk>',Categoria_detail_view, name = 'actividad_detail_api'),
    path('tecnicos/',Usuario_Actividad_api_view, name = 'tecnico_api'),
    path('tecnico/<int:pk>',Usuario_Actividad_detail_view, name = 'tecnico_api_detail_api')
]