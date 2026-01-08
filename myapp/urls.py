from django.urls import path
from .views import LoginView, RegisterView
from . import views as views

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),

    path('courses/', views.course_list_page, name='course_list'),
    path('courses/<int:course_id>/', views.course_detail_page),
    path('my-courses/', views.my_courses_page),
    path('lessons/<int:lesson_id>/', views.lesson_page),
]