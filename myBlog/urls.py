from django.conf.urls import url

from . import views

urlpatterns = [
    # Main Root
    url(r'^$', views.index, name='index'),
    # Sub Root
    url(r'^/welcome/$', views.welcome, name='welcome')
]
