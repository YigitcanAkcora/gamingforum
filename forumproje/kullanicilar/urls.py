from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('kayitol/', kayitol, name="kayitol"),
    path('girisyap/', girisyap, name='girisyap'),
    path('cikisyap/', cikisyap, name='cikisyap'),
    path('profil/', profiles_view, name="profiles_page"),
    path('profil/ekle/', profile_add_view, name="profile_add_page"),
    path('profil/edit/<slug:profil_slug>/',profile_edit, name= "profile_edit"),
    path('profil/changepass',change_password_view, name="profile_password"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)