from django.shortcuts import render,redirect
from django.views.generic import TemplateView

class LoginView(TemplateView):
    template_name = "login.html"

class RegisterView(TemplateView):
    template_name = "register.html"

# class IndexView(TemplateView):
#     template_name = "index.html"

#     def dispatch(self, request, *args, **kwargs):
#         if not request.session.get("user_id"):
#             return redirect("/login/")
#         return super().dispatch(request, *args, **kwargs)


def login_page(request):
    return render(request, 'login.html')


def course_list_page(request):
    return render(request, 'courses.html')


def course_detail_page(request, course_id):
    return render(request, 'course_detail.html', {'course_id': course_id})


def my_courses_page(request):
    return render(request, 'my_courses.html')


def lesson_page(request, lesson_id):
    return render(request, 'lesson.html', {'lesson_id': lesson_id})
