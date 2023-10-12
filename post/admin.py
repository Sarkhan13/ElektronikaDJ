from django.contrib import admin
from .models import *

class phone_inline(admin.StackedInline):
    model = Phone
    extra = 0

class photo_inline(admin.TabularInline):
    model = images
    extra = 3

class note_inline(admin.StackedInline):
    model = Notebook
    extra = 0

class prod_inline(admin.ModelAdmin):
    list_display=('name','price','date','user')
    inlines = [phone_inline,note_inline, photo_inline]
    


admin.site.register(Category)

admin.site.register(Product,prod_inline)
admin.site.register(Phone)
admin.site.register(specialshop)
admin.site.register(images)
admin.site.register(Notebook)

