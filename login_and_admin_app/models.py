from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def registration_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # current_users = User.objects.filter(email=postData['email'])
        errors = {}
        if len(postData['first_name']) < 2:
            errors ['first_name'] = "First Name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors ['last_name'] = "Last Name should be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        current_users = User.objects.filter(email=postData['email'])
        if len(current_users) > 0:
            errors ['email'] = "That email is already in use"
        if len(postData['password']) < 8:
            errors ['password'] = "Password should be at least 8 characters long"
        if postData['password'] != postData['pw_confirm']:
            errors['pw_confirm'] = "Password and PW_Confirm did not match!"
        return errors

    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])
        print (existing_user)
        if len(postData['email']) == 0:
            errors ['email'] = "Email required"
        if len(postData['password']) < 8:
            errors ['password'] = "Password should be at least 8 characters long"
        if bcrypt.checkpw(postData['password'].encode(),existing_user[0].password.encode()) != True:
            errors['password'] = 'Email and password do not match'
        return errors

    

class User(models.Model):
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    password=models.CharField(max_length=12)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()



# Create your models here.
