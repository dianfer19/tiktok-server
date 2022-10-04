from fileinput import filename
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin, Group
from django.db import models
from django.forms import model_to_dict
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import os


def get_file_path(instance, file):
    ext = file.split('.')[-1]
    filename = "%s.%s" % (instance.id, ext)
    return os.path.join('avatar/', filename)


class User(AbstractUser, PermissionsMixin):
    email = models.EmailField(_('Correo'), unique=True)
    avatar = models.ImageField(
        upload_to=get_file_path, blank=True, verbose_name='Imagen', null=True)
    cellphone = models.CharField(
        max_length=10, blank=True, null=True, verbose_name='Número Celular')
    identificacion = models.CharField(
        max_length=13, blank=True, null=True, unique=True, verbose_name='Cédula o Ruc')
    razon_social = models.CharField(
        max_length=100, blank=True, null=True,  verbose_name='Nombre o Razon Social')
    address = models.CharField(max_length=200, blank=True, null=True)
    reference = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='Referencia')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True, verbose_name='Estado')
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def toJSON(self):
        item = model_to_dict(
            self, exclude=['password', 'groups', 'user_permissions', 'last_login'])
        item['tipo'] = {'id': self.tipo, 'name': self.get_tipo_display()}
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['estado'] = 'Activo' if self.is_active else 'Inactivo'
        return item

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.set_password(self.password)
        else:
            user = User.objects.get(pk=self.pk)
            if user.password != self.password:
                self.set_password(self.password)
        super().save(*args, **kwargs)

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('El correo es obligatorio'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # def create_superuser(self, email, password, **extra_fields):
    #     """
    #     Create and save a SuperUser with the given email and password.
    #     """
    #     extra_fields.setdefault('is_staff', True)
    #     extra_fields.setdefault('is_superuser', True)
    #     extra_fields.setdefault('is_active', True)
    #
    #     if extra_fields.get('is_staff') is not True:
    #         raise ValueError(_('Superuser must have is_staff=True.'))
    #     if extra_fields.get('is_superuser') is not True:
    #         raise ValueError(_('Superuser must have is_superuser=True.'))
    #     return self.create_user(email, password, **extra_fields)
