# Generated by Django 4.2.8 on 2023-12-14 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forumapp', '0002_soru_kullanici'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soru',
            name='kullanici',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
