from django.http import HttpResponse
from django.shortcuts import render
from .form import *
from .models import *

# Create your views here.

def student_view(request):
    if request.method == 'GET':
        frm_unbound = Student_form()
        d = {'frm':frm_unbound}
        resp = render(request,'myapp/student.html',context=d)
        return resp
    elif request.method == 'POST':
        frm_bound = Student_form(request.POST)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("student succesfully registered")
        else:
            resp = render(request,'myapp/student.html',context=d)
            return resp


def personal_view(request):
    if request.method == 'GET':
        frm_unbound = Personal_details_form()
        d = {'frm':frm_unbound}
        resp = render(request,'myapp/personal.html',context=d)
        return resp
    elif request.method == 'POST':
        frm_bound = Personal_details_form(request.POST)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("Details succesfully Filled")
        else:
            resp = render(request,'myapp/personal.html',context=d)
            return resp


def payment_view(request):
    if request.method == 'GET':
        frm_unbound = Payment_details_form()
        d = {'frm':frm_unbound}
        resp = render(request,'myapp/payment.html',context=d)
        return resp
    elif request.method == 'POST':
        frm_bound = Payment_details_form(request.POST)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("Payment Details succesfully Filled")
        else:
            resp = render(request,'myapp/payment.html',context=d)
            return resp


def course_view(request):
    if request.method == 'GET':
        frm_unbound = Course_details_form()
        d = {'frm':frm_unbound}
        resp = render(request,'myapp/course.html',context=d)
        return resp
    elif request.method == 'POST':
        frm_bound = Course_details_form(request.POST)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("Payment Details succesfully Filled")
        else:
            resp = render(request,'myapp/course.html',context=d)
            return resp


def get_student(request):
    d = {}
    d['courses'] = Course_details.objects.all()
    if request.method == 'GET':
        resp = render(request,'myapp/getstudent.html',context=d)
        return resp
    elif request.method == 'POST':
        cid = request.POST.get('course')
        C = Course_details.objects.get(id=int(cid))
        d['all_stu'] = C.student.all()
        resp = render(request,'myapp/getstudent.html',context=d)
        return resp
        


    # C1 = Course_details.objects.all()
    # d = {}
    # d['courses'] = C1
    # if request.method == 'GET':
    #     C = Course_details.objects.get(id=1)
    #     d['all_stu'] = C.student.all()
    #     d['cname'] = C.name
    #     d['cid'] = C.id
    #     resp = render(request,'myapp/getstudent.html',context=d)
    #     return resp
    # elif request.method == 'POST':
    #     cid = request.POST.get('course')
    #     C = Course_details.objects.get(id=int(cid))
    #     d['all_stu'] = C.student.all()
    #     d['cname'] = C.name
    #     resp = render(request,'myapp/getstudent.html',context=d)
    #     return resp




def myform(request):
    if request.method == 'GET':
        frm_unbound = Myform()
        d = {'frm':frm_unbound}
        resp = render(request,'myapp/myform.html',context=d)
        return resp
    elif request.method == 'POST':
        frm_bound = Myform(request.POST)
        if frm_bound.is_valid():
            return HttpResponse("Succesfully Submited")




def Student_img_view(request):
    if request.method == 'GET':
        frm_unbound = Studentimgform()
        d = {'frm':frm_unbound}
        resp = render(request,'myapp/img.html',context=d)
        return resp
    elif request.method == 'POST':
        frm_bound = Studentimgform(request.POST,files=request.FILES)
        d = {'frm':frm_bound}
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("Form Submited")
        else:
            resp = render(request,'myapp/img.html',context=d)
            return resp










