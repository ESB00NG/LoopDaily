from django.db import models
from django.contrib.auth.models import User

# Modelo que representa un loop de audio
class Loop(models.Model):
    title = models.CharField(max_length=100)  # Campo de texto para el titulo del loop, con un maximo de 100 caracteres
    description = models.TextField()  # Campo de texto largo para la descripcion del loop
    bpm = models.IntegerField(default=120)  # Campo numerico para el BPM (beats por minuto) con un valor predeterminado de 120
    escala = models.CharField(max_length=50, default='Fm')  # Campo de texto para la escala musical, con un maximo de 50 caracteres y valor predeterminado 'Fm'
    categoria = models.CharField(max_length=50, default='Trap')  # Campo de texto para la categoria o genero musical, con un maximo de 50 caracteres y valor predeterminado 'Trap'
    file = models.FileField(upload_to='loops/')  # Campo de archivo para subir el loop, los archivos se guardaran en la carpeta 'loops/'
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Campo de fecha y hora que se establece automaticamente cuando se sube el loop
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacion de clave foranea al modelo User, indicando que cada loop pertenece a un usuario especifico. Si el usuario se elimina, tambien se eliminan sus loops
    likes = models.ManyToManyField(User, related_name='loop_likes', blank=True)  # Relacion muchos-a-muchos con el modelo User, permitiendo que varios usuarios den 'likes' a un loop. El campo es opcional (puede estar en blanco)
    image = models.ImageField(upload_to='loop_images/', null=True, blank=True)
    def __str__(self):
        return self.title  # Metodo que define como se mostrara el objeto cuando se convierta en una cadena, en este caso, muestra el titulo del loop

    def total_likes(self):
        return self.likes.count()  # Metodo que retorna el numero total de 'likes' que tiene el loop


# Modelo que representa un comentario sobre un loop
class Comment(models.Model):
    loop = models.ForeignKey(Loop, related_name='comments', on_delete=models.CASCADE)  # Relacion de clave foranea al modelo Loop, indicando que cada comentario pertenece a un loop especifico. Si el loop se elimina, tambien se eliminan sus comentarios
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacion de clave foranea al modelo User, indicando que cada comentario pertenece a un usuario especifico. Si el usuario se elimina, tambien se eliminan sus comentarios
    text = models.TextField()  # Campo de texto largo para el contenido del comentario
    created_at = models.DateTimeField(auto_now_add=True)  # Campo de fecha y hora que se establece automaticamente cuando se crea el comentario

    def __str__(self):
        return f'Comment by {self.user.username} on {self.loop.title}'  # Metodo que define como se mostrara el objeto cuando se convierta en una cadena, mostrando quien hizo el comentario y en que loop

# Modelo que representa el perfil de un usuario
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relacion uno-a-uno con el modelo User
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)  # Campo de imagen para la foto de perfil, opcional (puede estar en blanco)

    def __str__(self):
        return self.user.username  # Metodo que define como se mostrara el objeto cuando se convierta en una cadena, en este caso, muestra el nombre de usuario
    
