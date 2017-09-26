from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$', views.listar_pub, name='listar_pub'),
    url(r'^postear/(?P<pk>[0-9]+)/$', views.detalle_pub, name='postear'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publicar/$', views.publicar_post, name='publicar_post'),
    url(r'^post/(?P<pk>\d+)/borrar/$', views.borrar_post, name='borrar_post'),
]
