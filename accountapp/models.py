from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models

from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, gender, password=None):
        if not email:
            raise ValueError('이메일을 입력해주세요.')

        user = self.model(
            email = self.normalize_email(email),
            date_of_birth = date_of_birth,
            username = username,
            gender = gender
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, date_of_birth, gender, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            username=username,
            gender=gender
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email',
        max_length=100,
        unique=True,
        primary_key=True
    )

    username = models.TextField(
        verbose_name='username',
        max_length=20
    )

    date_of_birth = models.DateField(
        verbose_name="date_of_birth"
    )

    gender = models.CharField(
        verbose_name='gender',
        max_length=10
    )

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'gender', 'date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_lable):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = "User_List"
        verbose_name = "사용자"
        verbose_name_plural = "사용자_리스트"
        # ordering = ('-registered_date',)