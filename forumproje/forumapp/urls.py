from django.urls import path
from .views import *

app_name = 'forumapp'
urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    path('sorular/', SoruListView.as_view(), name="sorular"),
    path('sorular/<int:pk>/', SoruDetailView.as_view(), name="sorudetay"),
    path('sorular/olustur/', SoruCreateView.as_view(), name="soruolustur"),
    path('sorular/<int:pk>/guncelle/', SoruUpdateView.as_view(), name="soruguncelle"),
    path('sorular/<int:pk>/sil/', SoruDeleteView.as_view(), name="sorusil"),
    path('sorular/<int:pk>/yorum/', YorumYapView.as_view(), name= 'yorumyap')
] 
