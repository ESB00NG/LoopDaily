from pathlib import Path

# Construye rutas dentro del proyecto como esta: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuraciones rapidas para el desarrollo - no adecuadas para produccion
# Ver https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# ADVERTENCIA DE SEGURIDAD: manten la clave secreta usada en produccion en secreto
SECRET_KEY = 'django-insecure-6w^6hogrg*4r#@@!e4#76t*dy-#!bn=qm_%xyuf-b)3%ko#=)6'

# ADVERTENCIA DE SEGURIDAD: no actives el debug en produccion
DEBUG = True

# Lista de hosts permitidos para tu aplicacion en produccion
ALLOWED_HOSTS = []


# Definicion de las aplicaciones instaladas

INSTALLED_APPS = [
    'django.contrib.admin',  # Administracion de Django
    'django.contrib.auth',  # Manejo de autenticacion y autorizacion
    'django.contrib.contenttypes',  # Manejo de tipos de contenido
    'django.contrib.sessions',  # Manejo de sesiones
    'django.contrib.messages',  # Manejo de mensajes flash
    'django.contrib.staticfiles',  # Manejo de archivos estaticos
    'loops',  # Tu aplicacion personalizada "loops"
]

# Definicion del middleware

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Seguridad
    'django.contrib.sessions.middleware.SessionMiddleware',  # Manejo de sesiones
    'django.middleware.common.CommonMiddleware',  # Funciones comunes
    'django.middleware.csrf.CsrfViewMiddleware',  # Proteccion contra CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Manejo de autenticacion
    'django.contrib.messages.middleware.MessageMiddleware',  # Manejo de mensajes
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Proteccion contra clickjacking
]

# Configuracion de la URL principal
ROOT_URLCONF = 'musicloops.urls'

# Configuracion de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Motor de plantillas de Django
        'DIRS': [],  # Directorios adicionales de plantillas (vacío porque usas APP_DIRS)
        'APP_DIRS': True,  # Busca plantillas dentro de las carpetas de las aplicaciones instaladas
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Contexto de depuración
                'django.template.context_processors.request',  # Contexto de la solicitud HTTP
                'django.contrib.auth.context_processors.auth',  # Contexto de autenticación
                'django.contrib.messages.context_processors.messages',  # Contexto de mensajes
            ],
        },
    },
]

# Configuracion de la aplicacion WSGI (para el despliegue en servidores web)
WSGI_APPLICATION = 'musicloops.wsgi.application'


# Configuracion de la base de datos
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos (SQLite en este caso)
        'NAME': BASE_DIR / 'db.sqlite3',  # Nombre de la base de datos (ruta del archivo SQLite)
    }
}


# Validadores de contraseñas
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # Valida la similitud de atributos del usuario
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Valida la longitud minima de la contraseña
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Valida contraseñas comunes
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Valida que no sea solo numerica
    },
]


# Configuracion de internacionalizacion
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es'  # Lenguaje predeterminado de la aplicacion

TIME_ZONE = 'UTC'  # Zona horaria predeterminada

USE_I18N = True  # Activa la internacionalizacion

USE_TZ = True  # Activa el manejo de zonas horarias


# Configuracion de archivos estaticos (CSS, JavaScript, Imagenes)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

MEDIA_URL = '/media/'  # URL para acceder a archivos subidos por el usuario
MEDIA_ROOT = BASE_DIR / 'media'  # Directorio donde se guardan los archivos subidos

STATIC_URL = '/static/'  # URL para archivos estaticos
STATICFILES_DIRS = [BASE_DIR / "static"]  # Directorios adicionales donde buscar archivos estaticos

# Tipo de campo predeterminado para claves primarias
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Tipo de campo predeterminado para claves primarias

# Redireccionamiento despues de iniciar y cerrar sesion
LOGIN_REDIRECT_URL = '/'  # Redirige a "Inicio" despues de iniciar sesion
LOGOUT_REDIRECT_URL = '/'  # Redirige a la pagina de inicio despues de cerrar sesion
