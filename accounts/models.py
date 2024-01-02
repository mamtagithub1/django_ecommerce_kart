from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
class MyAccountmanager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,password=None):
        if not email:
            raise ValueError('Enter Correct E-Mail Address/Id! ')
        if not username:
            raise ValueError('Must Provide with Valid Username! ')
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,) 
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,password):
        user=self.create_user(
             email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,) 
        # Now cuz we are creating user we need to make this required fields True
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user
      


# Below is custom user model
class Account(AbstractBaseUser): 
    # we will need 5 fields-- 
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50)
    # cuz this is custom user model,we have to mention some required fields here
    # required fields
    date_join=models.DateTimeField(auto_now_add=True)
    last_login=models.DateField(auto_now_add=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superadmin=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    # when we write username='email,then we will be able to login with email-address
    REQUIRED_FIELDS=['username','first_name','last_name']

    # to operate MyAccount Manger with MyAccount we need to call above class here
    objects=MyAccountmanager()

    def __str__(self):
        return self.email
    
    def has_perm(self,permission,obj=None):
        return self.is_admin
    
    def has_module_perms(self,add_label):
        return True