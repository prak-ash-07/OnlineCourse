from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import UserAccount,Course, Lesson, Enrollment, LessonProgress, UserAccount
from .serializers import RegisterSerializer, LoginSerializer,CourseSerializer, LessonSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "User registered"}, status=201)
        return Response(serializer.errors, status=400)


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            try:
                user = UserAccount.objects.get(username=username)
                if check_password(password, user.password):
                    request.session['user_id'] = user.id
                    return Response({
                        "msg": "Login success",
                        "user_id": user.id
                    })
                else:
                    return Response({"error": "Invalid password"}, status=401)
            except UserAccount.DoesNotExist:
                return Response({"error": "User not found"}, status=404)

        return Response(serializer.errors, status=400)


def get_logged_user(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return None
    return UserAccount.objects.get(id=user_id)

class CourseListAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CourseDetailAPIView(APIView):
    def get(self, request, course_id):
        course = Course.objects.get(id=course_id)
        lessons = course.lessons.all()

        enrolled = False
        user = get_logged_user(request)
        if user:
            enrolled = Enrollment.objects.filter(user=user, course=course).exists()

        return Response({
            "course": CourseSerializer(course).data,
            "lessons": LessonSerializer(lessons, many=True).data,
            "enrolled": enrolled,
            "logged_in": bool(user)
        })


class EnrollAPIView(APIView):
    def post(self, request, course_id):
        user = get_logged_user(request)
        if not user:
            return Response({"error": "Login required"}, status=401)

        course = Course.objects.get(id=course_id)
        Enrollment.objects.get_or_create(user=user, course=course)

        return Response({"msg": "Enrolled successfully"})


class MyCoursesAPIView(APIView):
    def get(self, request):
        user = get_logged_user(request)
        if not user:
            return Response({"error": "Unauthorized"}, status=401)

        enrollments = Enrollment.objects.filter(user=user)
        courses = [e.course for e in enrollments]
        return Response(CourseSerializer(courses, many=True).data)


class LessonDetailAPIView(APIView):
    def get(self, request, lesson_id):
        user = get_logged_user(request)
        lesson = Lesson.objects.get(id=lesson_id)

        if user:
            LessonProgress.objects.get_or_create(
                user=user,
                lesson=lesson,
                defaults={"visited": True}
            )

        return Response(LessonSerializer(lesson).data)
    
    def post(self, request):
        serializer = LessonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
