#this is to save all the sites
# this should add in settings also because contex processsors available
from .models import categoty

def menu_links(request):
    links=categoty.objects.all() # links is a function name
    return dict(links=links)   # to covert to dictionary  dictis using