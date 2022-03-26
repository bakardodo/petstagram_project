from django.contrib import admin

# Register your models here.
from petstagram.main.models import Pet, PetPhoto


class PetInlineAdmin(admin.StackedInline):
    model = Pet



@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')

@admin.register(PetPhoto)
class PetPhotoAdmin(admin.ModelAdmin):
    pass


