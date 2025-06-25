from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings

ROLE_CHOICES = (
    ('admin', 'Admin'),
    ('staff', 'Staff'),
    ('student', 'Student'),
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, phonenumber, userid, password=None, role=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not userid:
            raise ValueError("Users must have a user ID")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phonenumber=phonenumber,
            userid=userid,
            role=role
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phonenumber, userid, password=None):
        user = self.create_user(
            email=email,
            name=name,
            phonenumber=phonenumber,
            userid=userid,
            password=password,
            role='admin'
        )
        user.is_admin = True
        user.is_superuser = True  # ✅ REQUIRED for Django admin
        user.is_staff = True      # ✅ Needed if you want admin site access
        user.save(using=self._db)
        return user


# ✅ Custom User Model
class MyUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=15)
    userid = models.CharField(max_length=50, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # ✅ REQUIRED
    is_staff = models.BooleanField(default=False)      # ✅ REQUIRED

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'phonenumber', 'userid']

    def __str__(self):
        return self.userid

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin


# ✅ Student Model
class Student(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=20)

    def __str__(self):
        return f"Student: {self.user.name}"


# ✅ Staff Model
class Staff(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"Staff: {self.user.name}"

class StudentRegistr(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    student_class = models.CharField(max_length=50)
    address = models.TextField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

