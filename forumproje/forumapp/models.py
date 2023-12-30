from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Soru(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    baslik = models.CharField(max_length=10000)
    icerik = models.TextField(null=True, blank=True)
    olusturulma_zamani = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.kullanici.username} - Soru'
    
    def get_absolute_url(self):
        return reverse("forumapp:sorudetay", kwargs={"pk": self.pk})
    
    
class Yorum(models.Model):
    soru = models.ForeignKey(Soru, related_name="yorum", on_delete=models.CASCADE)
    kullaniciadi = models.CharField(max_length=100)
    icerik = models.TextField(null=True, blank=True)
    olusturulma_zamani = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.soru.baslik, self.soru.kullanici)
    
    def get_absolute_url(self):
        return reverse("forumapp:sorudetay", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)




