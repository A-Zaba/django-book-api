from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime
# from django.utils.translation import ugettextlazy as _


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    pass

