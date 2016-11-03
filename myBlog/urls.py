from django.conf.urls import url

from . import views

urlpatterns = [
    # Main Route
    url(r'^$', views.index, name='index'),
    # Sub Route
    url(r'^welcome/$', views.welcome, name='welcome')
]
