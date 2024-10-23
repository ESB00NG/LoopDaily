from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from loops import views
from django.contrib.auth import views as auth_views

# Definicion de las rutas URL principales del proyecto
urlpatterns = [
    # Ruta para el panel de administracion de Django
    path('admin/', admin.site.urls),
    
    # Incluye las rutas definidas en la aplicacion "loops"
    path('loops/', include('loops.urls')),

    # Redirecciona la URL raiz (/) a la vista principal de "loops"
    path('', RedirectView.as_view(url='/loops/', permanent=True)),

    # Incluye las rutas relacionadas con la autenticacion de usuarios proporcionadas por Django
    path('accounts/', include('django.contrib.auth.urls')),

    # Ruta para la vista de registro de usuarios personalizada
    path('signup/', views.signup, name='signup'),

    # Ruta para la vista del perfil del usuario
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/', views.profile, name='profile_with_id'),

    # Ruta para cerrar sesion (logout)
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

