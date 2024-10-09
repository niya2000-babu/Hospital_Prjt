from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from adminapp.models import adddepartments
from patientsapp.models import Login
from Hosapp.models import doctorsregister,appointmentshedule,schedule,prescription
from django.utils import timezone
from patientsapp.models import Register




# Create your views here.

def doctor(request):
    context = {}
    template = loader.get_template("doctors.html")
    return HttpResponse(template.render(context, request))


def doctor_reg(request):
    if request.method == 'POST':
        d = doctorsregister()
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        hname = request.POST.get("hname")
        street = request.POST.get("street")
        city = request.POST.get("city")
        state = request.POST.get("state")
        pin = request.POST.get("pin")
        country = request.POST.get("country")
        spcial = request.POST.get("ddlspecial")
        uname = request.POST.get("uname")
        pwd = request.POST.get("pwd")
        photo = request.FILES["photo"]
        qual = request.FILES["qual"]
        exp = request.FILES["exp"]
        d.Name = name
        d.Email = email
        d.Contact = phone
        d.Address = hname
        d.street = street
        d.city = city
        d.state = state
        d.pin = pin
        d.country = country
        d.Specialization = spcial
        d.photo = photo
        d.qual = qual
        d.exp = exp
        d.uname = uname
        d.pwd = pwd
        d.status = 'pending'
        l = Login()
        l.Username = uname
        l.Password = pwd
        l.Usertype = 'Doctor'
        l.save()
        d.save()
        return HttpResponse("<script>alert('Inserted Successfully');window.location='/doctor'</script>")
    else:
        b = adddepartments.objects.all()
        context = {'dptdwn': b}
        template = loader.get_template("doctor_reg.html")
        return HttpResponse(template.render(context, request))



def viewpatientlist(request):
    p=Register.objects.raw("SELECT r.*, a.* FROM patientsapp_register r JOIN patientsapp_appointment a ON r.Username = a.Email;")
    context = {'key': p}
    template = loader.get_template("viewpatientrecord.html")
    return HttpResponse(template.render(context, request))

    # uname=request.session["uname"]
    # doc_id=request.session["doc_id"]
    # current_date = timezone.now().date()
    #
    # p = Register.objects.raw("SELECT    p. *, a. *, d. *, ap. * FROM patientapp_Register p JOIN Adminapp_assigndoctor a ON p.Username = a.Email JOIN medoffapp_doctorsregister d ON a.Doctor = d.id JOIN  patientapp_appointment ap ON ap.Email = a.Email where a.Doctor = %s and ap.Date >= %s",[doc_id,current_date])
    # context = {'key':p }
    # template=loader.get_template("viewpatientrecord.html")
    # return HttpResponse(template.render(context,request))


#____________

def pschedule(request):
    if request.method == 'POST':
        d = schedule()
        name = request.POST.get("name")
        age = request.POST.get("age")
        contact = request.POST.get("phone")
        email = request.POST.get("Email")
        gender = request.POST.get("gender")
        time = request.POST.get("timepicker")
        bill = request.POST.get("Bill")

        d.Name = name
        d.Age = age
        d.Contact = contact
        d.Email = email
        d.Gender = gender
        d.Time = time
        d.bill = bill

        d.save()
        return HttpResponse("<script>alert('scheduled Successfully');window.location='/doctor_reg'</script>")
    else:
        context = {}
        template = loader.get_template("appointmentsheduling.html")
        return HttpResponse(template.render(context, request))

def eprescription(request):
    if request.method == 'POST':
        d = prescription()
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        medicines = request.POST.get("medicines")
        test = request.POST.get("test")

        d.Name = name
        d.Age = age
        d.Gender = gender
        d.Medicines = medicines
        # d.Gender = gender
        d.Test = test

        d.save()
        return HttpResponse("<script>alert('prescription send Successfully');window.location='/doctor'</script>")
    else:
        context={}
        template=loader.get_template("e_priscriptions.html")
        return HttpResponse(template.render(context,request))





