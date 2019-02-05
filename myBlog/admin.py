from django.contrib import admin
from myBlog.models import post, author

# Register your models here.
admin.site.register(post)
admin.site.register(author)