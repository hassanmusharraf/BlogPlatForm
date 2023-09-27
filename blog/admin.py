from django.contrib import admin
from blog.models import *

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Comment)