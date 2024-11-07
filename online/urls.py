"""
URL configuration for online project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from onlineapp import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_signup/', views.student_signup, name='student_signup'),
    path('faculty_signup/', views.faculty_signup, name='faculty_signup'),
    path('admin_signup/', views.admin_signup, name='admin_signup'),
    path('login/', views.custom_login, name='login'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('faculty_dashboard/', views.faculty_dashboard, name='faculty_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('',views.index),
    path('signup/',views.common_signup),
    path('logout/',views.logoutt),
    path('add_mendor/',views.add_mendor),
    path('accpect_mentor/<id>/',views.accpect_mentor),
    path('mentor_records/',views.mentor_records),
    path('more_information/',views.more_informations),
    path('grant_delet/<id>/',views.grant_delet),
    path('loans_delet/<id>/',views.loans_delet),
    path('incentive_delet/<id>/',views.incentive_delet),
    path('job_delet/<id>/',views.job_delet),
    path('add_job/',views.add_job),
    path('add_incentive/',views.add_incentive),
    path('add_grants/',views.add_grants),
    path('add_loans/',views.add_loans),
    path('terms_and_conditions/',views.terms_and_conditions),
    path('loat_request/',views.loat_request),
    path('loan_success/',views.loan_success),
    path('admin_view_requests/',views.admin_view_requests),
    path('faq/',views.faq),
    path('Privacy/',views.privacy_and_policy),
    path('mentor_access/',views.mentor_access),
    path('add_study_material/',views.add_study_material),
    path('add_video_material/',views.add_video_material),
    path('Student_request/',views.Student_request),
    path('view_student_details/<id>/',views.view_student_details),
    path('payment/<id>/',views.payment),
    path('payment_success/<id>/',views.payment_success),
    path('faculty_progress/',views.faculty_progress),
    path('del_category/<id>/',views.del_category),
    path('add_category/',views.add_category),
    path('delete_material/<id>/',views.delete_material),
    path('delete_video_met/<id>/',views.delete_video_met),
    path('study_material/',views.study_material),
    path('cat_books/',views.cat_books),
    path('book/<id>/',views.book),
    path('cat_video/',views.cat_video),
    path('videos/<id>/',views.videos),
    path('add_test/',views.add_test),
    path('add_questions/<id>/',views.add_questions),
    path('choose_test/',views.choose_test),
    path('test/<id>',views.test),
    path('progress/',views.progress),
    path('stu_more_information/',views.stu_more_information),
    path('view_incentive/',views.view_incentive),
    path('view_load/',views.view_load),
    path('view_grants/',views.view_grants),
    path('choose_signup/',views.choose_signup),
    path('my_account/',views.my_account),
    path('acc/<id>/',views.acc),
    path('Approved_Student/',views.Approved_Student),
    path('loan_request/',views.loan_request),
    path('loan_request_accept/<id>/',views.loan_request_accept),
    path('loan_request_reject/<id>/',views.loan_request_reject),
    path('job/',views.job_view),
    path('job_apply/<id>/',views.job_apply),
    path('job_apllication/',views.job_apllication),
    path('accept_mentor/<id>/',views.accept_mentor),
    path('reject_mentor/<id>/',views.reject_mentor),
    path('test_success/',views.test_success),
    

    
    
     

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


