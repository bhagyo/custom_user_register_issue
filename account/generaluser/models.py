from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_staff=False, is_admin=False, is_active=True, is_doctor=False):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        user_obj = self.model(
            email=self.normalize_email(email),
        )
        user_obj.username = username
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active

        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True
        )
        # user.staff = True # We can write this way also shown in line 39, this happened also like in line no. 52,53
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_admin=True
        )
        #user.staff = True
        #user.admin = True

        # uporer line duto evabe likha thik na

        user.save(using=self._db)
        return user

    def create_doctoruser(self, email, password):
        """
        Creates and saves a doctor user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            doctor=True,
            staff=True
        )
        user.save(using=self._db)
        return user
# hook in the New Manager to our Model


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(max_length=255, unique=True)  # blank=False, null=False)
    doctor = models.BooleanField(default=False)  # Whether this profile is a doctor or not
    #timestamp = models.DateTimeField(auto_add_now=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)  # a superuser
    # notice the absence of a "Password field", that's built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Email & Password are required by default.
    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    @property
    def is_doctor(self):
        "Is the user is a doctor or not?"
        return self.doctor
