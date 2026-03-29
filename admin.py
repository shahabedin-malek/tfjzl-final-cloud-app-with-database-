from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Inline for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for Question
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Course Admin
class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('name',)

# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')

# Register models
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Submission)