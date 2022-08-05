from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index),
    path('', views.index , name='zxc'),

    path('course/', views.course),
    path('members/', views.members),
    path('developers/', views.developers, name ='contact'),
    
    path('second/', views.second, name='second'),

    path('phone/', views.phone , name='phone'),

    path('laptop/', views.laptop , name='laptop'),

    path('login/', views.login , name='login'),

    path('create/', views.create, name ='create'),

    path('<int:pk>/', views.DetailView.as_view(), name = 'detail'),

    path('<int:pk>/update', views.UpdateView.as_view(), name = 'update'),

    path('<int:pk>/delete', views.DeleteView.as_view(), name = 'delete'),
]
