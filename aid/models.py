from django.db import models

# ----- 시간표 --------------------------------------------------------------------------------------------------------------------------------------------------------

# 시간표 등록
class Course(models.Model):
    DAY_CHOICES = (
        ('월', '월요일'),
        ('화', '화요일'),
        ('수', '수요일'),
        ('목', '목요일'),
        ('금', '금요일'),
        ('토', '토요일'),
        ('일', '일요일'),
    )
    
    c_name = models.CharField(max_length=255)
    c_date = models.DateField()
    c_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    c_time = models.TimeField()

# 시간표 시간 추가등록
class CourseTime(models.Model):
    DAY_CHOICES = [
        ('월', '월'),
        ('화', '화'),
        ('수', '수'),
        ('목', '목'),
        ('금', '금'),
        ('토', '토'),
        ('일', '일'),
    ]

    ct_schedule = models.ForeignKey(Course, related_name='course_times', on_delete=models.CASCADE)
    ct_day = models.CharField(max_length=3, choices=DAY_CHOICES)
    ct_start_time = models.TimeField()
    ct_end_time = models.TimeField()

# 시간표 메모 등록
class CourseMemo(models.Model):
    cm_work = models.ForeignKey(Course, related_name='course_memos', on_delete=models.CASCADE)
    cm_memo = models.CharField(max_length=255)



# ----- 개인 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------

# 개인 일정 등록
class Schedule(models.Model):
    CATEGORY_CHOICES = [
        ('운동', '운동'),
        ('약속', '약속'),
        ('여행', '여행'),
        ('회의', '회의'),
        ('기타', '기타'),
    ]
    
    DAY_CHOICES = [
        ('월', '월'),
        ('화', '화'),
        ('수', '수'),
        ('목', '목'),
        ('금', '금'),
        ('토', '토'),
        ('일', '일'),
    ]
    
    s_category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    s_name = models.CharField(max_length=255)
    s_week = models.CharField(max_length=3, choices=DAY_CHOICES)
    s_start_time = models.TimeField()
    s_end_time = models.TimeField()

# 개인 일정 시간 추가등록
class ScheduleTime(models.Model):
    DAY_CHOICES = [
        ('월', '월'),
        ('화', '화'),
        ('수', '수'),
        ('목', '목'),
        ('금', '금'),
        ('토', '토'),
        ('일', '일'),
    ]

    st_schedule = models.ForeignKey(Schedule, related_name='schedule_times', on_delete=models.CASCADE)
    st_day = models.CharField(max_length=3, choices=DAY_CHOICES)
    st_start_time = models.TimeField()
    st_end_time = models.TimeField()

# 개인 일정 메모 등록
class ScheduleMemo(models.Model):
    sm_schedule = models.ForeignKey(Schedule, related_name='schedule_memos', on_delete=models.CASCADE)
    sm_memo = models.CharField(max_length=255)



# ----- 과제 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------

# 과제 일정 등록
class Assignment(models.Model):
    DAY_CHOICES = (
        ('월', '월요일'),
        ('화', '화요일'),
        ('수', '수요일'),
        ('목', '목요일'),
        ('금', '금요일'),
        ('토', '토요일'),
        ('일', '일요일'),
    )
    
    a_name = models.CharField(max_length=255)
    a_date = models.DateField()
    a_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    a_deadline = models.TimeField()


# 과제 일정 메모 등록
class AssignmentMemo(models.Model):
    am_assignment = models.ForeignKey(Assignment, related_name='assignment_memos', on_delete=models.CASCADE)
    am_memo = models.CharField(max_length=255)

