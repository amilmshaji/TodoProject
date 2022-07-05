from django.contrib import admin

# Register your models here
from TodoApp.models import Task

admin.site.register(Task)