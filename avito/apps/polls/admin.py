from django.contrib import admin
from .models import Poll, Answer
 
 
class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 2

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'id', 'votes')

 
class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, 
            {'fields': ['title',]}
        ),
    ]
    inlines = [AnswerInline]
    list_display = ('title', 'id')
 
 
admin.site.register(Poll, PollAdmin)
admin.site.register(Answer, AnswerAdmin)