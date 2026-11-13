from django.db import models
from django.shortcuts import render,redirect


class Course(models.Model):
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    profile_image = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.student_name

def manage_courses(request):
    courses = Course.objects.all()

    return render(
        request,
        'courses.html',
        {'courses': courses}
    )


def add_course(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')

        if course_name:
            Course.objects.create(
                course_name=course_name
            )

        return redirect('manage_courses')

    return render(request, 'add_course.html')


def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()

    return redirect('manage_courses')

class Attendance(models.Model):

    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES
    )

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.student_name} - {self.date} - {self.status}"