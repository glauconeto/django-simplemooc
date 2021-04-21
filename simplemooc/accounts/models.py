import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin,
    UserManager
)
from django.conf import settings

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nome de usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\\w.@+-]+$'),
            'O nome de usuário só pode conter letras, digitos ou os seguintes'
            ' caracteres: @/./+/-/_', 'invalid')]
    )

    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo ?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe ?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    
class PasswordReset(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name='Usuário',
        on_delete=models.CASCADE,
        related_name="reset"
    )
    key = models.CharField('Chave', max_length=100, unique=True)
    created_at = models.DateTimeField('Criado em ', auto_now_add=True)
    confirmed =  models.BooleanField("Confirmado?", default=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.created_at}"

    class Meta:
        verbose_name = 'Nova Senha'
        verbose_name_plural = 'Novas senhas'
        ordering = ['-created_at']