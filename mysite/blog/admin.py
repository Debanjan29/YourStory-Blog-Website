from django.contrib import admin

from .models import Contact
from .models import Post
from .models import PostComments

admin.site.register(Contact)
admin.site.register(Post)
admin.site.register(PostComments)

# Register your models here. Without Registering the model after making it in Installed Apps COMPULSORY so that the Model is registered in admin
