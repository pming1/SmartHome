# coding=utf-8

from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question information', {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # 羅列出關聯的表的數據
    inlines = [ChoiceInline]
    # 羅列哪些字段內容
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # 字段過濾
    list_filter = ['pub_date', 'question_text']
    # 搜索哪個字段的內容
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
