from rest_framework import viewsets, status

from .models import Course, CourseTime, CourseMemo
from .models import Schedule, ScheduleTime, ScheduleMemo
from .models import Assignment, AssignmentMemo

from .serializers import CourseSerializer, CourseTimeSerializer, CourseMemoSerializer, CourseListSerializer
from .serializers import ScheduleSerializer, ScheduleTimeSerializer, ScheduleMemoSerializer, ScheduleListSerializer
from .serializers import AssignmentSerializer, AssignmentMemoSerializer, AssignmentListSerializer


from rest_framework.response import Response
from rest_framework.views import APIView

# ----- 시간표 --------------------------------------------------------------------------------------------------------------------------------------------------------

# 시간표 등록
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# 개인 일정 시간 추가등록
class CourseTimeViewSet(viewsets.ModelViewSet):
    queryset = CourseTime.objects.all()
    serializer_class = CourseTimeSerializer

# 시간표 메모 등록
class CourseMemoViewSet(viewsets.ModelViewSet):
    queryset = CourseMemo.objects.all()
    serializer_class = CourseMemoSerializer

# 시간표 목록
class CourseListAPIView(APIView):
    queryset = Course.objects.all()
    def get(self,request):
        coures = Course.objects.all()
        serializer = CourseListSerializer(coures, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    

# ----- 개인 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------


# 개인 일정 등록
class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

# 개인 일정 시간 추가등록
class ScheduleTimeViewSet(viewsets.ModelViewSet):
    queryset = ScheduleTime.objects.all()
    serializer_class = ScheduleTimeSerializer

# 개인 일정 메모 등록
class ScheduleMemoViewSet(viewsets.ModelViewSet):
    queryset = ScheduleMemo.objects.all()
    serializer_class = ScheduleMemoSerializer
    
# 개인 일정 목록
class ScheduleListAPIView(APIView):
    queryset = Schedule.objects.all()
    def get(self,request):
        Schedules = Schedule.objects.all()
        serializer = ScheduleListSerializer(Schedules, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)


# ----- 과제 일정 -----------------------------------------------------------------------------------------------------------------------------------------------------

# 과제 일정 등록
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

# 과제 일정 메모 등록
class AssignmentMemoViewSet(viewsets.ModelViewSet):
    queryset = AssignmentMemo.objects.all()
    serializer_class = AssignmentMemoSerializer
    
# 과제 일정 목록
class AssignmentListAPIView(APIView):
    queryset = Assignment.objects.all()
    def get(self,request):
        Assignments = Assignment.objects.all()
        serializer = AssignmentListSerializer(Assignments, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)