from django.shortcuts import render, redirect, get_object_or_404
from .models import Loop, UserProfile
from django.contrib.auth.models import User
from .forms import LoopForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from .forms import CommentForm
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile
from django.http import JsonResponse

# Vista para el registro de nuevos usuarios
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('upload_loop')  # Redirige a la vista de subir loops despues de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# Vista para mostrar el perfil de usuario, con registro obligatorio
@login_required
def profile(request):
    user_id = request.GET.get('user_id', request.user.id)  # Obtiene el ID del usuario a mostrar, por defecto es el usuario actual
    user = get_object_or_404(User, id=user_id)  # Obtiene el usuario o muestra un error 404 si no existe
    
    if user == request.user:  # Si el usuario es el mismo que esta autenticado
        if request.method == 'POST':
            profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
            if profile_form.is_valid():
                profile_form.save()
                return redirect('profile')  # Redirige al perfil actual despues de actualizarlo
        else:
            profile_form = UserProfileForm(instance=request.user.userprofile)
    else:
        profile_form = None  # Si es otro usuario, no se muestra el formulario para actualizar el perfil

    user_loops = Loop.objects.filter(user=user)  # Obtiene todos los loops subidos por el usuario

    context = {
        'user': user,
        'profile_form': profile_form,
        'user_loops': user_loops
    }
    return render(request, 'profile.html', context)

# Vista para listar todos los loops disponibles
def loop_list(request):
    loops = Loop.objects.all()  # Obtiene todos los loops
    
    # Filtrado de loops basado en parametros de busqueda
    title = request.GET.get('title')
    bpm_min = request.GET.get('bpm_min')
    bpm_max = request.GET.get('bpm_max')
    escala = request.GET.get('escala')
    categoria = request.GET.get('categoria')
    propietario = request.GET.get('propietario')

    if title:
        loops = loops.filter(title__icontains=title)
    if bpm_min:
        loops = loops.filter(bpm__gte=bpm_min)
    if bpm_max:
        loops = loops.filter(bpm__lte=bpm_max)
    if escala:
        loops = loops.filter(escala=escala)
    if categoria:
        loops = loops.filter(categoria=categoria)
    if propietario:
        loops = loops.filter(user__username__icontains=propietario)

    # Ordenamiento de loops basado en el numero de likes, comentarios o fecha de subida
    ordenar_por = request.GET.get('ordenar_por')
    if ordenar_por == 'likes':
        loops = loops.annotate(total_likes=Count('likes')).order_by('-total_likes')
    elif ordenar_por == 'comentarios':
        loops = loops.annotate(total_comentarios=Count('comments')).order_by('-total_comentarios')
    elif ordenar_por == 'fecha':
        loops = loops.order_by('-uploaded_at')

    context = {
        'loops': loops,
        'escalas': Loop.objects.values_list('escala', flat=True).distinct(),
        'categorias': Loop.objects.values_list('categoria', flat=True).distinct(),
    }
    return render(request, 'loop_list.html', context)

# Vista para subir un nuevo loop, solo accesible para usuarios autenticados
@login_required
def upload_loop(request):
    if request.method == 'POST':
        form = LoopForm(request.POST, request.FILES)  # Asegúrate de pasar request.FILES
        if form.is_valid():
            loop = form.save(commit=False)
            loop.user = request.user  # Asocia el loop con el usuario actual
            loop.save()  # Guarda el loop, incluyendo la imagen
            return redirect('loop_list')
    else:
        form = LoopForm()
    return render(request, 'upload_loop.html', {'form': form})

# Vista para borrar un loop, solo accesible para usuarios autenticados
@login_required
def delete_loop(request, loop_id):
    loop = get_object_or_404(Loop, id=loop_id)  # Obtiene el loop o muestra un error 404 si no existe
    
    # Verifica si el loop pertenece al usuario actual
    if loop.user != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este loop.")

    if request.method == 'POST':
        loop.delete()  # Elimina el loop
        return redirect('loop_list')  # Redirige a la lista de loops
    
    return render(request, 'confirm_delete.html', {'loop': loop})

# Vista para ver los detalles de un loop y sus comentarios
def loop_detail(request, loop_id):
    loop = get_object_or_404(Loop, id=loop_id)  # Obtiene el loop o muestra un error 404 si no existe
    comments = loop.comments.all()  # Obtiene todos los comentarios del loop

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.loop = loop  # Asocia el comentario con el loop
            comment.user = request.user  # Asocia el comentario con el usuario actual
            comment.save()  # Guarda el comentario en la base de datos
            return redirect('loop_detail', loop_id=loop.id)  # Redirige a los detalles del loop
    else:
        form = CommentForm()

    context = {
        'loop': loop,
        'comments': comments,
        'form': form,
    }
    return render(request, 'loop_detail.html', context)

# Vista para dar "Me gusta" a un loop, solo accesible para usuarios autenticados
@login_required
def like_loop(request, loop_id):
    loop = get_object_or_404(Loop, id=loop_id)  # Obtiene el loop o muestra un error 404 si no existe
    liked = False
    if loop.likes.filter(id=request.user.id).exists():
        loop.likes.remove(request.user)  # Si el usuario ya dio "Me gusta", se lo quita
    else:
        loop.likes.add(request.user)  # Si no, se le agrega el "Me gusta"
        liked = True
    
    # Devolver la respuesta en formato JSON para manejarlo con JavaScript
    return JsonResponse({
        'status': 'ok',
        'liked': liked,
        'total_likes': loop.likes.count()
    })

# Señal para crear un perfil de usuario cuando se crea un nuevo usuario
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Señal para guardar el perfil de usuario cuando se guarda un usuario
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
