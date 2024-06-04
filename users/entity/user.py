from django.db import models
from helper.models.base_model import BaseModel
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager.user_manager import UserManager

class User(AbstractBaseUser,PermissionsMixin,BaseModel):
    
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=255,blank=True, null=True)
    last_name = models.CharField(max_length=255,blank=True, null=True)
    mobile_no = models.CharField(max_length=10)
    dob = models.DateField(verbose_name='date of birth',blank=True, null=True)
    login_access = models.BooleanField(default=True)
    locked_reason = models.TextField(blank=True, null=True)
    is_eligible_for_business = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_no']

    def get_tokens(self):
        """Returns a tuple of JWT tokens (token, refresh_token)"""
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token), str(refresh)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'