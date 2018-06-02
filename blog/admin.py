from django.contrib import admin
from .models import Post
#on utilise la ligne 4: To make our model visible on the admin page, we need to register the model
admin.site.register(Post)

# Register your models here.
