from django.urls import path
from .api_views import RegisterAPIView, LoginAPIView

from .api_views import *

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
   

    path('courses/', CourseListAPIView.as_view()),
    
    path('courses/<int:course_id>/', CourseDetailAPIView.as_view()),
    path('courses/<int:course_id>/enroll/', EnrollAPIView.as_view()),
    path('my-courses/', MyCoursesAPIView.as_view()),
    path('lessons/<int:lesson_id>/', LessonDetailAPIView.as_view()),
    path('lessons/', LessonDetailAPIView.as_view()), 
]