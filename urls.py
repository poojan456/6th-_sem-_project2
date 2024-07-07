from django.contrib import admin
from django.urls import path , include
from BTS import views
urlpatterns = [
    path('', views.home,name='home'),
    path('map', views.map,name='map'),
    path('search', views.search,name='search'),
    path('index', views.index, name='index'),
    #path('fetch-route-data/', views.fetch_route_data, name='fetch_route_data'),
    #path('form', views.form,name='form'),
    path('about',views.about,name='about'),
    #path('example',views.example,name='example'),
    path('get_route/', views.get_route, name='get_route'),
    path('check_departure/', views.check_departure, name='check_departure'),
    path('update_status/', views.update_status, name='update_status'),
    path('reset_status/', views.reset_status, name='reset_status'),
    path('swap_source_destination/', views.swap_source_destination, name='swap_source_destination'),
]