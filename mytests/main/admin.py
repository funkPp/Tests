
from django.contrib import admin
from .models import Tests, Tasks, Answers, Result
admin.site.register(Tests)
admin.site.register(Tasks)
admin.site.register(Answers)
admin.site.register(Result)

class AnswersAdmin(admin.ModelAdmin):
    list_display = ('desc', 'true')
    ordering = ['task', 'id']