# capa de servicio/lógica de negocio

from ..persistence import repositories
from ..utilities import translator
from django.contrib.auth import get_user
#importamos las funcionalidades del archivo transport
from ..transport import transport


def getAllImages(input=None):
    # pedimos un listado crudo de imágenes a la API usando transport.py.
    json_collection = transport.getAllImages(input)

    # procesamos cada dato crudo, lo convertimos en una "Card" y lo guardamos en la lista de imágenes utilizando trnslator
    images = []
    for image in json_collection:
        images.append(translator.fromRequestIntoCard(image))
    return images

# añadir favoritos (usado desde el template 'home.html')
def saveFavourite(request):
    fav = '' # transformamos un request del template en una Card.
    fav.user = '' # le asignamos el usuario correspondiente.

    return repositories.saveFavourite(fav) # lo guardamos en la base.

# usados desde el template 'favourites.html'
def getAllFavourites(request):
    if not request.user.is_authenticated:
        return []
    else:
        user = get_user(request)

        favourite_list = [] # buscamos desde el repositories.py TODOS los favoritos del usuario (variable 'user').
        mapped_favourites = []

        for favourite in favourite_list:
            card = '' # transformamos cada favorito en una Card, y lo almacenamos en card.
            mapped_favourites.append(card)

        return mapped_favourites

def deleteFavourite(request):
    favId = request.POST.get('id')
    return repositories.deleteFavourite(favId) # borramos un favorito por su ID.