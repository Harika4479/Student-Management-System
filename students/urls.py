
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    path('signup/', views.signup, name='signup'),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),

    path('register/', views.register_student, name='register'),

    path('student/<int:student_id>/', views.student_detail, name='student_detail'),

    path('delete/<int:student_id>/', views.delete_student, name='delete_student'),

    path('students/', views.student_list, name='student_list'),

    # Course Management
    path('courses/', views.manage_courses, name='manage_courses'),

    path('courses/add/', views.add_course, name='add_course'),

    path('courses/delete/<int:course_id>/', views.delete_course, name='delete_course'),

    path('inactive-students/', views.inactive_students, name='inactive_students'),

    path(
    'student/<int:student_id>/toggle-status/',
    views.toggle_student_status,
    name='toggle_student_status'
),

path('attendance/', views.mark_attendance, name='mark_attendance'),

path('attendance/report/', views.attendance_report, name='attendance_report'),
path('student/<int:student_id>/edit/', views.edit_student, name='edit_student'),
]
