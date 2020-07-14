from django.shortcuts import render
from .forms import StudentcreateForm
from .models import Student
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)


def student_create_view(request):
    if request.method == "POST":
        form = StudentcreateForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            phone_num = request.POST["phone_num"]
            age = request.POST["age"]
            school_name = request.POST["school_name"]
            tenth_mark = request.POST["tenth_mark"]
            twelth_mark = request.POST["twelth_mark"]
            email = request.POST["email"]
            student_info = Student(name=name, phone_num=phone_num, age=age,school_name=school_name,tenth_mark=tenth_mark,twelth_mark=twelth_mark,email=email)
            student_info.save()
            return render(request, 'students/success.html')

    else:
        form = StudentcreateForm()
    return render(request, 'students/student_create.html', {'form': form})




def welcome(request):
    return render(request, 'students/welcome.html')



