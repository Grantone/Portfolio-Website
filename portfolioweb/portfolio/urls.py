from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/(\d+)'), views.project, name = 'project'),
]
