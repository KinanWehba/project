# Generated by Django 4.2.3 on 2023-07-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_manager',
            field=models.BooleanField(blank=True, null=True, verbose_name='مدير'),
        ),
    ]
