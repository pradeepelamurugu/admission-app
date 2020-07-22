from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic.detail import DetailView
from students.models import Student
# Create your views here.
from students.models import Student

def staff_view(request):
    all_students = Student.objects.all()
    return render(request, 'staff/staff_view.html', {'Students': all_students})
# def staff_view(request):
#     if request.method == 'GET':
#         all_students = Student.objects.all()
#         return render(request, 'staff/staff_view.html', {'Students': all_students})
#     if request.method == 'POST':
#         if 'active' in request.POST:
#             stu=get_object_or_404(stu,id=pk)
#             stu.status='active'
#             stu.save()
#     selectedstu = Student.objects.filter(status='accept')
#     return render(request, "staff/students_selected.html", {"selectedStudents": selectedstu})
#     if request.method == 'POST':
#         if 'reject' in request.POST:
#             stu = get_object_or_404(stu, id=pk)
#             stu.status = 'reject'
#             stu.save()
#     rejectedstu = Student.objects.filter(status='reject')
#     return render(request, "staff/students_rejected.html", {"rejectedStudents": rejectedstu})
# def staff_accept_view(request):
#
#     obj= Student.objects.all()
#     for stu in obj:
#         if request.method == 'POST':
#             if 'active' in request.POST :
#                 stu.status=active
#
#
#                 stu.save()
#             if 'reject' in request.POST :
#                 stu.status = 'reject'
#
#
#                 stu.save()
#
#
#         selectedstu = Student.objects.filter(status='accept')
#         return render(request, "staff/students_selected.html", {"selectedStudents": selectedstu})

# def accept_view(request,id):
#     if request.method == 'POST':
#         if 'active' in request.POST["accepted"]:
#             # stu=Student.objects.get(id=pk)
#             stu = get_object_or_404(Student, pk=id)
#             stu.status='active'
#             stu.save()
#     selectedstu = Student.objects.filter(status='accept')
#     return render(request, "staff/students_selected.html", {"selectedStudents": selectedstu})

# def reject_view(request,id='student_id'):
#     if request.method == 'POST':
#         if 'reject' in request.POST["rejected"]:
#             stu = get_object_or_404(Student, pk=id)
#             stu.status= 'reject'
#             stu.save()
#     rejectedstu = Student.objects.filter(status='reject')
#     return render(request, "staff/students_rejected.html", {"rejectedStudents": rejectedstu})

def accept_view(request):
    if request.method == 'POST':
        id = request.POST["student_id"]
        stu = get_object_or_404(Student, pk=id)
        if 'accept' in request.POST["decision"]:
        # if request.POST["decision"]=='accept':
            stu.status='accpeted'
            stu.save()
            return redirect('staff_view')
        if 'reject' in request.POST["decision"]:
        # if request.POST["decision"] == 'reject':
            stu.status = 'rejected'
            stu.save()
            return redirect('staff_view')
    selectedstu = Student.objects.filter(status='accepted')
    return render(request, "staff/students_selected.html", {"selectedStudents": selectedstu})
