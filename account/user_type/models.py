# eta all general_user er model

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# A class for general user (doctor+patient)

CustomUserModel = settings.AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


class Doctor(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    bmdc = models.IntegerField(null=False, blank=False)


class Patient(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    disease = models.TextField()


'''
Todo List:

Patient profile update korte hobe]
Doctor model ready hoy nai

'''


@receiver(post_save, sender=CustomUserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    if instance.doctor:
        Doctor.objects.create(user=instance)
    else:
        Patient.objects.create(user=instance)
    instance.profile.save()


'''
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
'''
