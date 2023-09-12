from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [


    #path("admin/", admin.site.urls),
    #path('',include('Accounts.urls'))
    path('home/',views.home,name="home"),
   # path('profile/', views.emp_profile, name="emp"),
   # path('hr/',views.hr_home,name="hr_home"),
   # path('manager/',views.manager_home,name="manager_home"),
    path('emplist/',views.Emp_list, name='emp_list'),
    #path('signup/',views.signup_view, name='signup'),
    path('signup/', views.Register_view, name='signup1'),
    path('detail/<int:id>/', views.employee_detail, name='detail') ,
    path('update/<int:id>/', views.update_emp, name='update'),
    path('details/<int:id>/', views.details_view, name='details') ,
    #path('hr/details/<int:id>/', views.details_view, name='details') ,
    path('emp/<int:id>/delete', views.delete_emp, name='delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html'),name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),

    path('leave-request/',views.leave_request_view, name='leave_request'),
    path('leave-request/success/', views.leave_request_success_view, name='leave_request_success'),
    path('leave-approval/<int:request_id>/', views.leave_approval_view, name='leave_approval'),
    path('leave-approvals_pending/', views.leave_approvals_pending, name='leave_approval_pending'),
    path('leave-requests/', views.leave_request_list_view, name='leave_request_list'),
    path('notifications/', views.notification_view, name='notifications'),
    path('notifyed/<int:id>/',views.Notifyed,name="notifyed"),
    path('permission-request/', views.permission_request_view, name='permission_request'),
    path('permission-request/success/', views.permission_request_success_view, name='permission_request_success'),
    path('permission-approval/<int:request_id>/', views.permission_approval_view, name='permission_approval'),
    path('permission-requests/', views.permission_request_list_view, name='permission_request_list'),
    path('attendance/', views.Attendance_view,name='attendance'),
    path('attendence_records/',views.Attndence_Records,name="records"),
    path('punch/',views.punch,name="punch"),
    path('punch_in/',views.punch_in_prasent,name="punch_in"),
    path('test/',views.test,),
   # path('calculation/', views.Calculation_view, name="calculate")
    path('api/events/', views.get_events, name='get_events'),
    #--------
    path("update_emp/<int:id>/", views.index, name="update_emp"),
    #path("update_emp/<int:id>/",views.emp_upd,name="update_emp"),
    path("get/<int:data_id>/", views.get_item, name="getitem"),
    path("create/",views.create,name="create"),
    path("update_p/<int:id>/", views.update_p, name="up_p"),
    path('my_get_view/',views.my_get_view,name="my_get_view"),
    path('send-sms/', views.send_sms, name='send-sms'),
    #-------------
    path('birthday/',views.birthdays,),
    path('attandrecords/',views.daywise_records,),

    path("upd/<int:id>/",views.emp_update_view,name="up_emp"),
    path("get_record/<int:data_id>/",views.emp_update_total_view,name="get_record"),

    path("get_immegration/<int:id>/", views.get_immegration_data, name="get_immegration"),
    path("get_immegration/", views.get_immegration_total_data, name="get_immegration_total_data"),

    path("submit_immegration/",views.Add_immegration_data,name="immegration"),
    path("update_immegration/", views.update_immegration_data, name="immegration_update"),
    path("delete_immegration/", views.delete_immegration_data, name="delete_immegration"),
    path("emergency_contacts/",views.Add_emergency_contacts_data,name="contacts"),
    path("emergency_contacts_update/", views.update_emergency_contacts_data, name="update_contacts"),
    path("emergency_contacts_get/<int:id>/", views.get_emergency_contacts_data, name="get_contacts"),
    path("emergency_contacts_delete/", views.delete_emergency_contacts_data, name="delete_contacts"),
    path("social_profile/",views.Add_profile_data,name="profile1"),
    path("social_profile_update/", views.update_profile_data, name="profile1_update"),
   # path("get_social_profile/<int:id>", views.Add_profile_data, name="update_profile1"),
    path("all_documents/", views.Add_documents_data, name="documents"),
    path("get_documents/<int:id>/", views.get_documents_data, name="get_documents"),
    path("update_documents/", views.update_documents_data, name="update_documents"),
    path("delete_documents/", views.delete_documents_data, name="delete_documents"),
    path("qualifications/", views.Add_qualifications_data, name="qualifications"),
    path("get_qualifications/<int:id>/", views.get_qualifications_data, name="get_qualifications"),
    path("update_qualifications/", views.update_qualifications_data, name="qualifications_update"),
    path("delete_qualifications/", views.delete_qualifications_data, name="qualifications_delete"),
    path("work_experience/", views.Add_work_experience_data, name="experience"),
    path("get_work_experience/<int:id>/", views.get_work_experience_data, name="get_experience"),
    path("update_work_experience/", views.update_work_experience_data, name="experience_update"),
    path("delete_work_experience/", views.delete_work_experience_data, name="experience_delete"),
    path("bank_account/", views.Add_bank_account_data, name="account"),
    path("bank_account_update/", views.update_bank_account_data, name="account_update"),
    path("get_bank_account_data/<int:id>/", views.get_bank_account_data, name="account_get"),
    path("bank_account_delete/", views.delete_bank_account_data, name="account_delete"),
    path("basic_salary/", views.Add_basic_salary_data, name="basic_salary"),
    path("update_basic_salary/", views.update_basic_salary_data, name="update_basic_salary"),
    path("allowances/", views.Add_allowances_data, name="allowances"),
    path("update_allowances/", views.update_allowances_data, name="update_allowances"),
    path("commissions/", views.Add_commissions_data, name="commissions"),
    path("update_commissions/", views.update_commissions_data, name="update_commissions"),
    path("loan/", views.Add_loan_data, name="loan"),
    path("update_loan/", views.update_loan_data, name="update_loan"),
    path("statutory_deduction/", views.Add_statutory_deduction_data, name="statutory_deduction"),
    path("update_statutory_deduction/", views.update_statutory_deduction_data, name="update_statutory_deduction"),
    path("other_payments/", views.Add_other_payments_data, name="other_payments"),
    path('update_other_payments/', views.update_other_payments_data, name='update_other_payments'),
    path("over_time/", views.Add_over_time_data, name="over_time"),
    path('update_over_time/', views.update_over_time_data, name='update_over_time'),


