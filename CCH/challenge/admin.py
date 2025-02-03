from django.contrib import admin
from challenge.models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)

# Register the Question model with the QuestionAdmin
admin.site.register(Question, QuestionAdmin)