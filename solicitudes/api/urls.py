from django.urls import path
from solicitudes.api.api import (
    Estado_api_view, 
    Estado_detail_view, 
    Rol_estado_api_view, 
    Rol_estado_detail_view, 
    Solicitud_api_view, 
    Solicitud_detail_view
    )

urlpatterns = [
    path('estados/',Estado_api_view, name = 'estados_api'),
    path('estado/<int:pk>',Estado_detail_view, name = 'estado_detail_view'),
    path('rolesEstados/',Rol_estado_api_view, name = 'Rol_estado_api_view'),
    path('rolEstado/<int:pk>',Rol_estado_detail_view, name = 'Rol_estado_detail_view'),
    path('solicitudes/',Solicitud_api_view, name = 'Solicitud_api_view'),
    path('solicitud/<int:pk>',Solicitud_detail_view, name = 'Solicitud_detail_view')
]