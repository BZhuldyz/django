from django.shortcuts import render

# Create your views here.

from .models import Prepod, Student

def index(request):
    num_students=Student.objects.all().count()
    num_teachers=Prepod.objects.count()
    
   
    return render(
        request,
        'index.html',
        context={'num_students':num_students,'num_prepod':num_prepod},
    )
	
from django.views import generic

class StudentListView(generic.ListView):
    model = Student
    paginate_by = 2
class StudentDetailView(generic.DetailView):
    model = Student