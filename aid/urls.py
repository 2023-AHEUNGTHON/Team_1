from django.urls import path, include
from rest_framework import routers

from .views import CourseViewSet, CourseTimeViewSet, CourseMemoViewSet, CourseListAPIView
from .views import ScheduleViewSet, ScheduleTimeViewSet, ScheduleMemoViewSet, ScheduleListAPIView
from .views import AssignmentViewSet, AssignmentMemoViewSet, AssignmentListAPIView

router = routers.DefaultRouter()

# ----- 시간표 --------------------------------------------------------------------------------------------------------------------------------------------------------

# 시간표 등록
router.register(r'c_post', CourseViewSet)

# 시간표 시간 추가등록
router.register(r'c_time', CourseTimeViewSet)

# 시간표 메모 등록
router.register(r'c_memo', CourseMemoViewSet)


# ----- 개인 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------


# 개인 일정 등록
router.register(r's_post', ScheduleViewSet)

# 개인 일정 시간 추가등록
router.register(r's_time', ScheduleTimeViewSet)

# 개인 일정 메모 등록
router.register(r's_memo', ScheduleMemoViewSet)


# ----- 과제 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------

# 과제 일정 등록
router.register(r'a_post', AssignmentViewSet)

# 과제 일정 메모 등록
router.register(r'a_memo', AssignmentMemoViewSet)







urlpatterns = [
    path('', include(router.urls)),
    path('c_list/',CourseListAPIView.as_view()),
    path('s_list/',ScheduleListAPIView.as_view()),
    path('a_list/',AssignmentListAPIView.as_view()),
]
