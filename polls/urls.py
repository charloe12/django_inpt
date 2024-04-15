from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    #path('chat/<str:message>', views.chat, name='chat'),
    path('map/', views.map, name='map'),
    #path('chatbot/', views.chatbot, name='chatbot'),

    path('pricing/', views.pricing, name='pricing'),
    path('admin/station', views.station, name='station'),
    path('admin/addStation', views.addStation, name='addStation'),
    path('admin/editStation', views.editStation, name='editStation'),
    path('admin/deleteStation', views.deleteStation, name='deleteStation'),

]