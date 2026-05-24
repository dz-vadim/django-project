from django.views.generic import ListView, CreateView, UpdateView

from .forms import StudentForm
from .models import Student, Teacher


class StudentListView(ListView):
    model = Student
    template_name = 'list.html'
    context_object_name = 'students'

from django.urls import reverse_lazy

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add.html'
    success_url = reverse_lazy('student_list')

from faker import Faker
import random

fake = Faker()

class LoadTestDataView(UpdateView):
    def get(self, request, *args, **kwargs):
        teachers = []

        for _ in range(3):
            teacher = Teacher.objects.create(
                name = fake.name(),
                experience_years = random.randint(1, 20),
            )
            teachers.append(teacher)