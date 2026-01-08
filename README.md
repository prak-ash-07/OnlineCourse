OnlineCourse – Mini MOOC Platform

A simple MOOC-style online course platform built using Django and Django REST Framework, where users can register, log in, view courses, enroll, and track lesson progress.



Features

- User registration and login
- Course listing with short and long descriptions
- Course detail page with lessons
- Enroll in a course
- View lessons under a course
- Track lesson visit/progress per user
- REST APIs built using Django REST Framework
- Simple frontend using HTML, CSS, and JavaScript



Tech Stack

- Backend: Python, Django, Django REST Framework
- Frontend:HTML, CSS, JavaScript
- Database: PostgreSQL
- ORM:Django ORM
- Version Control:Git & GitHub



Project Structure

course/
│
├── course/ 
├── myapp/
│ └── static,templates folder
├── manage.py

Installation & Setup

pip install django 
djangorestframework
pip install psycopg[binary]     

Run process :

python manage.py runserver 1234
http://127.0.0.1:1234/


Application Flow 

Users can register and log in using a simple authentication system.
Courses are displayed on the course list page.
Each course has multiple lessons associated with it.
Logged-in users can enroll in courses.
When a user opens a lesson, the lesson visit is tracked in the database.

REST APIs are used to fetch course and lesson data.

Frontend communicates with backend APIs using JavaScript (fetch).

- POST /register/                     - Register a new user
- POST /login/                        - Login

- POST /courses/                      - Create course
- GET /courses/<course_id>/           - read course
- POST /courses/<course_id>/enroll/   - Enroll in a course
- GET /my-courses/                    - my list of course
- POST /api/enroll/                   – Enroll user in a course
- GET /lessons/<lesson_id>/           - View lesson and track progress



