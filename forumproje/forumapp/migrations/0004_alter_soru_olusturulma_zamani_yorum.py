# Generated by Django 4.2.8 on 2023-12-19 20:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forumapp', '0003_alter_soru_kullanici'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soru',
            name='olusturulma_zamani',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullaniciadi', models.CharField(max_length=100)),
                ('icerik', models.TextField(blank=True, null=True)),
                ('olusturulma_zamani', models.DateTimeField(default=django.utils.timezone.now)),
                ('soru', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorum', to='forumapp.soru')),
            ],
        ),
    ]
