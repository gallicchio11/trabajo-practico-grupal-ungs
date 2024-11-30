from django.contrib import admin
from django.contrib.auth.models import User

#cambio de nombre al archivo admin, por admin_model(no sabia que nombre ponerle) por que admin esta como palabra reservada


#si es usuario es un super_usuario(osea un admin) retorna la verificacion
def is_superuser(u):
    return u.is_superuser


