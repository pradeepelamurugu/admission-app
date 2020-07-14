from django.shortcuts import render
from django.views.generic.detail import DetailView
from students.models import Student
# Create your views here.
from students.models import Student

def staff_view(request):
    all_students = Student.objects.all()
    return render(request, 'staff/staff_view.html', {'Students': all_students})

def staff_accept_view(request):

    obj= Student.objects.all()
    for stu in obj:
        if request.method == 'POST':
            if 'active' in request.POST :
                stu.status=active


                stu.save()
            if 'reject' in request.POST :
                stu.status = 'reject'


                stu.save()


        selectedstu = Student.objects.filter(status='accept')
        return render(request, "staff/students_selected.html", {"selectedStudents": selectedstu})

