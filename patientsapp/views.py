from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from patientsapp.models import Register, Login,pay

from Hosapp.models import doctorsregister,schedule,prescription
from patientsapp.models import appointment


#
# from.models import patientregister
# from adminapp.models import Login

# Create your views here.
def index(request):
        context = {}
        template = loader.get_template("index.html")
        return HttpResponse(template.render(context, request))

def registration(request):
    if request.method=='POST':
        r=Register()
        l=Login()
        name = request.POST.get("name")
        age = request.POST.get("age")
        phone = request.POST.get("phone")
        gender= request.POST.get("gender")
        address = request.POST.get("address")
        username = request.POST.get("username")
        password = request.POST.get("password")
        r.Name=name
        r.Age=age
        r.Phone=phone
        r.Gender=gender
        r.Address=address
        r.Username=username
        r.Password=password
        r.Status="pending"
        r.save()
        l.Username=username
        l.Password=password
        l.Usertype='User'
        l.save()
        return HttpResponse("<script>alert('Inserted Successfully');window.location='/registration'</script>")

    else:
        context = {}
        template = loader.get_template("registration.html")
        return HttpResponse(template.render(context, request))

# def login(request):
#     context = {}
#     template = loader.get_template("login.html")
#     return HttpResponse(template.render(context, request))

def login(request):
    if request.method=="POST":
        uname=request.POST.get('username')
        request.session["uname"]=uname
        pwd=request.POST.get('password')
        if(Login.objects.filter(Username=uname,Password=pwd)):
            li=Login.objects.filter(Username=uname,Password=pwd)
            for i in li:
                if(i.Usertype == "admin"):
                    request.session["uname"] = uname
                    context = {}
                    template = loader.get_template("admin.html")
                    return HttpResponse(template.render(context, request))
                elif (i.Usertype == "User"):
                    u = Register.objects.get(Username=uname)
                    if (u.Status == "pending"):
                        return HttpResponse("<script>alert('Not Approved ');window.location='/login';</script>")
                    else:
                        request.session["uname"] = uname
                        context = {}
                        template = loader.get_template("patients.html")
                        return HttpResponse(template.render(context, request))

                elif(i.Usertype == "Doctor"):
                    u=doctorsregister.objects.get(uname=uname)
                    if(u.status=="pending"):
                        return HttpResponse("<script>alert('NoT Approved by admin');window.location='/login';</script>")
                    else:
                        request.session["uname"]=uname
                        context = {}
                        template = loader.get_template("doctors.html")
                        return HttpResponse(template.render(context, request))

        else:
            return HttpResponse("<script>alert('invalid uname or pwd');window.location='/login';</script>")
    else:

        context = {}
        template = loader.get_template("login.html")
        return HttpResponse(template.render(context, request))


def patients(request):
    context = {}
    template = loader.get_template("patients.html")
    return HttpResponse(template.render(context, request))


def element(request):
    context={}
    template=loader.get_template("elements.html")
    return HttpResponse(template.render(context,request))



def patientappointment(request):
    if request.method == 'POST':
        r = appointment()
        name = request.POST.get("name")
        email = request.POST.get("email")
        date = request.POST.get("datepicker")
        symptoms = request.POST.get("Symptoms")
        contact = request.POST.get("contact")


        r.Name = name
        r.Email = email
        r.Date = date
        r.Symptoms = symptoms
        r.Contact = contact
        r.status = 'pending'
        r.save()
        return HttpResponse("<script>alert('Booking added  Successfully');window.location='/patients_appointment'</script>")
    else:
        context = {}
        template = loader.get_template("appointment.html")
        return HttpResponse(template.render(context, request))






# def patients_appointment(request):
#     context = {}
#     template = loader.get_template("appointment.html")
#     return HttpResponse(template.render(context, request))





def medicaltips(request):
    context={}
    template=loader.get_template("medicaltips.html")
    return HttpResponse(template.render(context,request))
def payment(request):
    d=schedule.objects.all()
    context = {'key':d}

    template = loader.get_template("payment.html")
    return HttpResponse(template.render(context, request))

def account_details(request):
    if request.method=='POST':
        r = pay()
        bank = request.POST.get("bankname")
        branch = request.POST.get("branchname")
        IFSC = request.POST.get("ifsc")
        cardholder = request.POST.get("cname")
        amount = request.POST.get("amount")
        r.BankName==bank
        r.Branch=branch
        r.IFSC=IFSC
        r.cardholder=cardholder
        r.amount=amount
        r.save()
        return HttpResponse("<script>alert('payment Successfully');window.location='/patienthome'</script>")
    else:
        context = {}
        template = loader.get_template("AddAccount.html")
        return HttpResponse(template.render(context, request))

# def billamount(request):
#     a=eprescription.objects.all()
#     context={'key':a}
#     template=loader.get_template("billamount.html")
#     return HttpResponse(template.render(context,request))
#
def view_history(request):
    d= prescription.objects.all()

    context = {'key':d}
    template = loader.get_template("viewhistory.html")
    return HttpResponse(template.render(context, request))

