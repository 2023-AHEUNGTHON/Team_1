from rest_framework import serializers
from .models import Course, CourseTime, CourseMemo
from .models import Schedule, ScheduleTime, ScheduleMemo
from .models import Assignment, AssignmentMemo

# ----- 시간표 --------------------------------------------------------------------------------------------------------------------------------------------------------

# 시간표 메모 등록
class CourseMemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseMemo
        fields = '__all__'

# 시간표 시간 추가등록
class CourseTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseTime
        fields = '__all__'

# 시간표 등록
class CourseSerializer(serializers.ModelSerializer):
    course_times = CourseTimeSerializer(many=True, read_only=True)
    course_memos = CourseMemoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ('id', 'c_name', 'c_date', 'c_week', 'c_time', 'course_times', 'course_memos')
        
# 시간표 목록
class CourseListSerializer(serializers.ModelSerializer):
    course_times = CourseTimeSerializer(many=True, read_only=True)
    course_memos = CourseMemoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = ('id', 'c_name', 'c_date', 'c_week', 'c_time', 'course_times', 'course_memos')
        

# ----- 개인 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------

# 개인 일정 메모 등록
class ScheduleMemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleMemo
        fields = '__all__'

# 개인 일정 시간 추가등록
class ScheduleTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleTime
        fields = '__all__'

# 개인 일정 등록
class ScheduleSerializer(serializers.ModelSerializer):
    schedule_times = ScheduleTimeSerializer(many=True, read_only=True)
    schedule_memos = ScheduleMemoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Schedule
        fields = ('id', 's_category', 's_name', 's_week',  's_start_time', 's_end_time', 'schedule_times', 'schedule_memos')
        

# 개인 일정 목록
class ScheduleListSerializer(serializers.ModelSerializer):
    schedule_times = ScheduleTimeSerializer(many=True, read_only=True)
    schedule_memos = ScheduleMemoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Schedule
        fields = ('id','s_category','s_name','s_week', 's_start_time', 's_end_time' ,'schedule_times', 'schedule_memos')
        


# ----- 과제 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------

# 과제 일정 메모 등록
class AssignmentMemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentMemo
        fields = '__all__'


# 과제 일정 등록
class AssignmentSerializer(serializers.ModelSerializer):
    assignment_memos = AssignmentMemoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Assignment
        fields = ('id', 'a_name', 'a_date', 'a_week', 'a_deadline', 'assignment_memos')
        
# 과제 일정 목록
class AssignmentListSerializer(serializers.ModelSerializer):
    assignment_memos = AssignmentMemoSerializer(many=True, read_only=True)
    
    class Meta:
        model = Assignment
        fields = ('id', 'a_name', 'a_date', 'a_week', 'a_deadline', 'assignment_memos')

