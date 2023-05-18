import uuid

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from api.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, default="")
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    CHOICES_PROFESSION = (
        ("ST", "Student"),
        ("TE", "Teacher"),
        ("CH", "Chairman")
    )
    profession = models.CharField(
        choices=CHOICES_PROFESSION,
        default="ST",
        null=False,
        blank=False
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.password:
            self.password = str(uuid.uuid4()).replace('-', '')
        super(User, self).save(*args, **kwargs)

    @property
    def get_teacher(self):
        if hasattr(self, "teacher"):
            return self.teacher
        return None

    @property
    def get_student(self):
        if hasattr(self, "student"):
            return self.student
        return None

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
