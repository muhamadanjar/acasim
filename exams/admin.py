from django.contrib import admin

# Register your models here.
class AdminQuiz(admin.ModelAdmin):
    list_display = ("title",)
