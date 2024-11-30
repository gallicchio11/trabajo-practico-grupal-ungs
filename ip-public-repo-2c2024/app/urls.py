from django.urls import path
from app import views
urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('login/', views.index_page, name='login'),
    path('home/', views.home, name='home'),
    path('buscar/', views.search, name='buscar'),

    # nuevo path para registro
    path('register/', views.register, name='register'),


    path('favourites/', views.getAllFavouritesByUser, name='favoritos'),
    path('favourites/add/', views.saveFavourite, name='agregar-favorito'),
    path('favourites/delete/', views.deleteFavourite, name='borrar-favorito'),

    #nuevo path para la lista de usuario del admin
    path('user_list/', views.list_users, name='user_list'),


    path('exit/', views.exit, name='exit'),
]