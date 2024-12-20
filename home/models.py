# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Personel(models.Model):

    #__Personel_FIELDS__
    ad = models.TextField(max_length=255, null=True, blank=True)
    soyad = models.TextField(max_length=255, null=True, blank=True)
    sicilno = models.TextField(max_length=255, null=True, blank=True)
    email = models.TextField(max_length=255, null=True, blank=True)
    dahili = models.TextField(max_length=255, null=True, blank=True)
    fotografyolu = models.TextField(max_length=255, null=True, blank=True)

    #__Personel_FIELDS__END

    class Meta:
        verbose_name        = _("Personel")
        verbose_name_plural = _("Personel")



#__MODELS__END
