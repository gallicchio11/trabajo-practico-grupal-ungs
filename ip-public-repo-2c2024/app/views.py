# capa de vista/presentación

from django.shortcuts import redirect, render
from .layers.services import services
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def index_page(request):
    return render(request, 'index.html')

# esta función obtiene 2 listados que corresponden a las imágenes de la API y los favoritos del usuario, y los usa para dibujar el correspondiente template.
# si el opcional de favoritos no está desarrollado, devuelve un listado vacío.
def home(request):
    images = services.getAllImages()
    favourite_list = []
    
    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })

def search(request):
    search_msg = request.POST.get('query', '')

    # si el texto ingresado no es vacío, trae las imágenes y favoritos desde services.py,
    # y luego renderiza el template (similar a home).

    if (search_msg != ''):
        # si es distinto a nada, realiza la busqueda de imagenes con  el "search_msg"
        images = services.getAllImages(search_msg)
        favourite_list = []
    else:
        # sino no la realiza con "search_msg"
        images = services.getAllImages()
        favourite_list = []
    #retorna el renderizado con images y favourite_list
    return render(request, 'home.html', { 'images': images, 'favourite_list': favourite_list })




# Estas funciones se usan cuando el usuario está logueado en la aplicación.
@login_required
def getAllFavouritesByUser(request):
    favourite_list = []
    return render(request, 'favourites.html', { 'favourite_list': favourite_list })

@login_required
def saveFavourite(request):
    pass

@login_required
def deleteFavourite(request):
    pass

@login_required
def exit(request):
    logout(request)
    return redirect("/")
 
#vista que redirige a el archivo register.html
def register(request):
    return render(request, 'registration/register.html')  # Ajusta el nombre de la plantilla

from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    # el si la reques es POST recibe las variables del fomulario register
    if request.method == 'POST':
        name = request.POST['name']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['mail']
        password = request.POST['password']

        # verifico por terminal
        print("Datos recibidos:", name, lastname, username, email, password)
        
        # validaar si no se repiten los datos
        if User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está registrado.')
            return redirect('register')
        
        # instancio un usuario con los datos del registro
        user = User.objects.create_user(
            first_name=name,
            last_name=lastname,
            username=username,
            email=email,
            password=password
        )
        #guardo el nuevo usuario registRado
        user.save()
        
        #mensaje de registro  exitoso 
        messages.success(request, 'Registro exitoso')
    
    #por defecto redirije a register devuelta
    return render(request, 'registration/register.html')


#vista de usuario admin
from django.contrib.auth.decorators import user_passes_test
from app.admin_model import is_superuser

#funcion que requiere que sea un super_usuario
@user_passes_test(is_superuser)
def list_users(request):
    # si no es un admin el que intenta acceder redirije al inicio
    if not request.user.is_superuser:
        messages.error(request, "No tienes permisos para acceder a esta página.")
        return redirect('home')  # Redirige a la página principal u otra que prefieras
    
    #obtengo un listado de todos los usuarios
    users = User.objects.all()
    #retorna el renderizado de todos los usuarios a user_list.html
    return render(request, 'user_list.html', {'users': users})