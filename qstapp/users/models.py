from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

# Create your models here.
how_use = (('teacher','インストラクター'), ('student', '受講者'))

class MyUserManager(models.Model):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

    def search(self, kwargs):
        qs = self.get_queryset()
        if kwargs.get('first_name', ''):
            qs = qs.filter(first_name__icontains=kwargs['first_name'])
        if kwargs.get('last_name', ''):
            qs = qs.filter(last_name__icontains=kwargs['last_name'])
        if kwargs.get('department', ''):
            qs = qs.filter(department__name=kwargs['department'])
        if kwargs.get('company', ''):
            qs = qs.filter(company__name=kwargs['company'])
        return qs

class CustomUser(AbstractBaseUser, PermissionsMixin):

    """
    Customized User model itself
    """
    username = models.CharField(_('username'), max_length=150, blank=True)
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    first_name = models.CharField(default='', max_length=60, blank=True)
    last_name = models.CharField(default='', max_length=60, blank=True)
    current_position = models.CharField(default='', max_length=64, blank=True)
    about = models.CharField(default='', max_length=255, blank=True)
    department = models.CharField(default='', max_length=128, blank=True)
    company = models.CharField(default='', max_length=128, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    
    objects = MyUserManager()


    def __str__(self):
        return self.email
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
