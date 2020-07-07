# from django import forms
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
# from django.contrib.auth.models import Group
from django.db import models


# custom import
# importing group class from django
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, commit=True):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        # groups = Group.objects.all()
        #         for grp in groups:
        #             print(grp)
        user.set_password(password)
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email, username,
        and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            commit=False
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=40, unique=True)
    username = models.CharField(max_length=50, unique=True)
    # first_name = models.CharField(max_length=50)
    #     last_name = models.CharField(max_length=50)
    #     group = models.CharField(max_length=60,verbose_name='group')
    #     group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    date_joined = models.DateTimeField(verbose_name='date joined', blank=True, null=True)
    last_login = models.DateTimeField(verbose_name='last login', blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_accounts = models.BooleanField(default=False)
    is_support = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)
    is_sales = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    object = UserManager()

    # define the custom permissions
    # related to User.
    #     class Meta:
    #
    #         permissions = (
    #             ("can_go_in_non_ac_bus", "To provide non-AC Bus facility"),
    #             ("can_go_in_ac_bus", "To provide AC-Bus facility"),
    #             ("can_stay_ac-room", "To provide staying at AC room"),
    #             ("can_go_dehradoon", "Trip to Dehradoon"),
    #             ("can_go_mussoorie", "Trip to Mussoorie"),
    #             ("can_go_haridwaar", "Trip to Haridwaar"),
    #             ("can_go_rishikesh", "Trip to Rishikesh"),)

    # Add other custom permissions according to need.


    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        #         return self.is_admin
        return True

    def has_module_perms(self, app_label):
        return True

