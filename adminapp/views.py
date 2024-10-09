from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from Hosapp.models import doctorsregister
from patientsapp.models import Register,appointment
from .models import adddepartments,assigndoctor
from django.http import JsonResponse



from Hosapp .models import doctorsregister




# Create your views here.
def admin_page(request):
    context = {}
    template = loader.get_template("admin.html")
    return HttpResponse(template.render(context, request))


def add_departments(request):
    if request.method == 'POST':
        s = adddepartments()
        department = request.POST.get("department")
        s.Department = department
        s.save()
        return HttpResponse("<script>alert('Department added successfully');window.location='/add_departments';</script>")

    else:
        context = {}
        template = loader.get_template("add_departments.html")
        return HttpResponse(template.render(context, request))
#
#
# def doctors_details(request):
#     context = {}
#     template = loader.get_template

def viewdoctorlist(request):
    alldoc=doctorsregister.objects.all()
    context = {'key': alldoc}
    template = loader.get_template("view_doctors.html")
    return HttpResponse(template.render(context, request))


def doctordtls(request,id):
    id=doctorsregister.objects.get(id=id)
    context = {'key': id}
    template = loader.get_template("doctorprofile.html")
    return HttpResponse(template.render(context, request))


def approvedoc(request,id):
    r=doctorsregister.objects.get(id=id)
    # email=r.Email
    r.status='approve'
    r.save()
    # subject = 'You got an email from hospital'
    # message = 'Your request accepted successfully!!!!Now you can access your account'
    # email_from = settings.EMAIL_HOST_USER
    # mailid = email
    # recipient_list = [mailid, ]
    # send_mail(subject, message, email_from, recipient_list)

    return HttpResponse("<script>alert('Approved successfully');window.location='/viewdoctorlist';</script>")



def rejectdoc(request,id):
    r=doctorsregister.objects.get(id=id)
    # request.session["email"]=r.Email
    r.status='reject'
    r.save()
    # subject = 'You got an email from hospital'
    # message = 'Your request has declined!!!!Check your request...'
    # email_from = settings.EMAIL_HOST_USER
    # mailid = request.session["email"]
    # recipient_list = [mailid, ]
    # send_mail(subject, message, email_from, recipient_list)
    return HttpResponse("<script>alert('Rejected successfully');window.location='/viewdoctorlist';</script>")



def pending_patients(request):
    pndg_pts =Register.objects.filter(Status='pending')

    context = {'key':pndg_pts}
    template = loader.get_template("pending_patients.html")
    return HttpResponse(template.render(context, request))

def approved_patients(request,id):
    r = Register.objects.get(id=id)

    # email = r.Username
    r.Status = 'approved'
    r.save()


    return HttpResponse("<script>alert('Your Registration Approved successfully');window.location='/pending_patients';</script>")


def viewappointment(request):
    aponmnts=appointment.objects.all()
    for i in aponmnts:
        request.session["email"]= i.Email
    context = {'key': aponmnts}
    template = loader.get_template("viewappointments.html")
    return HttpResponse(template.render(context, request))


def appointmentsdtls(request,id):
    id=appointment.objects.get(id=id)
    context = {'key': id}
    template = loader.get_template("vieweachappointments.html")
    return HttpResponse(template.render(context, request))


def approveappointments(request,id):
    r=appointment.objects.get(id=id)
    # email=r.Email
    r.status='approved'
    r.save()
    # subject = 'You got an email from ehospital'
    # message = 'Your request accepted successfully!!!!Now you can access your account'
    # email_from = settings.EMAIL_HOST_USER
    # mailid = email
    # recipient_list = [mailid, ]
    # send_mail(subject, message, email_from, recipient_list)

    return HttpResponse("<script>alert('Approved successfully');window.location='/viewappointment';</script>")




def get_doctors1(request):
    aponmnts=adddepartments.objects.all()

    # r1 = appointment.objects.raw("select * from patientsapp_appointment where Email=%s", [email])
    d=doctorsregister.objects.all()
    context = {'doc':d,'key': aponmnts}
    template = loader.get_template("assigndoctor.html")
    return HttpResponse(template.render(context, request))

# def get_doctors(request, specialization):
#     if request.method == 'GET':
#         doctors = doctorsregister.objects.filter(Specialization=specialization).values('id','Name')
#         return JsonResponse(list(doctors), safe=False)

# def get_doctors(request, department_id):
#     doctors = doctorsregister.objects.filter(department_id=department_id,
#                                                  status='approved')  # Assuming you only want approved doctors
#     doctor_list = list(doctors.values('id', 'Name'))
#     return JsonResponse(doctor_list, safe=False)



def assignduty(request):
    if request.method == 'POST':
        r = assigndoctor()
        name = request.POST.get("name")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        symptoms = request.POST.get("symptoms")
        department = request.POST.get("ddldepartment")
        doctors = request.POST.get("ddldoctors")

        r.Name = name
        r.Contact = contact
        r.Email = email
        r.Symptoms = symptoms
        r.Department = department
        r.Doctor = doctors
        r.save()
        return HttpResponse("<script>alert('assigned Successfully');window.location='/viewdoctorlist'</script>")
    else:

        template=loader.get_template("assigndoctor.html")
        context = {}
        return HttpResponse(template.render(context,request))






