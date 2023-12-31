# Generated by Django 4.2.3 on 2023-07-18 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='how_i',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='المحافظة'),
        ),
        migrations.AddField(
            model_name='profile',
            name='address_detail',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='العنوان بالتفصيل'),
        ),
        migrations.AddField(
            model_name='profile',
            name='number_phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='رقم الهاتف'),
        ),
        migrations.AddField(
            model_name='profile',
            name='specialist_res',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='متخصص في'),
        ),
        migrations.AddField(
            model_name='profile',
            name='subtitle',
            field=models.CharField(default=1, max_length=250, verbose_name='نبذة عنك'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='waiting_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='ساعات الانتظار'),
        ),
        migrations.AddField(
            model_name='profile',
            name='working_time',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ساعات العمل'),
        ),
    ]
