from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from datetime import date

from .models import Student, Course, Attendance


# -------------------------
# DASHBOARD
# -------------------------

@login_required
def dashboard(request):

    total_students = Student.objects.count()

    active_students = Student.objects.filter(
        is_active=True
    ).count()

    inactive_students = Student.objects.filter(
        is_active=False
    ).count()

    total_courses = Course.objects.count()

    students = Student.objects.all()

    context = {
        'students': students,
        'total_students': total_students,
        'active_students': active_students,
        'inactive_students': inactive_students,
        'total_courses': total_courses,
    }

    return render(
        request,
        'accounts/dashboard.html',
        context
    )


# -------------------------
# STUDENT REGISTRATION
# -------------------------

@login_required
def register_student(request):

    if request.method == 'POST':

        student_name = request.POST.get('student_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')
        course = request.POST.get('course')
        profile_image = request.FILES.get('profile_image')

        Student.objects.create(
            student_name=student_name,
            email=email,
            mobile_number=mobile_number,
            course=course,
            profile_image=profile_image
        )

        messages.success(
            request,
            'Student registered successfully!'
        )

        return redirect('student_list')

    return render(request, 'register.html')


# -------------------------
# STUDENT LIST
# -------------------------

@login_required
def student_list(request):

    students = Student.objects.all()

    return render(
        request,
        'student_list.html',
        {
            'students': students
        }
    )


# -------------------------
# STUDENT DETAILS
# -------------------------

@login_required
def student_detail(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    return render(
        request,
        'student_detail.html',
        {
            'student': student
        }
    )


@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.student_name = request.POST.get('student_name')
        student.email = request.POST.get('email')
        student.mobile_number = request.POST.get('mobile_number')
        student.course = request.POST.get('course')

        if request.FILES.get('profile_image'):
            student.profile_image = request.FILES['profile_image']

        student.save()

        messages.success(request, 'Student details updated successfully!')
        return redirect('student_list')

    courses = Course.objects.all()

    return render(request, 'edit_student.html', {
        'student': student,
        'courses': courses
    })
# -------------------------
# DELETE STUDENT
# -------------------------

@login_required
def delete_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == 'POST':

        student.delete()

        messages.success(
            request,
            'Student deleted successfully!'
        )

        return redirect('student_list')

    return redirect(
        'student_detail',
        student_id=student_id
    )


# -------------------------
# SIGNUP
# -------------------------

def signup(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                'accounts/signup.html',
                {
                    'error': 'Username already exists'
                }
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            'Account created successfully!'
        )

        return redirect('login')

    return render(
        request,
        'accounts/signup.html'
    )


# -------------------------
# LOGIN
# -------------------------

def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        return render(
            request,
            'accounts/login.html',
            {
                'error': 'Invalid username or password'
            }
        )

    return render(
        request,
        'accounts/login.html'
    )


# -------------------------
# LOGOUT
# -------------------------

@login_required
def user_logout(request):

    logout(request)

    return redirect('login')


# -------------------------
# COURSE LIST
# -------------------------

@login_required
def manage_courses(request):

    courses = Course.objects.all()

    return render(
        request,
        'course.html',
        {
            'courses': courses
        }
    )


# -------------------------
# ADD COURSE
# -------------------------
# ADD COURSE

@login_required
def add_course(request):

    if request.method == 'POST':

        course_name = request.POST.get('course_name')

        if course_name:
            Course.objects.create(
                course_name=course_name
            )

            messages.success(
                request,
                'Course added successfully!'
            )

            return redirect('manage_courses')

    return render(request, 'add_course.html')
# -------------------------
# DELETE COURSE
# -------------------------

@login_required
def delete_course(request, course_id):

    course = get_object_or_404(
        Course,
        id=course_id
    )

    if request.method == 'POST':

        course.delete()

        messages.success(
            request,
            'Course deleted successfully!'
        )

        return redirect('manage_courses')

    return redirect('manage_courses')

@login_required
def manage_courses(request):
    courses = Course.objects.all()
    return render(request, 'course.html', {'courses': courses})

@login_required
def inactive_students(request):
    students = Student.objects.filter(is_active=False)
    return render(request, 'inactive_students.html', {
        'students': students
    })


@login_required
def toggle_student_status(request, student_id):

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':

        student.is_active = not student.is_active

        student.save(update_fields=['is_active'])

        if student.is_active:
            messages.success(request, 'Student activated successfully!')
        else:
            messages.success(request, 'Student deactivated successfully!')

    return redirect('student_list')

@login_required
def mark_attendance(request):

    selected_date = request.GET.get(
        'date',
        timezone.localdate().isoformat()
    )

    students = Student.objects.filter(is_active=True)

    if request.method == 'POST':

        selected_date = request.POST.get('date')

        for student in students:

            status = request.POST.get(
                f'status_{student.id}'
            )

            if status in ['Present', 'Absent']:

                Attendance.objects.update_or_create(
                    student=student,
                    date=selected_date,
                    defaults={'status': status}
                )

        messages.success(
            request,
            'Attendance saved successfully!'
        )

        return redirect(
            f'/attendance/?date={selected_date}'
        )

    attendance_records = Attendance.objects.filter(
        date=selected_date
    )

    attendance_map = {
        record.student_id: record.status
        for record in attendance_records
    }

    for student in students:
        student.today_status = attendance_map.get(
            student.id, ''
        )

    return render(request, 'attendance.html', {
        'students': students,
        'selected_date': selected_date,
        'attendance_map': attendance_map
    })

@login_required
def attendance_report(request):

    selected_date = request.GET.get(
        'date',
        timezone.localdate().isoformat()
    )

    attendance_records = Attendance.objects.filter(
        date=selected_date
    ).select_related('student')

    present_count = attendance_records.filter(
        status='Present'
    ).count()

    absent_count = attendance_records.filter(
        status='Absent'
    ).count()

    return render(request, 'attendance_report.html', {
        'attendance_records': attendance_records,
        'selected_date': selected_date,
        'present_count': present_count,
        'absent_count': absent_count
    })
