from django.urls import path
import adminapp.views


urlpatterns = [


    path('admin_home_page/', adminapp.views.admin_page, name="adminhomepage"),
    path('add_departments/', adminapp.views.add_departments, name="add_departments"),
    # path('doc_details/<id>', adminapp.views.doctors_details, name="doctors_details"),
    path('viewdoctorlist/', adminapp.views.viewdoctorlist, name="viewdoctorlist"),
    path('doctordtls/<id>', adminapp.views.doctordtls, name="doctors_details"),
    path('approvedoc/<id>', adminapp.views.approvedoc, name="approvedoc"),
    path('rejectdoc/<id>', adminapp.views.rejectdoc, name="rejectdoc"),
    path('pending_patients/', adminapp.views.pending_patients, name="pending_patients"),
    path('approved_patients/<id>', adminapp.views.approved_patients, name="approved_patients"),
    path('viewappointment', adminapp.views.viewappointment, name="viewappointment"),
    path('appointmentsdtls/<id>', adminapp.views.appointmentsdtls, name="appointmentsdtls"),
    path('approveappointments/<id>', adminapp.views.approveappointments, name="approveappointments"),
    path('get-doctors1/', adminapp.views.get_doctors1, name='get_doctors1'),
    # path('get_doctors/<int:department_id>/', views.get_doctors, name='get_doctors'),
    path('assignduty', adminapp.views.assignduty, name="assignduty"),

]