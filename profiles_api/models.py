from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager For User Profiles"""

    def create_user(self, email, name, password=None):
        """Create A New User Profile"""
        if not email:
            raise ValueError("User Must Have An Email!")
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """DataBase Model For Users In The System"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve Full Name Of User"""
        return self.name

    def get_short_name(self):
        """Retrieve Short Name Of User"""
        return self.name

    def __str__(self):
        """Retrieve Short Name Of User"""
        return self.email


class ProfileFeedItem(models.Model):
    """profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feed')
    status_txt = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_txt
