from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin ,AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password, is_admin, is_staff, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        presentuser = self.model(email=email, is_superuser=is_admin, is_staff=is_staff, created_date=now)
        if(password != ''):
            presentuser.set_password(password)
        presentuser.save(using=self._db)
        return presentuser

    def create_user(self,email, **extra_fields):
        return self._create_user(email, '', False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)



class PresentUser(AbstractBaseUser,PermissionsMixin):

    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    email = models.EmailField('email address',unique=True, blank=True, null=True)
    mobile_number = models.CharField('Mobile Number',max_length=20,blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField('Gender',max_length=1,choices=GENDER_CHOICES, null=True, blank=True)
    created_date = models.DateTimeField('date joined', default=timezone.now)
    is_staff = models.BooleanField('is staff', default=False, )

    USERNAME_FIELD = 'email'
    objects =  CustomUserManager()

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name




