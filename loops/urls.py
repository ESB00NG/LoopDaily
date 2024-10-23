from django.urls import path
from .views import loop_list, upload_loop, delete_loop, loop_detail, like_loop

# Definicion de las rutas URL para la aplicacion "loops"
urlpatterns = [
    # Ruta para la lista de loops, la pagina principal
    path('', loop_list, name='loop_list'),

    # Ruta para subir un nuevo loop
    path('upload/', upload_loop, name='upload_loop'),

    # Ruta para eliminar un loop especifico basado en su ID
    path('delete/<int:loop_id>/', delete_loop, name='delete_loop'),

    # Nueva URL para la vista de detalle de un loop especifico, identificado por su ID
    path('loop/<int:loop_id>/', loop_detail, name='loop_detail'),

    # Nueva URL para dar "like" a un loop, identificado por su ID
    path('like/<int:loop_id>/', like_loop, name='like_loop'),
]

