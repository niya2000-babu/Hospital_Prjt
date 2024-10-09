from django.urls import path
import Hosapp.views

urlpatterns = [


    path('doctor/', Hosapp.views.doctor, name="doctor"),
    path('doct_reg/', Hosapp.views.doctor_reg, name="doctor_registration"),
    # path('appointmentsheduling/', Hosapp.views.next_page_view, name="appointmentsheduling"),
    path('viewpatientlist/', Hosapp.views.viewpatientlist, name="viewpatientlist"),
    path('pschedule-page/', Hosapp.views.pschedule, name='pschedule'),
    path('e-prescription/', Hosapp.views.eprescription, name='e-prescription'),

]