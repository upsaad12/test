from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.accueil),
    url(r'^inscription/$',views.inscription),
    url(r'^enfant/$',views.ajoutEnfant),
    
]
