# Generated by Django 4.2.3 on 2023-07-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_is_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default=1, upload_to='profile', verbose_name='الصورة الشخصية'),
            preserve_default=False,
        ),
    ]