#project management urls
    path('add_projects/',views.Add_project,name='add_project'),
    path('get_project_details/',views.get_project_details,name='get_project_details'),
    path('update_projects/', views.Update_project_details, name='update_project'),
    path('delete_projects/', views.delete_project_details, name='delete_project_details'),



# task urls
    path('get_task_list/', views.get_tasks, name='get_project_list'),
    path('get_task_record/<int:id>/', views.get_taks_record_wise, name='get_project_record'),
    path('add_task/', views.add_taks, name='add_tasks'),
    path('update_task/', views.update_tasks, name='update_tasks'),
    path('delete_tasks/', views.delete_tasks, name='delete_tasks'),


    path("faq/", views.faq, name="faq"),
    path("contacts_d/", views.contacts_d, name="contacts_d"),

    path('hr_view/',views.Hr_view ,name="hr_dashboard"),



    path("company_policy/", views.Add_company_policy_data, name="company_policy"),
    path('update_company_policy/', views.update_company_policy_data, name='update_company_policy'),
    path("delete_company_policy/", views.delete_company_policy_data, name="delete_company_policy"),
    path("company_policy_get/<int:id>/", views.get_company_policy_data, name="company_policy_get"),

    path("announcements/", views.Add_announcements_data, name="announcements"),
    path('update_announcements/', views.update_annoucements_data, name='update_announcements'),
    path("delete_announcements/", views.delete_announcements_data, name="delete_announcements"),
    path("announcements_get/<int:id>/", views.get_announcements_data, name="announcements_get"),

    path("designation/", views.Add_designation_data, name="designation"),
    path('update_designation/', views.update_designation_data, name='update_designation'),
    path("delete_designation/", views.delete_designation_data, name="delete_designation"),
    path("designation_get/<int:id>/", views.get_designation_data, name="designation_get"),

    path("location/", views.Add_location_data, name="location"),
    path('update_location/', views.update_location_data, name='update_location'),
    path("delete_location/", views.delete_location_data, name="delete_location"),
    path("location_get/<int:id>/", views.get_location_data, name="location_get"),

    path("department/", views.Add_department_data, name="department"),
    path('update_department/', views.update_department_data, name='update_department'),
    path("delete_department/", views.delete_department_data, name="delete_department"),
    path("department_get/<int:id>/", views.get_department_data, name="department_get"),
    path("company/", views.Add_company_data, name="company"),
    path('update_company/', views.update_company_data, name='update_company'),
    path("delete_company/", views.delete_company_data, name="delete_company"),
    path("company_get/<int:id>/", views.get_company_data, name="company_get"),



    path("promotions/", views.Add_promotions_data, name="promotions"),
    path("awards/", views.Add_awards_data, name="awards"),

    path("travel/", views.Add_travel_data, name="travel"),

    path("transfer/", views.Add_transfer_data, name="transfer"),

    path("resignation/", views.Add_resignation_data, name="resignation"),

    path("complains/", views.Add_complains_data, name="complains"),
    path("warnings/", views.Add_warnings_data, name="warnings"),
    path("terminations/", views.Add_terminations_data, name="terminations"),
    path("update_terminations/", views.update_terminations_data, name="update_terminations"),
    path("update_warnings/", views.update_warnings_data, name="update_warnings"),
    path("update_complains/", views.update_complains_data, name="update_complains"),
    path("update_resignation/", views.update_resignation_data, name="update_resignation"),
    path("update_transfer/", views.update_transfer_data, name="update_transfer"),
    path("update_travel/", views.update_travel_data, name="update_travel"),
    path("update_awards/", views.update_awards_data, name="update_awards"),
    path("update_promotions/", views.update_promotions_data, name="update_promotions"),
    path("delete_promotions/", views.delete_promotions_data, name="delete_promotions"),
    path("delete_terminations/", views.delete_terminations_data, name="delete_terminations"),
    path("delete_warnings/", views.delete_warnings_data, name="delete_warnings"),
    path("delete_complains/", views.delete_complains_data, name="delete_complains"),
    path("delete_resignation/", views.delete_resignation_data, name="delete_resignation"),
    path("delete_transfer/", views.delete_transfer_data, name="delete_transfer"),
    path("delete_travel/", views.delete_travel_data, name="delete_travel"),

    path("delete_awards/", views.delete_awards_data, name="delete_awards"),
    path("awards_get/<int:id>/", views.get_awards_data, name="awards_get"),
    path("promotions_get/<int:id>/", views.get_promotions_data, name="promotions_get"),
    path("complains_get/<int:id>/", views.get_complains_data, name="complains_get"),
    path("resignation_get/<int:id>/", views.get_resignation_data, name="resignation_get"),
    path("terminations_get/<int:id>/", views.get_terminations_data, name="terminations_get"),
    path("transfer_get/<int:id>/", views.get_transfer_data, name="transfer_get"),
    path("travel_get/<int:id>/", views.get_travel_data, name="travel_get"),
    path("warnings_get/<int:id>/", views.get_warnings_data, name="warnings_get"),
    path("job_post/", views.Add_job_post_data, name="job_post"),
    path("update_job_post/", views.update_job_post_data, name="update_job_post"),
    path("delete_job_post/", views.delete_job_post_data, name="delete_job_post"),

    path("job_candidate/", views.Add_job_candidate_data, name="job_candidate"),
    path("update_job_candidate/", views.update_job_candidate_data, name="update_job_candidate"),
    path("delete_job_candidate/", views.delete_job_candidate_data, name="delete_job_candidate"),

    path("job_interview/", views.Add_job_interview_data, name="job_interview"),
    path("update_job_interview/", views.update_job_interview_data, name="update_job_interview"),
    path("delete_job_interview/", views.delete_job_interview_data, name="delete_job_interview"),
    path("job_post_get/<int:id>/", views.get_job_post_data, name="job_post_get"),
    path("job_candidate_get/<int:id>/", views.get_job_candidate_data, name="job_candidate_get"),
    path("job_interview_get/<int:id>/", views.get_job_interview_data, name="job_interview_get"),






    path("trainer_get/<int:id>/", views.get_trainer_data, name="trainer_get"),
    path("training_type_get/<int:id>/", views.get_training_type_data, name="training_type_get"),
    path("training_list_get/<int:id>/", views.get_training_list_data, name="training_list_get"),
    path("trainer/", views.Add_trainer_data, name="trainer"),
    path("update_trainer/", views.update_trainer_data, name="update_trainer"),
    path("delete_trainer/", views.delete_trainer_data, name="delete_trainer"),

    path("training_type/", views.Add_training_type_data, name="training_type"),
    path("update_training_type/", views.update_training_type_data, name="update_training_type"),
    path("delete_training_type/", views.delete_training_type_data, name="delete_training_type"),

    path("training_list/", views.Add_training_list_data, name="training_list"),
    path("update_training_list/", views.update_training_list_data, name="update_training_list"),
    path("delete_training_list/", views.delete_training_list_data, name="delete_training_list"),

    path("events/", views.Add_events_data, name="events"),
    path("update_events/", views.update_events_data, name="update_events"),
    path("delete_events/", views.delete_events_data, name="delete_events"),
    path("events_get/<int:id>/", views.get_events_data, name="events_get"),


    path("meetings/", views.Add_meetings_data, name="meetings"),
    path("update_meetings/", views.update_meetings_data, name="update_meetings"),
    path("delete_meetings/", views.delete_meetings_data, name="delete_meetings"),
    path("meetings_get/<int:id>/", views.get_meetings_data, name="meetings_get"),


    path("category/", views.Add_category_data, name="category"),
    path("update_category/", views.update_category_data, name="update_category"),
    path("delete_category/", views.delete_category_data, name="delete_category"),

    path("assets/", views.Add_assets_data, name="assets"),
    path("update_assets/", views.update_assets_data, name="update_assets"),
    path("delete_assets/", views.delete_assets_data, name="delete_assets"),
    path("assets_get/<int:id>/", views.get_assets_data, name="assets_get"),
    path("category_get/<int:id>/", views.get_category_data, name="category_get"),


    path("clients/", views.Add_clients_data, name="clients"),
    path("update_clients/", views.update_clients_data, name="update_clients"),
    path("delete_clients/", views.delete_clients_data, name="delete_clients"),
    path("clients_get/<int:id>/", views.get_clients_data, name="clients_get")




















]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
