# from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model to track sign-up details
class SignUp(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      signup_date = models.DateTimeField(default=timezone.now)
      
      def __str__(self):
            return self.user.username

# Model to track login details
class LoginAction(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)
      login_date = models.DateTimeField(default=timezone.now)
      
      def __str__(self):
            
            return f'{self.user.username} logged in at {self.login_date}'

# Model to track contact submissions
class Contact(models.Model):
      name = models.CharField(max_length=100)
      email = models.EmailField()
      message = models.TextField()
      contact_date = models.DateTimeField(default=timezone.now)
      
      def __str__(self):
            
            return f'{self.name} ({self.email})'

