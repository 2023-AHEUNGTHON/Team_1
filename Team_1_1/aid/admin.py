from django.contrib import admin

from .models import Course, CourseTime, CourseMemo
from .models import Schedule, ScheduleTime, ScheduleMemo
from .models import Assignment, AssignmentMemo

# ----- 시간표 --------------------------------------------------------------------------------------------------------------------------------------------------------

# 시간표 메모 등록
class CourseInline(admin.TabularInline):
    model = CourseMemo

# 시간표 시간 추가등록
class CourseTimeInline(admin.TabularInline):
    model = CourseTime

# 시간표 등록
class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseInline, CourseTimeInline]
    
admin.site.register(Course, CourseAdmin)


# ----- 개인 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------

# 개인 일정 메모 등록
class ScheduleMemoInline(admin.TabularInline):
    model = ScheduleMemo

# 개인 일정 시간 추가등록
class ScheduleTimeInline(admin.TabularInline):
    model = ScheduleTime

# 개인 일정 등록
class ScheduleAdmin(admin.ModelAdmin):
    inlines = [ScheduleTimeInline, ScheduleMemoInline]

admin.site.register(Schedule, ScheduleAdmin)


# ----- 과제 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------

# 과제 일정 메모 등록
class AssignmentInline(admin.TabularInline):
    model = AssignmentMemo

# 과제 일정 등록
class AssignmentAdmin(admin.ModelAdmin):
    inlines = [AssignmentInline]
    
admin.site.register(Assignment, AssignmentAdmin)