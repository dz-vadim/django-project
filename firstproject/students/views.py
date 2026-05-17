from django.views.generic import ListView, CreateView

from .forms import StudentForm
from .models import Student

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