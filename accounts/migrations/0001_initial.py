# Generated by Django 4.2.3 on 2023-07-15 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='الاسم')),
                ('how_i', models.TextField(max_length=300, verbose_name='من انا')),
                ('price', models.IntegerField(max_length=5, verbose_name='سعر الكشف')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
