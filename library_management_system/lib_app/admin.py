from django.contrib import admin
from .models import Add_a_book,Update_an_entry_of_a_book,Delete_a_book,Get_all_book
admin.site.register(Add_a_book)
admin.site.register(Update_an_entry_of_a_book)
admin.site.register(Delete_a_book)
admin.site.register(Get_all_book)

# Register your models here.
