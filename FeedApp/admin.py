from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Profile)
admin.site.register(Relationship)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
