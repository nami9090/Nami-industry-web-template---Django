from django.urls import path
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('portfolio-details/<int:pk>/', views.portfolio, name='portfolio'),
    path('service-details/<int:pk>/', views.service, name='service'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'),
    path('produit', views.produit_viz, name='produit'),
    path('ajouter_produit', views.ajouter_image, name='ajouter_produit'),

    #not in use
    path('starter', views.starter_page, name='starter')
    #
]
handler404 = views.custom_404
