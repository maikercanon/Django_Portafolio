from django.urls import path
from .views import mis_posts, post_detail
#esta variable de namespace es para llamasr las urls de mi blog
app_name='blog'
urlpatterns=[
    #estas son las rutas de mi blog, las escribo aqui
    #y con la funcion de include de urls principal 
    #no necesito redenderizar mas
    path('',mis_posts,name='posts'),
    #aqui utilizo una convercion de tipo '<>' que arroja un parametro entero, y llama a uma funcion vista
    #este parametro se le pasara a la vista funcion post_detail
    path('<int:post_id>', post_detail, name='post_detail')
]