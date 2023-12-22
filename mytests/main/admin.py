
from django.contrib import admin
from .models import Tests, Tasks, Answers, Result


@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('task', 'desc', 'true')

admin.site.register(Tests)
admin.site.register(Tasks)
admin.site.register(Result)