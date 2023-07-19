from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.utils.text import slugify

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name = models.CharField(_("الاسم"), max_length=50)
    subtitle = models.TextField(_("نبذة عنك"),max_length=250)
    address = models.CharField(_("المحافظة"),max_length=50,blank=True,null = True)
    address_detail = models.CharField(_("العنوان بالتفصيل"),max_length=250,blank=True,null = True)
    number_phone = models.CharField(_("رقم الهاتف"),max_length=50,blank=True,null = True)

    facebook = models.CharField(_("facebbok"),max_length=50,blank=True,null = True)
    twitter = models.CharField(_("twitter"),max_length=50,blank=True,null = True)
    google = models.CharField(_("google"),max_length=50,blank=True,null = True)




    working_time = models.CharField(_("ساعات العمل"),max_length=50,blank=True,null = True)
    waiting_time = models.IntegerField(_("ساعات الانتظار"),blank=True,null = True)
    specialist_res = models.CharField(_("متخصص في"),max_length=50,blank=True,null = True)
    price = models.IntegerField(_("سعر الكشف"),blank=True,null=True)    
    is_manager = models.BooleanField(_("مدير"),blank=True,null=True)
    image = models.ImageField(_("الصورة الشخصية"),upload_to="profile")
    slug =models.SlugField(_("slug"),blank=True,null = True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile,self).save(*args,**kwargs)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return "%s" %(self.user.username)
def create_profile (sender , **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile ,sender=User)
