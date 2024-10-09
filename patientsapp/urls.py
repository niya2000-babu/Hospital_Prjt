from django.urls import path
import patientsapp.views

urlpatterns = [

    path('', patientsapp.views.index, name="index"),
    path('registration/', patientsapp.views.registration, name="registration"),
    path('login/', patientsapp.views.login, name="login"),
    path('patients/', patientsapp.views.patients, name="patients"),
    path('patients_appointment/', patientsapp.views.patientappointment, name="patients_appointment"),
    # path('elements/', patientsapp.views.elements, name="elements"),
    # path('', patientsapp.views.elements, name="elements"),
    path('medicaltips/', patientsapp.views.medicaltips, name="medicaltips"),
    path('payment/', patientsapp.views.payment, name="payment"),
    path('account_details/', patientsapp.views.account_details, name="account_details"),
    path('view_history/', patientsapp.views.view_history, name="view_history"),

]

