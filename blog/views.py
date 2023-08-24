from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.
def mis_posts(request):
    plasmar_en_html=Post.objects.all()
    return render(request, 'posts.html', {'post':plasmar_en_html})

def post_detail(request, post_id):
    #utilizo la funcion get_object_or_404 le paso el modelo y si no esta en la base de datos
    #el pk, osea el primarykey lance un error de no found
    existe_post=get_object_or_404(Post,pk=post_id)
    #esta funcion vista redenderiza la vista html y se le pasa el parametro post_id
    #que viene de el archivo url de la app blog
    return render(request, 'posts_detail.html', {'detail':existe_post} )