from django.contrib import admin
from .models import Category , Incomes , Expense

# Register your models here.

admin.site.register(Category)
admin.site.register(Incomes)
admin.site.register(Expense)
