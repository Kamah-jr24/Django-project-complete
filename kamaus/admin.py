# from django.contrib import admin
from django.contrib import admin
from .models import SignUp, LoginAction, Contact

# Register the models to appear in the Django admin site
admin.site.register(SignUp)
admin.site.register(LoginAction)
admin.site.register(Contact)








