from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),        
    url(r'^test/$', views.test, name='test'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^music/$', views.music, name='music'),
    path(r'music/grupo/<pk>/', views.datosGrupo, name='datosGrupo'),
    path(r'music/album/<pk>/', views.datosAlbum, name='datosAlbum'),
    path(r'music/musico/<pk>/', views.datosMusico, name='datosMusico'),
    path(r'music/nuevoGrupo/', views.nuevoGrupo, name='nuevoGrupo'),
    path(r'music/nuevoAlbum/', views.nuevoAlbum, name='nuevoAlbum'),
    path(r'music/nuevoMusico/', views.nuevoMusico, name='nuevoMusico'),
    path(r'music/editarGrupo/(?\D<pk>)/', views.editGrupo, name='editGrupo'),
    path(r'music/editarAlbum/(?\D<pk>)/', views.editAlbum, name='editAlbum'),
    path(r'music/editarMusico/(?\D<pk>)/', views.editMusico, name='editMusico'),
    path(r'music/listarGrupos/', views.listarGrupos, name='listarGrupos'),
    path(r'music/listarAlbumes/', views.listarAlbumes, name='listarAlbumes'),
    path(r'music/listarMusicos/', views.listarMusicos, name='listarMusicos'),
    path(r'music/borrarGrupo/(?\D<pk>)/', views.borrarGrupo, name='borrarGrupo'),
    path(r'music/reclamaDatos/', views.reclamaDatos, name='reclamaDatos'),
#---Manejo de sesiones----------------------------------------------------------
    path(r'register/', views.signup, name='signup'),
    path(r'login/', views.login, name='login'),
    path(r'logout/', views.logout_view, name='logout'),

]

