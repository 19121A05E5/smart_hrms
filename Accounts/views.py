# Create your views here.
from django.core.exceptions import ValidationError
"""

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

"""
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .forms import LeaveRequestForm
from .forms import CustomSignupForm,EmployeeMasterForm,CustomUpdateForm
from django.shortcuts import render,redirect
from .forms import RegisterForm
from . models import EmployeeMaster,Tasks,Projects,Client,Company, Leavecategory,Attendance,Permission,PermissionApproval,Immegration,Emergency_Contacts,Social_Profile,Documents_All,Qualifications,Work_Experience,Bank_Account,Basic_Salary,Allowances,Commissions,Loan,Statutory_Deduction,Other_Payments,Over_Time
from django.contrib import messages
from django.contrib.auth import login as auth_login , authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
# Create your views here.
from Accounts.models import CustomUser,LeaveRequest,Notification,Public_holidays#Permission,PermissionApproval
from django.contrib import messages
from .models import Event,Pro,Company,Company_Policy,Announcements,Designation,Assets_Category,Location,Department,Promotions,Awards,Travel,Transfer,Resignation,Complains,Warnings,Terminations,Trainer,Training_Type,Training_List,Assets,Job_Post,Job_Candidate,Job_Interview,Client,Events,Meetings
from django.conf import settings
from django.http import HttpResponse
from twilio.rest import Client

def send_sms(request):
    account_sid = settings.TWILIO_ACCOUNT_SID
    auth_token = settings.TWILIO_AUTH_TOKEN
    twilio_phone_number = '+15555555555'  # Replace with your Twilio phone number
    recipient_phone_number = '+1234567890'  # Replace with the recipient's phone number

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body="Hello from your Django app!",
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        return HttpResponse(f"SMS sent with SID: {message.sid}")
    except Exception as e:
        return HttpResponse(f"SMS sending failed: {str(e)}")
















def index(request,id):
    data_id=id # Replace this with the actual value you want to pas1

    user=CustomUser.objects.get(id=data_id)
    emp_obj=EmployeeMaster.objects.get(user_id=user.id)
    data2=Immegration.objects.filter(user_id=data_id).all()
    data3=Emergency_Contacts.objects.filter(user_id=data_id).all()
    data4=Documents_All.objects.filter(user_id=data_id).all()
    data5=Qualifications.objects.filter(user_id=data_id).all()
    data6=Work_Experience.objects.filter(user_id=data_id).all()
    data7=Bank_Account.objects.filter(user_id=data_id).all()

    data8=Basic_Salary.objects.filter(user_id=data_id).all()
    data9=Allowances.objects.filter(user_id=data_id).all()
    data10=Commissions.objects.filter(user_id=data_id).all()
    data11=Loan.objects.filter(user_id=data_id).all()
    data12=Statutory_Deduction.objects.filter(user_id=data_id).all()
    data13=Other_Payments.objects.filter(user_id=data_id).all()
    data14=Over_Time.objects.filter(user_id=data_id).all()
    data00=Social_Profile.objects.filter(user_id=data_id).all()
    data15 = Company_Policy.objects.all()
    data16 = Announcements.objects.all()
    data17 = Designation.objects.all()
    data18 = Location.objects.all()
    data19 = Department.objects.all()
    data20 = Company.objects.all()

    data21 = Promotions.objects.all()
    data23 = Awards.objects.all()
    data24 = Travel.objects.all()
    data25 = Transfer.objects.all()
    data26 = Resignation.objects.all()
    data27 = Complains.objects.all()
    data28 = Warnings.objects.all()
    data29 = Terminations.objects.all()

    data30 = Trainer.objects.all()
    data31 = Training_Type.objects.all()
    data32 = Training_List.objects.all()

    data35 = Assets_Category.objects.all()
    data36 = Assets.objects.all()

    data37 = Job_Post.objects.all()
    data38 = Job_Candidate.objects.all()
    data39 = Job_Interview.objects.all()
    data40 = Client.objects.all()
    data41 = Events.objects.all()
    data42 = Meetings.objects.all()









    k=Pro.objects.all()
    context = {'data_id':data_id,'k':k,'user':user,'emp_obj':emp_obj,'data00':data00,'data2':data2,'data3':data3,'data4':data4,'data5':data5,'data6':data6,'data7':data7,'data8':data8,'data9':data9,'data10':data10,'data11':data11,'data12':data12,'data13':data13,'data14':data14,'data15':data15,'data16':data16,'data17':data17,'data18':data18,'data19':data19,'data20':data20,'data21':data21,'data23':data23,'data24':data24,'data25':data25,'data26':data26,'data27':data27,'data28':data28,'data29':data29,'data30':data30,'data31':data31,'data32':data32,'data35':data35,'data36':data36,'data37':data37,'data38':data38,'data39':data39,'data40':data40,'data41':data41,'data42':data42}
    return render(request,'hr/emp.edit.html',context)



def emp_update_view(request, id):
    if request.method == 'POST':
        # Assuming you're using a model named YourModel
        #try:
        #    user = CustomUser.objects.get(id=id)
         #   item=EmployeeMaster.objects.get(usr_id=user.id)
       # except EmployeeMaster.DoesNotExist:
         #   response_data = {'error': 'Item not found'}
          #  return JsonResponse(response_data, status=404)
        user = CustomUser.objects.get(id=id)
        emp_u=EmployeeMaster.objects.get(user_id=user.id)

        email = request.POST.get('email')
        username = request.POST.get('username')
        emp_id = request.POST.get('emp_id')
        phone_no = request.POST.get('phone_no')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state= request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital_status')
        company = request.POST.get('company')
        department = request.POST.get('department')
        role = request.POST.get('role')
        shift = request.POST.get('shift')
        joining_date= request.POST.get('joining_date')

        print(first_name,phone_no,last_name, emp_id, role, department,joining_date,email,last_name ,address,city,state,zip_code,country, date_of_birth,  gender, marital_status,shift)
        # Update the item's fields based on the new data
        user.first_name=first_name
        user.last_name=last_name
        user.username=username
        user.email=email
        user.save()
        emp_u.EmployeeID =emp_id
        emp_u. phone_number=phone_no
        emp_u.Address =address
        emp_u.JoiningDate="-".join(joining_date.split("-"))
        emp_u.Shift_time=shift
        emp_u.City=city
        emp_u.state=state
        emp_u.PinCode= zip_code
        emp_u.country=country
        emp_u.BirthDate="-".join(date_of_birth.split("-"))
        emp_u.Gender=gender
        emp_u.MaratialStatus=marital_status
        emp_u.companyname=company
        emp_u.Department=department
        emp_u.Role=role
        emp_u.save()




        response_data = {'first_name': first_name}
        return JsonResponse(response_data)

    response_data = {'error': 'Invalid request'}
    return JsonResponse(response_data, status=400)




def emp_update_total_view(request,data_id):
    if request.method == 'GET':

        user=CustomUser.objects.get(id=data_id)
        basic=EmployeeMaster.objects.get(user_id=user.id)
        data = {
            'first_name':user.first_name,
            'last_name': user.last_name,
            'username':user.username,
            'email':user.email,
            'phone_no':basic.phone_number,
            'emp_id':basic.EmployeeID,
            'address':basic.Address,
            'city':basic.City,
            'state':basic.state,
            'zip_code':basic.PinCode,
            'country':basic.country ,
        'date_of_birth':basic.BirthDate,
        'gender':basic.Gender,
        'marital_status':basic.MaratialStatus,
        'company':basic.companyname,
        'department':basic.Department,
        'designation':basic.Designation,
        'role':basic.Role,
        'shift':basic.Shift_time,
        'joining_date':basic.JoiningDate,

              }
        print(data)
        return JsonResponse(data)











































import os
def get_immegration_data(request,id):
    if request.method == 'GET':
        immigration_record=Immegration.objects.get(id=id)
        print(immigration_record.document_name,immigration_record.document_number,immigration_record.issue_date,immigration_record.document_file, immigration_record.country, immigration_record.expired_date)
        data = {
            "document_type": immigration_record.document_name,
            "immigration_document_number": immigration_record.document_number,
            "immigration_issue_date": immigration_record.issue_date,
            "immigration_expiry_date": immigration_record.expired_date,
            "countrys": immigration_record.country,

          # "immigration_document_file_update": os.path.basename(immigration_record.document_file)
            # Add more fields as needed
              }
        return JsonResponse(data)


def get_immegration_total_data(request):
    # Fetch the immigration records from the database
    immigration_records = Immegration.objects.all()

    # Create a list of dictionaries representing each record
    data = []
    for record in immigration_records:
        data.append({
            "document_name": record.document_name,
             "document_number": record.document_number,
            "issue_date": record.issue_date,
            "expired_date": record.expired_date,

            "country": record.country,
           # "file_name": record.document_file.name
            # Add more fields as needed
        })

    # Return the data as a JSON response
    return JsonResponse(data, safe=False)






def Add_immegration_data(request):
    if request.method == 'POST' and request.FILES.get('immigration_document_file'):

        immigration_document_file= request.FILES['immigration_document_file']
        document_type = request.POST.get('document_type')
     #   immigration_document_file = request.POST.get('immigration_document_file')
        immigration_document_number = request.POST.get('immigration_document_number')
        immigration_issue_date = request.POST.get('immigration_issue_date')
        immigration_expiry_date = request.POST.get('immigration_expiry_date')
        country = request.POST.get('country')
        data_id = request.POST.get('data_id')
        user = CustomUser.objects.get(id=data_id)



        print(document_type,immigration_document_file,immigration_document_number,immigration_issue_date,country,immigration_expiry_date,document_type)

        obj=Immegration.objects.create(user_id=user.id, document_name=document_type,document_number=immigration_document_number,issue_date="-".join( immigration_issue_date.split("-")),expired_date="-".join(immigration_expiry_date.split("-")),country=country,document_file= immigration_document_file)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def delete_immegration_data(request):
    if request.method == 'POST' and request.is_ajax():

        immigration_id= request.POST.get('immigration_id')
        data_id = request.POST.get('data_id')

        user = CustomUser.objects.get(id=data_id)
        obj = Immegration.objects.get(user_id=user.id, id=immigration_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)


def update_immegration_data(request):
    if request.method == 'POST' and request.is_ajax() and request.FILES.get('immigration_document_file_update'):
        data_id=request.POST.get('data_id')
        immigration_id= request.POST.get('immigration_id')
        immigration_document_file_update = request.FILES['immigration_document_file_update']
        document_type_update = request.POST.get('document_type_update')
        #   immigration_document_file = request.POST.get('immigration_document_file')
        immigration_document_number_update   = request.POST.get('immigration_document_number_update')
        immigration_issue_date_update   = request.POST.get('immigration_issue_date_update')
        immigration_expiry_date_update = request.POST.get('immigration_expiry_date_update')
        countrys_update = request.POST.get('countrys_update')
        print(immigration_id,data_id,immigration_document_file_update,document_type_update,immigration_document_number_update,immigration_issue_date_update,immigration_expiry_date_update,countrys_update )
        user = CustomUser.objects.get(id=data_id)
        obj = Immegration.objects.get(user_id=user.id,id=immigration_id)
        obj.document_name=document_type_update
        obj.document_number=immigration_document_number_update
        obj.issue_date="-".join( immigration_issue_date_update.split("-"))
        obj.expired_date="-".join(immigration_expiry_date_update.split("-"))
        obj.country=countrys_update
        obj.document_file=immigration_document_file_update
        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)






def Add_emergency_contacts_data(request):
    if request.method == 'POST':


        relation = request.POST.get('relation')
        contact_work_email = request.POST.get('contact_work_email')
        contact_name = request.POST.get('contact_name')
        contact_address = request.POST.get('contact_address')
        mobile = request.POST.get('mobile')
        contact_city = request.POST.get('contact_city')
        contact_state = request.POST.get('contact_state')
        contact_zip = request.POST.get('contact_zip')
        country1 = request.POST.get('country1')
        data_id = request.POST.get('data_id')

        user = CustomUser.objects.get(id=data_id)




        print(relation,contact_work_email,contact_name,contact_address,mobile,contact_city,contact_state,contact_zip,country1)

        obj=Emergency_Contacts.objects.create(user_id=user.id, relation=relation,email=contact_work_email,name=contact_name,address=contact_address, mobile_no=mobile,city=contact_city,state=contact_state,zip_code=contact_zip,country=country1)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def update_emergency_contacts_data(request):


    if request.method == 'POST' and request.is_ajax():
        user = CustomUser.objects.get(id=request.user.id)
        data_id = request.POST.get('data_id')
        contact_id = request.POST.get('contact_id')
        relation_update= request.POST.get('relation_update')
        contact_work_email_update= request.POST.get('contact_work_email_update')
        contact_name_update = request.POST.get('contact_name_update')
        contact_address_update = request.POST.get('contact_address_update')
        mobile_update = request.POST.get('mobile_update')
        contact_city_update = request.POST.get('contact_city_update')
        contact_state_update = request.POST.get('contact_state_update')
        contact_zip_update = request.POST.get('contact_zip')
        country_update = request.POST.get('country_update')
        print(relation_update,contact_id,data_id, contact_work_email_update,country_update,contact_state_update,contact_zip_update,contact_city_update,contact_name_update, contact_address_update,mobile_update,contact_address_update)
        obj=Emergency_Contacts.objects.get(id=contact_id,user_id=data_id)
        obj.relation = relation_update
        obj.email = contact_work_email_update
        obj.name = contact_name_update
        obj.address = contact_address_update
        obj.mobile_no = mobile_update
        obj.city = contact_city_update
        obj.state = contact_state_update
        obj.zip_code = contact_zip_update
        obj.country = country_update
        obj.save()

        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def delete_emergency_contacts_data(request):
    if request.method == 'POST' and request.is_ajax():
        data_id = request.POST.get('data_id')
        contact_id = request.POST.get('contact_id')
        obj = Emergency_Contacts.objects.get(id=contact_id, user_id=data_id)
        obj.delete()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)




def get_emergency_contacts_data(request,id):
    if request.method == 'GET':
        emergency_contacts =Emergency_Contacts.objects.get(id=id)
        data = {
            "relation_update":emergency_contacts.relation,
            "contact_work_email_update": emergency_contacts.email,
            "contact_name_update": emergency_contacts.name,
            "contact_address_update": emergency_contacts.address,
            "mobile_update": emergency_contacts.mobile_no,
            "contact_city_update": emergency_contacts.city,
            "contact_state_update": emergency_contacts.state,
            "contact_zip_update": emergency_contacts.zip_code,
            "country_update": emergency_contacts.country,






                }
        return JsonResponse(data)


def Add_profile_data(request):
    if request.method == 'POST':



        fb_id = request.POST.get('fb_id')
        skype_id = request.POST.get('skype_id')
        linkedIn_id = request.POST.get('linkedIn_id')
        twitter_id = request.POST.get('twitter_id')
        whatsapp_id = request.POST.get('whatsapp_id')
        data_id = request.POST.get('data_id')
        user = CustomUser.objects.get(id=data_id)




        print(fb_id,skype_id,linkedIn_id,twitter_id,whatsapp_id)

        obj=Social_Profile.objects.create(user_id=user.id, facebook_profile=fb_id,linkedin_profile=linkedIn_id,skype_profile=skype_id,twitter_profile=twitter_id, whatsapp_profile=whatsapp_id)


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def update_profile_data(request):
    if request.method == 'POST':

        data_id = request.POST.get('data_id')
        profile_id = request.POST.get('profile_id')

        fb_id = request.POST.get('fb_id_update')
        skype_id = request.POST.get('skype_id_update')
        linkedIn_id = request.POST.get('linkedIn_id_update')
        twitter_id = request.POST.get('twitter_id_update')
        whatsapp_id = request.POST.get('whatsapp_id_update')

        print(fb_id, skype_id, linkedIn_id, twitter_id, whatsapp_id,data_id,profile_id)

        obj = Social_Profile.objects.get(user_id=data_id,id=profile_id)
        obj.facebook_profile=fb_id
        obj.linkedin_profile=linkedIn_id
        obj.skype_profile=skype_id
        obj.twitter_profile=twitter_id
        obj.whatsapp_profile=whatsapp_id

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


"""
def update_profile_data(request):
    if request.method == 'POST':

        data_id = request.POST.get('data_id')

        fb_id = request.POST.get('fb_id')
        skype_id = request.POST.get('skype_id')
        linkedIn_id = request.POST.get('linkedIn_id')
        twitter_id = request.POST.get('twitter_id')
        whatsapp_id = request.POST.get('whatsapp_id')




        print(fb_id,skype_id,linkedIn_id,twitter_id,whatsapp_id)
        CustomUser.objects.get(id=data_id)
        obj=Social_Profile.objects.create(user_id=data_id, facebook_profile=fb_id,linkedin_profile=linkedIn_id,skype_profile=skype_id,twitter_profile=twitter_id, whatsapp_profile=whatsapp_id)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def update_profile_record_data(request,id):
    user = CustomUser.objects.get(id=id)

    if request.method == 'POST' and request.is_ajax():
        pass


"""

def Add_documents_data(request):
    if request.method == 'POST' and request.FILES.get('document_document_file'):

        document_document_file= request.FILES['document_document_file']
        documents_type = request.POST.get('documents_type')
        document_title = request.POST.get('document_title')
        document_expiry_date = request.POST.get('document_expiry_date')
        document_description = request.POST.get('document_description')
        document_is_notify = request.POST.get('document_is_notify')
        data_id = request.POST.get('data_id')
        user = CustomUser.objects.get(id=data_id)



        print(documents_type,document_document_file,document_title,document_expiry_date,document_description,document_is_notify)

        obj=Documents_All.objects.create(user_id=user.id, document_name=documents_type,title=document_title,expired_date="-".join( document_expiry_date.split("-")),description=document_description,document_file=document_document_file)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def update_documents_data(request):


    if request.method == 'POST' and request.is_ajax() and request.FILES.get('document_document_file_update'):
      #  user = CustomUser.objects.get(id=request.user.id)

        document_document_file = request.FILES['document_document_file_update']
        data_id=request.POST.get('data_id')
        document_id = request.POST.get('document_id')
        documents_type = request.POST.get('documents_type_update')
        document_title = request.POST.get('document_title_update')
        document_expiry_date_update = request.POST.get('document_expiry_date_update')
        document_description = request.POST.get('document_description_update')

        user = CustomUser.objects.get(id=data_id)


        print(documents_type, document_id,data_id,document_document_file, document_title, document_expiry_date_update, document_description,
             )

        obj = Documents_All.objects.get(user_id=user.id, id= document_id)
        obj.document_name=documents_type
        obj.title=document_title
        obj.expired_date=document_expiry_date_update
        obj.description=document_description
        obj.document_file=document_document_file

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def delete_documents_data(request):


    if request.method == 'POST' and request.is_ajax() :
      #  user = CustomUser.objects.get(id=request.user.id)

     #   document_document_file = request.FILES['document_document_file_update']
        data_id=request.POST.get('data_id')
        document_id = request.POST.get('document_id')
        print(data_id,document_id)


        obj = Documents_All.objects.get(user_id=data_id, id= document_id)
        obj.delete()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)




def get_documents_data(request,id):


    if request.method == 'GET' :

        obj = Documents_All.objects.get(id=id)

        data = {
            'documents_type_update': obj.document_name,
            'document_title_update': obj.title,
            'document_expiry_date_update': obj.expired_date,
            'document_description_update': obj.description,

        }
        return JsonResponse(data, safe=False)



















def Add_qualifications_data(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        institution_name = request.POST.get('institution_name')
        education_level = request.POST.get('education_level')
        qualification_from_date = request.POST.get('qualification_from_date')
        qualification_to_date = request.POST.get('qualification_to_date')
        language = request.POST.get('language')
        professional_skills = request.POST.get('professional_skills')
        qualification_description = request.POST.get('qualification_description')
        data_id= request.POST.get('data_id')
        user = CustomUser.objects.get(id=data_id)





        print(institution_name,education_level,qualification_from_date,qualification_to_date,language,professional_skills,qualification_description)

        obj=Qualifications.objects.create(user_id=user.id, name_of_university=institution_name,branch=education_level,from_date=qualification_from_date,to_date=qualification_to_date, languages=language,skills=professional_skills,description=qualification_description)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def update_qualifications_data(request):


    if request.method == 'POST' and request.is_ajax():
        institution_name = request.POST.get('institution_name_update')
        education_level = request.POST.get('education_level_update')
        qualification_from_date = request.POST.get('qualification_from_date_update')
        qualification_to_date = request.POST.get('qualification_to_date_update')
        language = request.POST.get('language_update')
        professional_skills = request.POST.get('professional_skills_update')
        qualification_description = request.POST.get('qualification_description_update')
        data_id = request.POST.get('data_id')
        qualification_id = request.POST.get('qualification_id')

        print(data_id,qualification_id,institution_name,education_level,qualification_from_date,qualification_to_date,language,professional_skills,qualification_description)
        user = CustomUser.objects.get(id=data_id)
        obj = Qualifications.objects.get(user_id=data_id,id=qualification_id)
        obj.name_of_university=institution_name
        obj.branch=education_level
        obj.from_date=qualification_from_date
        obj.to_date=qualification_to_date
        obj.languages=language
        obj.skills=professional_skills
        obj.description=qualification_description
        obj.save()
        messages.success(request, 'Qualifications request submitted successfully.',extra_tags='alert alert-success alert-dismissible fade show')


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def delete_qualifications_data(request):


    if request.method == 'POST' and request.is_ajax():

        data_id = request.POST.get('data_id')
        qualification_id = request.POST.get('qualification_id')

        print(data_id,qualification_id)
        obj = Qualifications.objects.get(user_id=data_id, id=qualification_id)
        obj.delete()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def get_qualifications_data(request,id):


    if request.method == 'GET' :

        obj = Qualifications.objects.get(id=id)

        data = {
        'institution_name_update':obj.name_of_university,
       'education_level_update':obj.branch,
        'qualification_from_date_update':obj.from_date,
        'qualification_to_date_update':obj.to_date,
        'language_update':obj.languages,
        'professional_skills_update':obj.skills,
        'qualification_description_update':obj.description


        }
        return JsonResponse(data, safe=False)
















def Add_work_experience_data(request):
    if request.method == 'POST' and request.FILES.get('workex_document_file'):

        workex_document_file = request.FILES['workex_document_file']

        work_company_name = request.POST.get('work_company_name')
        work_experience_from_date = request.POST.get('work_experience_from_date')
        work_experience_to_date = request.POST.get('work_experience_to_date')
        designations = request.POST.get('designations')
        work_experience_description = request.POST.get('work_experience_description')
        data_id = request.POST.get('data_id')

        user = CustomUser.objects.get(id=request.user.id)






        print(work_company_name,work_experience_from_date,workex_document_file,work_experience_to_date,designations,work_experience_description)

        obj=Work_Experience.objects.create(user_id=user.id,company=work_company_name, document_file= workex_document_file ,from_date=work_experience_from_date,to_date=work_experience_to_date,description=work_experience_description,designation=designations)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def update_work_experience_data(request):


    if request.method == 'POST' and request.is_ajax() and request.FILES.get('workex_document_file_update'):

        workex_document_file = request.FILES['workex_document_file_update']

        work_company_name = request.POST.get('work_company_name_update')
        work_experience_from_date = request.POST.get('work_experience_from_date_update')
        work_experience_to_date = request.POST.get('work_experience_to_date_update')
        designations = request.POST.get('designations_update')
        work_experience_description = request.POST.get('work_experience_description_update')
        data_id = request.POST.get('data_id')
        workex_id = request.POST.get('workex_id')
        user = CustomUser.objects.get(id=data_id)
        print(work_experience_description,work_experience_to_date,work_experience_from_date,workex_document_file,work_company_name,designations)

        obj = Work_Experience.objects.get(user_id=data_id,id=workex_id)
        obj.company=work_company_name
        obj.document_file=workex_document_file
        obj.from_date=work_experience_from_date
        obj.to_date=work_experience_to_date
        obj.description=work_experience_description
        obj.designation=designations
        obj.save()

        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def delete_work_experience_data(request):


    if request.method == 'POST' and request.is_ajax() :


        data_id = request.POST.get('data_id')
        workex_id = request.POST.get('workex_id')

        obj = Work_Experience.objects.get(user_id=data_id,id=workex_id)

        obj.delete()

        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def get_work_experience_data(request,id):


    if request.method == 'GET':
        obj = Work_Experience.objects.get(id=id)
        data={
            'work_company_name_update':obj.company,
            'work_experience_from_date_update':obj.from_date,
            'work_experience_to_date_update':obj.to_date,
            'work_experience_description_update':obj.description,
             'designations_update': obj.designation,


           }
        print(data)
        return JsonResponse(data, safe=False)















def Add_bank_account_data(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        bank_account_title = request.POST.get('bank_account_title')
        bank_account_number = request.POST.get('bank_account_number')
        bank_bank_name = request.POST.get('bank_bank_name')
        bank_bank_code = request.POST.get('bank_bank_code')
        bank_bank_branch = request.POST.get('bank_bank_branch')






        print(bank_account_title,bank_account_number,bank_bank_name,bank_bank_code,bank_bank_branch)

        obj=Bank_Account.objects.create(user_id=user.id,account_title=bank_account_title,account_number=bank_account_number,bankname=bank_bank_name,ifsc_code=bank_bank_code,branch=bank_bank_branch)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def update_bank_account_data(request):


    if request.method == 'POST' and request.is_ajax():
        if request.method == 'POST':
            user = CustomUser.objects.get(id=request.user.id)

            bank_account_title = request.POST.get('bank_account_title_update')
            bank_account_number = request.POST.get('bank_account_number_update')
            bank_bank_name = request.POST.get('bank_bank_name_update')
            bank_bank_code = request.POST.get('bank_bank_code_update')
            bank_bank_branch = request.POST.get('bank_bank_branch_update')
            data_id = request.POST.get('data_id')
            bank_account_id = request.POST.get('bank_account_id')
            user = CustomUser.objects.get(id=data_id)
            obj = Bank_Account.objects.get(user_id=user.id,id=bank_account_id)
            obj.account_title=bank_account_title
            obj.account_number=bank_account_number
            obj.bankname=bank_bank_name
            obj.ifsc_code=bank_bank_code
            obj.branch=bank_bank_branch
            obj.save()

            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)




def get_bank_account_data(request,id):


    if request.method == 'GET' :
        obj=Bank_Account.objects.get(id=id)
        data={
        'bank_account_title_update':obj.account_title,
        'bank_account_number_update': obj.account_number,
        'bank_bank_name_update':  obj.bankname,
        'bank_bank_code_update': obj.ifsc_code,
        'bank_bank_branch_update': obj.branch,

        }
        return JsonResponse(data, safe=False)





























def delete_bank_account_data(request):


    if request.method == 'POST' and request.is_ajax():
        if request.method == 'POST':

            data_id = request.POST.get('data_id')
            bank_account_id = request.POST.get('bank_account_id')

            obj = Bank_Account.objects.get(user_id=data_id,id=bank_account_id)

            obj.delete()

            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)






















def Add_basic_salary_data(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        basic_Salary_mon = request.POST.get('basic_Salary_mon')
        payslip_type = request.POST.get('payslip_type')
        basic_salary_amount = request.POST.get('basic_salary_amount')







        print(basic_Salary_mon,payslip_type,basic_salary_amount)

        obj=Basic_Salary.objects.create(user_id=user.id,month_year=basic_Salary_mon,payslip_type=payslip_type,basic_salary=basic_salary_amount)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)





def update_basic_salary_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        basic_salary_id=request.POST.get('basic_salary_id')

        basic_Salary_mon_upd = request.POST.get('basic_Salary_mon_upd')
        payslip_type_upd = request.POST.get('payslip_type_upd')
        basic_salary_amount_upd = request.POST.get('basic_salary_amount_upd')




        print(basic_salary_id,data_id,basic_Salary_mon_upd,payslip_type_upd,basic_salary_amount_upd)








        user = CustomUser.objects.get(id=data_id)
        obj = Basic_Salary.objects.get(user_id=user.id,id=basic_salary_id)




        obj.month_year=basic_Salary_mon_upd
        obj.payslip_type=payslip_type_upd
        obj.basic_salary=basic_salary_amount_upd




        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)







def Add_allowances_data(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        mon_year = request.POST.get('mon_year')
        allowance_type = request.POST.get('allowance_type')
        allowance_title = request.POST.get('allowance_title')
        allowance_amount = request.POST.get('allowance_amount')







        print(mon_year,allowance_type,allowance_title,allowance_amount)

        obj=Allowances.objects.create(user_id=user.id,month_year=mon_year,allowance_type=allowance_type,allowance_title=allowance_title,allowance_amount=allowance_amount)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)





def update_allowances_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        allowances_id=request.POST.get('allowances_id')

        mon_year_upd = request.POST.get('mon_year_upd')
        allowance_type_upd = request.POST.get('allowance_type_upd')
        allowance_title_upd = request.POST.get('allowance_title_upd')
        allowance_amount_upd = request.POST.get('allowance_amount_upd')




        print(allowances_id,data_id,mon_year_upd,allowance_type_upd,allowance_title_upd,allowance_amount_upd)








        user = CustomUser.objects.get(id=data_id)
        obj = Allowances.objects.get(user_id=user.id,id=allowances_id)




        obj.month_year=mon_year_upd
        obj.allowance_type=allowance_type_upd
        obj.allowance_title=allowance_title_upd
        obj.allowance_amount=allowance_amount_upd



        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)






def Add_commissions_data(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        mon_year_c = request.POST.get('mon_year_c')
        commission_title = request.POST.get('commission_title')
        commission_amount = request.POST.get('commission_amount')




        print(mon_year_c,commission_title,commission_amount)

        obj=Commissions.objects.create(user_id=user.id,month_year=mon_year_c,commission_title=commission_title,commission_amount=commission_amount)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def update_commissions_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        commissions_id=request.POST.get('commissions_id')

        mon_year_c_upd = request.POST.get('mon_year_c_upd')
        commission_title_upd = request.POST.get('commission_title_upd')
        commission_amount_upd = request.POST.get('commission_amount_upd')




        print(commissions_id,data_id,mon_year_c_upd,commission_title_upd,commission_amount_upd)








        user = CustomUser.objects.get(id=data_id)
        obj = Commissions.objects.get(user_id=user.id,id=commissions_id)




        obj.month_year=mon_year_c_upd
        obj.commission_title=commission_title_upd
        obj.commission_amount=commission_amount_upd



        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)






def Add_loan_data(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        mon_year_l = request.POST.get('mon_year_l')
        title_l = request.POST.get('title_l')
        number_of_installments = request.POST.get('number_of_installments')
        loan_option = request.POST.get('loan_option')
        amount_l = request.POST.get('amount_l')
        reason_l = request.POST.get('reason_l')




        print(mon_year_l,title_l,number_of_installments,loan_option,amount_l,reason_l)

        obj=Loan.objects.create(user_id=user.id,month_year=mon_year_l,title=title_l,number_of_installments=number_of_installments,loan_option=loan_option,amount=amount_l,reason=reason_l)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)





def update_loan_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        loan_id=request.POST.get('loan_id')

        mon_year_l_upd = request.POST.get('mon_year_l_upd')
        title_l_upd = request.POST.get('title_l_upd')
        number_of_installments_upd = request.POST.get('number_of_installments_upd')
        loan_option_upd = request.POST.get('loan_option_upd')
        amount_l_upd = request.POST.get('amount_l_upd')
        reason_l_upd = request.POST.get('reason_l_upd')



        print(loan_id,data_id,mon_year_l_upd,title_l_upd,number_of_installments_upd,loan_option_upd,amount_l_upd,reason_l_upd)








        user = CustomUser.objects.get(id=data_id)
        obj = Loan.objects.get(user_id=user.id,id=loan_id)




        obj.month_year=mon_year_l_upd
        obj.title=title_l_upd
        obj.number_of_installments=number_of_installments_upd
        obj.loan_option = loan_option_upd
        obj.amount = amount_l_upd
        obj.reason = reason_l_upd



        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)









def Add_statutory_deduction_data(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        mon_year_s = request.POST.get('mon_year_s')
        title_s = request.POST.get('title_s')
        deduction_option = request.POST.get('deduction_option')
        deduction_amount = request.POST.get('deduction_amount')
        reason_s = request.POST.get('reason_s')





        print(mon_year_s,title_s,deduction_option,deduction_amount,reason_s)

        obj=Statutory_Deduction.objects.create(user_id=user.id,month_year=mon_year_s,deduction_title=title_s,deduction_option=deduction_option,deduction_amount=deduction_amount,reason=reason_s)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)









def update_statutory_deduction_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        statutory_deduction_id=request.POST.get('statutory_deduction_id')

        mon_year_s_upd = request.POST.get('mon_year_s_upd')
        title_s_upd = request.POST.get('title_s_upd')
        deduction_option_upd = request.POST.get('deduction_option_upd')
        deduction_amount_upd = request.POST.get('deduction_amount_upd')
        reason_s_upd = request.POST.get('reason_s_upd')



        print(statutory_deduction_id,data_id,mon_year_s_upd,title_s_upd,deduction_option_upd,deduction_amount_upd,reason_s_upd)








        user = CustomUser.objects.get(id=data_id)
        obj = Statutory_Deduction.objects.get(user_id=user.id,id=statutory_deduction_id)




        obj.month_year=mon_year_s_upd
        obj.deduction_title=title_s_upd
        obj.deduction_option=deduction_option_upd
        obj.deduction_amount = deduction_amount_upd
        obj.reason = reason_s_upd



        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)









def Add_other_payments_data(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        mon_year_p = request.POST.get('mon_year_p')
        title_p = request.POST.get('title_p')
        amount_p = request.POST.get('amount_p')






        print(mon_year_p,title_p,amount_p)

        obj=Other_Payments.objects.create(user_id=user.id,month_year=mon_year_p,title=title_p,amount=amount_p)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)





def update_other_payments_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        other_payments_id=request.POST.get('other_payments_id')

        mon_year_p_upd = request.POST.get('mon_year_p_upd')
        title_p_upd = request.POST.get('title_p_upd')
        amount_p_upd = request.POST.get('amount_p_upd')



        print(other_payments_id,data_id,mon_year_p_upd,title_p_upd,amount_p_upd)








        user = CustomUser.objects.get(id=data_id)
        obj = Other_Payments.objects.get(user_id=user.id,id=other_payments_id)




        obj.month_year=mon_year_p_upd
        obj.title=title_p_upd
        obj.amount=amount_p_upd



        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)













def Add_over_time_data(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)

        mon_year_o = request.POST.get('mon_year_o')
        title_o = request.POST.get('title_o')
        number_of_days = request.POST.get('number_of_days')
        total_hours = request.POST.get('total_hours')
        rate = request.POST.get('rate')






        print(mon_year_o,title_o,number_of_days,total_hours,rate)

        obj=Over_Time.objects.create(user_id=user.id,month_year=mon_year_o,title=title_o,number_of_days=number_of_days,total_hours=total_hours,rate=rate)

        obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)









def update_over_time_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        over_time_id=request.POST.get('over_time_id')

        mon_year_o_upd = request.POST.get('mon_year_o_upd')
        title_o_upd = request.POST.get('title_o_upd')
        number_of_days_upd = request.POST.get('number_of_days_upd')
        total_hours_upd = request.POST.get('total_hours_upd')
        rate_upd = request.POST.get('rate_upd')


        print(over_time_id,data_id,mon_year_o_upd,title_o_upd,number_of_days_upd,total_hours_upd,rate_upd)








        user = CustomUser.objects.get(id=data_id)
        obj = Over_Time.objects.get(user_id=user.id,id=over_time_id)

        obj.month_year=mon_year_o_upd
        obj.title=title_o_upd
        obj.number_of_days=number_of_days_upd
        obj.total_hours=total_hours_upd
        obj.rate=rate_upd

        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)





























def create(request):
    if request.is_ajax and request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        print(name,email)
        profile= Pro.objects.create(name=name,email=email)
        profile.save()
        success= 'User'+name+'created successfully'
        response_data = {'message': f"Form submitted successfully. Name: {name}, Email: {email}"}
        return HttpResponse(success)


def update_p(request,id):
    profile= get_object_or_404(Pro, pk=id)
    if request.method == 'POST':
        profile.name = request.POST['name']
        profile.description = request.POST['description']
        profile.save()
        return JsonResponse({'message': 'Item updated successfully.'})
    return JsonResponse({'message': 'Invalid request method.'}, status=400)


def get_item(request, id):
    item = get_object_or_404(Pro, pk=id)
    data = {'name': item.name, 'description': item.email}
    return JsonResponse(data)













def my_get_view(request):
    data = list(Pro.objects.values())
    return JsonResponse(data, safe=False)








def get_events(request):
    events = Event.objects.all()
    events_data = list(events.values('title', 'description', 'date'))


    return JsonResponse(events_data, safe=False)

   # events = Event.objects.all()

  #  events_data = list(events.values('title', 'description', 'date'))

   # return JsonResponse(events_data, safe=False)
import pandas as pd


# d=datetime.date()
#  print(d)
#   date_series = pd.date_range('08/10/2019', periods=12, freq='D')
#  print(date_series)
def test(request):



   return render(request,'hr/employee_details.html',)

@login_required(login_url='/login/')
def home(request):
    if request.user.is_authenticated :

        user = CustomUser.objects.get(id=request.user.id)
        print(user)
        if user.is_employee == True:

            emp_data = EmployeeMaster.objects.get(user_id=user.id)
            public_holidays= Public_holidays.objects.all()
            birthdays=EmployeeMaster.objects.all()

            start_date =datetime.date.today()+datetime.timedelta(days=1)
            end_date = datetime.datetime(2023, 8, 1) # Two months have a maximum of 60 days
            punch_records = Attendance.objects.filter(employee=request.user.id, timestamp__range=(end_date,start_date )).all()
            return render(request, 'dashboards.html',
                          {'emp_data': emp_data, 'public_holidays': public_holidays, 'birthdays': birthdays,
                           'punch_records': punch_records})
        elif user.is_manager == True:
            return render(request,'hr/hr_dashboard.html')

        elif user.is_hr == True:
            return render(request, 'hr/hr_dashboard.html')
    else:
        return render(request,'login1.html')

    #return render(request,'dashboards.html',{'emp_data': emp_data,'public_holidays':public_holidays,'birthdays':birthdays,'punch_records': punch_records})













def emp(request):
    form= EmployeeMaster.objects.all()

    k=type(form.CreatedDate)
    return render(request,'view.html',{'form':form,"k":k})
"""
def Register(request):
    if request.method == "GET":
        form=RegisterForm()

    return render(request,'signup.html',{'form':form})

"""


def signup_view(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        form1=EmployeeMasterForm(request.POST,request.FILES)
        if form.is_valid() and form1.is_valid():

           # is_manager = form.cleaned_data['is_manager']
          #  is_employee = form.cleaned_data['is_employee']
        #    is_hr = form.cleaned_data['is_hr']

         #   if is_manager:
           #     user.is_manager = True
      #      if is_employee:
         #       user.is_employee = True
        #    if is_hr:
        #        user.is_hr = True

            u= form.save()

            u = form.save()
            k = form1.save(commit=False)
            k.user = u
            k.save()

            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = CustomUpdateForm()
        form1 = EmployeeMasterForm()

    return render(request, 'signup2.html', {'form': form,'form1':form1})





def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            print(user)
            auth_login(request, user)

            return redirect('home')


            # Check the user's role and redirect accordingly
            #if user.is_manager:
               # return redirect('home')  # Redirect to manager's home page
          #  elif user.is_employee:
                #return redirect('home')  # Redirect to employee's home page
          #  elif user.is_hr:
                #return redirect('home')  # Redirect to HR's home page
         #   else:
                # User has noERROR specific role or unknown role
                #return redirect('home')  # Redirect to default home page
        else:
            # Invalid credentials
            messages.error(request, 'invalid credentials.',extra_tags='alert alert-danger alert-dismissible fade show')
            return render(request, 'login1.html', {'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
        return render(request, 'login1.html', {'form': form})





def logout_view(request):
   logout(request)
   messages.info(request, 'successfully logout',extra_tags='alert alert-danger alert-dismissible fade show')
   return redirect('login')



def employee_detail(request,id):
    if request.method == "GET":
        user1 = CustomUser.objects.get(id=id)
        emp_obj = EmployeeMaster.objects.get(user_id=user1.id)
        return render(request,'details.html',{"emp_obj":emp_obj,"user":user1})













def Register(request):
    if request.method == "GET":
        form = RegisterForm()
        form1=EmployeeMasterForm()
        return render(request,"signup2.html",{"form":form,"form1":form1})
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        form1 = EmployeeMasterForm(request.POST,request.FILES)
        print(form.is_valid)

        if  form.is_valid() and  form1.is_valid():
            print(form)
            u=form.save()
            k=form1.save(commit=False)
            k.user=u
            k.save()
            return redirect('login')
        else:
            return HttpResponse("requist is not valid")





def update_emp(request,id):
        user = CustomUser.objects.get(id=id)
        emp_edit = EmployeeMaster.objects.get(user_id=user.id)
        if request.method == "POST":
            username = request.POST['username']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']

            user.username = username
            user.first_name = firstname
            user.last_name =  lastname
            user.email = email
            user.save()
            form1 = EmployeeMasterForm(request.POST ,instance=emp_edit)






            if form1.is_valid():

                form1.save()
                return redirect("home")
               # user = form.save()
               # profile = form1.save(commit=False)
               # profile.user_id = user.id
              #  profile.save()



        else:
            form = CustomUpdateForm( instance=user)
            form1 = EmployeeMasterForm( instance=emp_edit)

            return render(request,'emp_update.html',{"form": form,"form1":form1,"user":user,"emp_edit":emp_edit})











def delete_emp(request,id):
    user = CustomUser.objects.get(id=id)
    user.delete()
    return redirect("home")








def details_view(request,id):
    if request.method == "GET":
        user1 = CustomUser.objects.get(id=id)
        emp_obj = EmployeeMaster.objects.get(user_id=user1.id)
        if request.user.is_employee == True:
            return render(request,'profile.html',{"emp_obj":emp_obj,"user":user1})
        else :
            return render(request, 'hr/profile.html', {"emp_obj": emp_obj, "user": user1})



    elif request.method == "POST" and request.FILES.get('img'):
        user1 = CustomUser.objects.get(id=id)
        emp_obj1 = EmployeeMaster.objects.get(user_id=user1.id)
       # username = request.POST['username']
        fullname = request.POST['fullName']
        phonenumber=request.POST['phone']
        email=request.POST['email']
        city = request.POST['city']
        address=request.POST['address']
        shifttime=request.POST.get('shift')
        MaratialStatus=request.POST.get('MaratialStatus')
        Date_of_birth=request.POST['dob']
        profile= request.FILES['img']
        educationtype=request.POST.get('education type')
        designation=request.POST.get('designation')
        branch=request.POST.get('branch')
        passingyear=request.POST['passingyear']
        university = request.POST['university']

        print(fullname,phonenumber,email,address,shifttime,MaratialStatus,Date_of_birth,profile,educationtype,designation,branch,passingyear)


        user1.email=email
        user1.save()

        emp_obj1.fullname= fullname
        emp_obj1.phone_number=phonenumber
        emp_obj1.City = city
        emp_obj1.Address=address
        emp_obj1.Shift_time=shifttime
        emp_obj1.MaratialStatus=MaratialStatus
        emp_obj1.BirthDate="-".join(Date_of_birth.split("-"))


        emp_obj1.Education_type=educationtype
        emp_obj1.university = university
        emp_obj1.Designation=designation
        emp_obj1.Branch=branch
        emp_obj1.passing_year= passingyear
        emp_obj1.image =profile
        emp_obj1.save()
        return redirect('http://127.0.0.1:8000/details/{}/'.format(emp_obj1.user_id))

    elif request.method== "POST":
        username = request.POST['username']
        newpassword = request.POST['newpassword']
        confirmpassword = request.POST['confirmpassword']
        if newpassword !=confirmpassword:
            return HttpResponse("password is not same")
        u = CustomUser.objects.get(username__exact=username)
        u.set_password(confirmpassword)
        u.save()
        html = "password is changed successfully " +'<a href="http://127.0.0.1:8000/login/"> Login </a>'
        return HttpResponse(html)






        print(fullname)
       # lastname = request.POST['lastname']
       # email = request.POST['email']

      #  user.username = username
      #  user.first_name = firstname
      #  user.last_name = lastname
      #  user.email = email
      #  user.save()
       # form1 = EmployeeMasterForm(request.POST, instance=emp_obj)

        #if form1.is_valid():
         #   form1.save()
         #   return redirect("home")
        # user = form.save()
        # profile = form1.save(commit=False)
        # profile.user_id = user.id
        #  profile.save()





      #  return render(request, 'profile.html', {"form": form, "form1": form1, "user": user, "emp_edit": emp_edit})








@login_required(login_url="/login/")
def Register_view(request):
    if request.method == 'GET':
        return render(request, 'signup4.html')

    if request.method == 'POST' and request.FILES.get('profile_photo'):

        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['conformpassword']

        fullname = request.POST['fullname']
        email = request.POST['email']
        gender = request.POST.get('gender')
        department = request.POST.get('department')
        company = request.POST['company']
        worktype = request.POST.get('worktype')
        dob = request.POST['dob']
        employeeid = request.POST['employeeid']
        doj = request.POST['dateofjoining']
        role = request.POST.get('role')
        shift = request.POST.get('shift')
        phone = request.POST['phonenumber']
        city = request.POST['city']
        pincode = request.POST['pincode']
        designation = request.POST.get('designation')

        profile = request.FILES['profile_photo']

        print(fullname, dob ,department,phone,doj,worktype, designation,pincode,city,profile)


        user=CustomUser.objects.create_user(username=username,email=email)
        user.set_password(password)
        if designation == "employee":
            user.is_employee=True
        elif designation  == "hr":
            user.is_hr = True
        elif designation  == "manager":
            user.is_manager = True

        user.save()
        emp = EmployeeMaster.objects.create(user=user, EmployeeID=employeeid, Gender=gender, Role=role,
                                            Shift_time=shift, fullname=fullname, Department=department, BirthDate=dob,
                                            companyname=company, City=city, PinCode=pincode,
                                            JoiningDate=doj, image=profile )
        emp.save()
        messages.success(request, 'You are successfully signup',extra_tags='alert alert-success alert-dismissible fade show')  #
        return redirect('login')

    else:
        messages.success(request, 'You have singed up not successfully.',extra_tags='alert alert-error alert-dismissible fade show')



@login_required(login_url="/login/")
def Add_employee_view(request):
    if request.method == 'GET':
        return render(request, 'add_employee.html')

    if request.method == 'POST' and request.FILES.get('profile_photo'):

        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['conformpassword']

        fullname = request.POST['fullname']
        email = request.POST['email']
        gender = request.POST.get('gender')
        department = request.POST.get('department')
        company = request.POST['company']
        worktype = request.POST.get('worktype')
        dob = request.POST['dob']
        employeeid = request.POST['employeeid']
        doj = request.POST['dateofjoining']
        role = request.POST.get('role')
        shift = request.POST.get('shift')
        phone = request.POST['phonenumber']
        city = request.POST['city']
        pincode = request.POST['pincode']
        designation = request.POST.get('designation')

        profile = request.FILES['profile_photo']

        print(fullname, dob ,department,phone,doj,worktype, designation,pincode,city,profile)


        user=CustomUser.objects.create_user(username=username,email=email)
        user.set_password(password)
        if designation == "employee":
            user.is_employee=True
        elif designation  == "hr":
            user.is_hr = True
        elif designation  == "manager":
            user.is_manager = True

        user.save()
        emp = EmployeeMaster.objects.create(user=user, EmployeeID=employeeid, Gender=gender, Role=role,
                                            Shift_time=shift, fullname=fullname, Department=department, BirthDate=dob,
                                            companyname=company, City=city, PinCode=pincode,
                                            JoiningDate=doj, image=profile )
        emp.save()
        messages.success(request, 'You are successfully signup',extra_tags='alert alert-success alert-dismissible fade show')  #
        return redirect('login')

    else:
        messages.success(request, 'You have singed up not successfully.',extra_tags='alert alert-error alert-dismissible fade show')




def birthdays(request):
    birthday=EmployeeMaster.objects.all()
    return render(request,'k5.html',{'data':birthday})

















"""


def Registr(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    if request.method == 'POST':
        #form = RegisterForm(request.POST)
      #  form1 = EmployeeMasterForm(request.POST)
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        confirmpassword = request.POST['cpwd']
        Email = request.POST['email']
        dob = request.POST['dob']
        empid = request.POST['empid']
        course = request.POST.get('course')
        department = request.POST.get('department')
        phone = request.POST['phno']
        gender = request.POST.get('gender')
        role = request.POST.get('role')
        shift = request.POST.get('shift')
        category = request.POST.get('category')

        print(username,firstname,password,Email, dob,empid ,course,department,phone, gender,role,shift,category)
        if len(username) < 5 or len(username) > 8:
            raise ValidationError(f'Length of the name:{username} is not between 5 -7 characters')
        if (password != confirmpassword):
            raise ValidationError("pasword and confirm password's is  not same")

        user=CustomUser.objects.create(username=username,first_name=firstname,last_name=lastname,password=password,email=Email)
        if category== "Employee":

            user.is_employee=True
        elif category == "Hr":
            user.is_hr = True
        elif category == "Manager":
            user.is_manager = True
        user.save()
        emp=EmployeeMaster.objects.create(user=user,EmployeeID=empid,Gender=gender,Role=role,Shift_time=shift)
        emp.save()
        messages.success(request, 'You .')  #
        return redirect('login')

    else:
        messages.success(request, 'You have singed up not successfully.')





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')



        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

          #  return redirect('login')

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

"""





def logout_view(request):
    logout(request)
    return redirect('login')




def Emp_list(request):
    data=EmployeeMaster.objects.all()
    return render(request,'hr/emp_data.html',{'data':data})





def Birthday(request):
    pass













#Leave related views

def leave_request_view(request):
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST, request.FILES)
        employee_name=request.POST['employeename']
        category = request.POST.get('category')
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        totaldays = request.POST['totaldays']
        reason = request.POST['reason']
        comments = request.POST['comments']
        halfday_vlue=request.POST.getlist('check')
       # secondhalfday= request.POST.get('check')


        print(employee_name,startdate,enddate,totaldays,category,reason,comments)
        user=CustomUser.objects.get(id=request.user.id)
        leavecategory = get_object_or_404(Leavecategory, name=category)


        obj=LeaveRequest(employee=user,LeaveCategory=leavecategory,StartDate=startdate,EndDate=enddate,totaldays=totaldays,reason=reason,comments=comments,)

        if len(halfday_vlue) == 1:
            for i in halfday_vlue:
                if i == "start_date_half":
                    obj.isfirst_halfday = True
                if i == "end_date_half":
                    obj.islast_halfday = True
        else:

            obj.isfirst_halfday = True
            obj.islast_halfday = True

        obj.save()

        return redirect('leave_request_success')  # Redirect to a success page
    else:
        form = LeaveRequestForm()

    context = {
        'form': form
    }
    return render(request, 'leave/leave_request.html', context)



def leave_request_success_view(request):
    return render(request, 'leave/leave_request_success.html')


def leave_approval_view(request, request_id):
    leave_request = get_object_or_404(LeaveRequest, id=request_id)

    if request.method == 'POST':
        # Handle the approval logic

        approval_status = request.POST.get('approval_status')
        approvername=request.POST['approvername']
        print(approval_status)
        comments = request.POST.get('comments')
        if (approval_status == "approved"):
            leave_request.status= "Approved"
            leave_request.IsActive = False
        elif (approval_status == "rejected"):
            leave_request.status = "Rejected"
            leave_request.IsActive = False

        else:
            leave_request.status = "Pending"





        leave_request.comments = comments
        leave_request.approvedby=approvername

        # Create a notification
        recipient = leave_request.employee
        print(recipient)
        message = "Your leave request with {},Id{} has been {}".format(str(leave_request.employee),leave_request.id, approval_status)
        notification = Notification(recipient=recipient, message=message,  notification_type="Leave")
        notification.save()
        leave_request.save()

        if request.user.is_employee == "True":
            return redirect('leave_request_list')  # Redirect to a leave request list page or success page
        else :
            return redirect('home')

    context = {
        'leave_request': leave_request,
    }

    return render(request, 'leave/approval.html', context)

def leave_approvals_pending(request):
    pending_requests=LeaveRequest.objects.filter(IsActive=True).all()
    return render(request,'leave/pending_approvals.html',{'pendingapprovals':pending_requests})





#manager or Hr side

def leave_request_list_view(request):
    if request.user.is_authenticated:
        user = CustomUser.objects.get(id=request.user.id)
        emp = EmployeeMaster.objects.filter(user_id=user.id)
    leave_requests = LeaveRequest.objects.filter(employee_id=user.id)  #leave_requests = LeaveRequest.objects.all()
    context = {
        'leave_requests': leave_requests,
     }
    return render(request, 'leave/leave_request_list.html', context)


#manager or Hr side
"""
def leave_request_list_view(request):
   #leave_requests = LeaveRequest.objects.filter(IsActive=True)
   leave_requests = LeaveRequest.objects.all()
   context = {
        'leave_requests': leave_requests,
    }
   return render(request, 'leave/leave_request_list.html', context)
"""



def notification_view(request):
   # notification =Notification.objects.all()
    notifications = Notification.objects.filter(status=False).count()

       # Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    context = {
        'notifications': notifications
    }
    return render(request, 'leave/notification.html', context)



def Notifyed(request,id):

    obj=Notification.objects.get(id=id)
    obj.status=True
    obj.save()
    user =CustomUser.objects.get(id=obj.recipient.id)

    id_1=EmployeeMaster.objects.get(user_id=user.id)
    print(id_1.user_id)

    return redirect('http://127.0.0.1:8000/details/{}/'.format(id_1.user_id))














def permission_request_view(request):
    if request.method== "POST":
        employee_name = request.POST['employeename']
        permission_category = request.POST.get('category')
        startdate = request.POST['startdate']
        enddate = request.POST['enddate']
        starttime = request.POST['start-time']
        endtime = request.POST['end-time']
        duration= request.POST['duration']
        location = request.POST['location']
        reason= request.POST['reason']
        print(employee_name,permission_category,startdate,enddate,starttime,endtime,duration,location,reason)
        user = CustomUser.objects.get(id=request.user.id)
        if permission_category == "WFH":
            obj = Permission(employee=user, permission_category=permission_category, StartDate=startdate,
                             EndDate=enddate,
                             location=location, Time_duration=duration + "days", reason=reason)
        else:
            obj = Permission(employee=user, permission_category=permission_category, StartDate=startdate,
                             EndDate=enddate, start_time=starttime, end_time=endtime, Time_duration=duration,
                             reason=reason)

        obj.save()
        obj1 = PermissionApproval(permission=obj)
        obj1.save()
        return redirect('permission_request_success')



    return render(request,'permission/permission_request.html')


def permission_request_success_view(request):
    return render(request, 'permission/permission_request_success.html')










def permission_approval_view(request, request_id):
    permission = get_object_or_404(Permission, id=request_id)
    permission_request=PermissionApproval.objects.get(permission_id=permission.id)

    if request.method == 'POST':
        # Handle the approval logic
        approval_status = request.POST.get('approval_status')
        approvername = request.POST['approvername']
        print(approval_status)
        comments = request.POST.get('comments')
        if (approval_status == "approved"):
            permission_request.approval_status= "Approved"
            permission.status = False
        elif (approval_status == "rejected"):
            permission_request.approval_status= "Rejected"
            permission.status = False

        else:
            permission_request.approval_status== "Pending"



        permission_request.comments = comments
        permission_request.approver=  approvername

        # Create a notification
        recipient = permission.employee
        print(recipient)
        message = "Your leave request with {},ID {} has been {}".format(str( permission.employee), permission.id, approval_status)
        notification = Notification(recipient=recipient, message=message, notification_type= "permission")
        notification.save()
        permission.save()
        permission_request.save()


        return redirect('leave_request_list')  # Redirect to a leave request list page or success page

    context = {
        'permission': permission,
    }
    return render(request, 'permission/permisson_approval.html', context)




def permission_request_list_view(request):
    if request.user.is_authenticated:
        if request.user.is_employee == True:
            user = CustomUser.objects.get(id=request.user.id)
            # emp = EmployeeMaster.objects.filter(user_id=user.id)
            permission = Permission.objects.all().filter(employee_id=user.id)
            print(permission)
            #leave_requests = LeaveRequest.objects.all()
            permissionapprove=PermissionApproval.objects.all().filter(permission_id__in=[k.id  for k in permission])
            context = {
               "list": zip(permission,permissionapprove)
            }
            return render(request, 'permission/permission_request_list.html', context)
        if request.user.is_hr== True:
            user = CustomUser.objects.get(id=request.user.id)
            # emp = EmployeeMaster.objects.filter(user_id=user.id)
            permission = Permission.objects.all().filter(employee_id=user.id)
            print(permission)
            #leave_requests = LeaveRequest.objects.all()
            permissionapprove=PermissionApproval.objects.all().filter(permission_id__in=[k.id  for k in permission])
            context = {
               "list": zip(permission,permissionapprove)
            }
            return render(request, 'hr/pending_permission_request_list.html', context)
        if request.user.is_manager== True:
            permissionapprove = PermissionApproval.objects.all().filter(approval_status ="Pending")
            context = {
                'permissionapprove':permissionapprove
            }

            return render(request, 'hr/pending_permission_request_list.html', context)










def Attendance_view(request):
    user = CustomUser.objects.get(id=request.user.id)
    emp_data = EmployeeMaster.objects.get(user_id=user.id)
    return render(request, 'attendence/attendence.html',{'emp_data':emp_data})

@csrf_exempt
def punch(request):
    user = CustomUser.objects.get(id=request.user.id)
    if request.method=='POST':

        punch=request.POST.get('action')

        print(punch)

        if punch == "Punch_In":
            obj = Attendance.objects.create(employee_id=user.id)
            obj.entry_type="PunchIn"
            obj.timestamp = timezone.now()
        elif punch == "Punch_Out":
            obj = Attendance.objects.create(employee_id=user.id)
            obj.entry_type = "PunchOut"
            obj.timestamp =timezone.now()
        elif punch == "Break_In":
            obj = Attendance.objects.create(employee_id=user.id)
            obj.entry_type = "BreakIn"
            obj.timestamp = timezone.now()
        elif punch == "Break_Out":
            obj = Attendance.objects.create(employee_id=user.id)
            obj.entry_type = "BreakOut"
            obj.timestamp = timezone.now()
        obj.save()
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


def Attndence_Records(request):
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    now=datetime.datetime.now()
    current_datetime = timezone.now()
    print(current_datetime)
    user = CustomUser.objects.get(id=request.user.id)
    obj = Attendance.objects.filter(employee_id= user.id,timestamp__lte=current_datetime).order_by('timestamp').all()

    return render(request,'attendence/attendece_records.html',{'obj':obj})





def daywise_records(request):
    start_date =datetime.datetime(2023, 7, 7)
    end_date = datetime.datetime(2023,8,7)  # Two months have a maximum of 60 days
    punch_records = Attendance.objects.filter(employee=1, timestamp__gte=start_date, timestamp__lt=end_date)
    return render(request,'k5.html',{'punch_records': punch_records})















    #if punch =="Punch_in":
     #    obj.punch_in=timezone.now()
   # elif punch == "Punch_Out":
    #    obj.punch_out= timezone.now()
  #  elif punch == "Break_In":
    #        obj.break_in  = timezone.now()
  #  elif punch == "Break_Out":
       #     obj.break_out  = timezone.now()

       # obj.save()


   # return render(request,'k.html')
                  #'attendence/attendence.html')
                         # 'attendence/attendence.html'
                  #'k.html')








def punch_in_prasent(request):
    if request.method == 'GET':
        date=datetime.date.today()
        print(date)
        user = CustomUser.objects.get(id=request.user.id)
        is_punch_in_present = Attendance.objects.filter(employee_id=user.id,entry_type = "PunchIn",timestamp__startswith=date).exists()
        is_punch_out_present = Attendance.objects.filter(employee_id=user.id, entry_type="PunchOut",timestamp__startswith=date).exists()
        is_break_in_present = Attendance.objects.filter(employee_id=user.id, entry_type="BreakIn",timestamp__startswith=date).exists()
        is_break_out_present = Attendance.objects.filter(employee_id=user.id, entry_type="BreakOut",timestamp__startswith=date).exists()
        print(is_punch_in_present)
        return JsonResponse({'is_punch_in_present': is_punch_in_present,
                             'is_punch_out_present':is_punch_out_present,
                             'is_break_in_present':is_break_in_present,
                              'is_break_out_present': is_break_out_present



                             })


def punch_out(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(id=request.user.id)
        obj = Attendance.objects.create(employee_id=user.id)
        obj.entry_type = "PunchOut"
        obj.timestamp = timezone.now()
        obj.save()
        return HttpResponse("home")








"""
def Calculation_view(request):
    sum=0
    if request.method=="POST":
        val = request.POST['value']
        obj1 = Calculation.objects.all()
        if obj1:
            k=[obj1.id for obj1 in Calculation.objects.all()][-1]
            s=Calculation.objects.get(id=k)
            sum=int(s.sum)+int(val)
        else:
            sum=sum+int(val)
        obj = Calculation.objects.create(value=val,sum=sum)
        obj.save()
        return redirect("calculate")


    elif request.method == "GET":
        obj1 = Calculation.objects.all()

        return render(request, 'cal.html',{"obj":obj1} )

"""















"""
    def emp_update(request,id):
        if request.method == 'POST':
            username = request.POST['username']
            obj=User.objects.get(username=username)
            print(obj)
            obj1=EmployeeMaster.objects.get(user=obj)
            print(obj1)
            username = request.POST['username']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = request.POST['password']
            confirmpassword = request.POST['cpwd']
            Email = request.POST['email']
            dob = request.POST['dob']
            empid = request.POST['empid']
            course = request.POST.get('course')
            department = request.POST.get('department')
            phone = request.POST['phno']
            gender = request.POST.get('gender')
            role = request.POST.get('role')
            shift = request.POST.get('shift')
            category = request.POST.get('category')


        else:
            return render(request,'emp_update.html')

    """


#=============================
#=============================

#HR RELATED VIEWS

def Hr_view(request):
    if request.user.is_authenticated:
        if request.user.is_manager== True:
            return render(request,'hr/hr_dashboard.html')








def Add_project(request):
    if request.method=='POST':
        project_title = request.POST.get('project_title')
        client = request.POST.get('client')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        company = request.POST.get('company')
        priority = request.POST.get('Priority')
        employee = request.POST['employee']
        summary = request.POST.get('summary')
        progress = request.POST.get('progress')
        print(project_title,client,start_date,end_date,company,priority,employee.split(","),summary,progress)
        obj=Projects.objects.create(title=project_title,client_id=client,company_id=company,start_date=start_date,end_date=end_date,priority=priority,summary=summary,Progress=progress+" Completed")

        for user_id in employee.split(","):
            user_instance = CustomUser.objects.get(pk=user_id)
            obj.Assigned_employees.add(user_instance)
            obj.save()
        return render(request,'hr/project/add_project.html')

    else:
        clients=Client.objects.all()
        employees=CustomUser.objects.all()
        camp = Company.objects.all()
        all_projects_with_employees = Projects.objects.all().prefetch_related('Assigned_employees')


        context={
            'all_projects_with_employees': all_projects_with_employees,
            'clients': clients,
            'employees': employees,
            'camp': camp,
        }

        return render(request,'hr/project/add_project.html',context)



def Update_project_details(request):
    if request.method=='POST':
        project_title = request.POST.get('project_title_upd')
        client = request.POST.get('client_upd')
        start_date = request.POST.get('start_date_upd')
        end_date = request.POST.get('end_date_upd')
        company = request.POST.get('company_upd')
        priority = request.POST.get('Priority_upd')
        employee = request.POST['employees_upd']
        summary = request.POST.get('summary_upd')
        progress = request.POST.get('progress_upd')
        project_id = request.POST.get('project_id')
      #  data_id = request.POST.get('data_id')

        print(project_id,progress,summary,employee,priority,company,end_date,start_date,client,project_title)

        obj=Projects.objects.get(id=project_id)
        obj.title=project_title
        obj.client_id=client
        obj.company_id=company
        obj.start_date=start_date
        obj.end_date=end_date
        obj.priority=priority
        obj.summary=summary
        obj.Progress=progress+" Completed"
        for user_id in employee.split(","):
            user_instance = CustomUser.objects.get(pk=user_id)
            obj.Assigned_employees.add(user_instance)
            obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

        #
       #
       #



def delete_project_details(request):
    if request.method=='POST':
        project_id = request.POST.get('project_id')
        obj = Projects.objects.get(id=project_id)
        obj.delete()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def get_project_details(request):
    if request.method=="GET":
        clients=Client.objects.all()
        employees=CustomUser.objects.all()
        camp = Company.objects.all()
        all_projects_with_employees = Projects.objects.all().prefetch_related('Assigned_employees')


        context={
            'all_projects_with_employees': all_projects_with_employees,
            'clients': clients,
            'employees': employees,
            'camp': camp,
        }

        return render(request,'hr/project/add_project.html',context)


def get_tasks(request):
    if request.method=="GET":
        clients = Client.objects.all()
        employees = CustomUser.objects.all()
        camp = Company.objects.all()
        projects=Projects.objects.all()


        all_tasks_with_employees = Tasks.objects.all()


        context={
            'all_tasks_with_employees': all_tasks_with_employees,
            'clients': clients,
            'employees': employees,
            'camp': camp,
            'projects':projects

        }

        return render(request,'hr/project/tasks.html',context)




def add_taks(request):
    if request.method=="POST":
        task_title = request.POST.get('task_title')
        client = request.POST.get('client')
        projects = request.POST.get('projects')
        Priority = request.POST.get('Priority')
        company = request.POST.get('company')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        employees = request.POST['employees']

        description = request.POST.get('description')
        progress = request.POST.get('progress')
        print(task_title,client,projects,Priority,start_date,end_date,employees,description,progress,company)
        obj = Tasks.objects.create(title=task_title, client_id=client, company_id=company,project_id=projects,
                                   start_date=start_date,end_date=end_date,description=description, priority=Priority, Progress=progress+"completed")

        for user_id in employees.split(","):
            user_instance = CustomUser.objects.get(pk=user_id)
            obj.employees.add(user_instance)
            obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)






def update_tasks(request):
    if request.method=="POST":
        task_title = request.POST.get('task_title_upd')
        client = request.POST.get('client_upd')
        projects = request.POST.get('projects_upd')
        Priority = request.POST.get('Priority_upd')
        company = request.POST.get('company_upd')
        start_date_upd = request.POST.get('start_date_upd')
        end_date = request.POST.get('end_date_upd')
        employees = request.POST['employees_upd']

        description = request.POST.get('description_upd')
        progress = request.POST.get('progress_upd')
        task_id = request.POST.get('task_id')
        print(task_id,task_title,client,projects,Priority,end_date,employees,description,progress,company)
        obj = Tasks.objects.get(id=task_id)
        obj.title=task_title
        obj.client_id=client
        obj.end_date=end_date
        obj.start_date=start_date_upd
        obj.description=description
        obj.company_id=company
        obj.priority=Priority
        obj.project_id=projects
        obj.Progress=progress+"completed"


        for user_id in employees.split(","):
            user_instance = CustomUser.objects.get(pk=user_id)
            obj.employees.add(user_instance)
            obj.save()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def get_taks_record_wise(request,id):
    if request.method=="GET":
        obj = Tasks.objects.get(id=id)
        print(obj.id)
        employees_list = obj.employees.all()


        l1 = [user.id for user in employees_list]
        data={
        'task_title_upd':obj.title,
        'client_upd':obj.client_id,
        'end_date_upd':obj.end_date,
        'start_date_upd':obj.start_date,
        'description_upd':obj.description,
        'company_upd':obj.company_id,
        'Priority_upd':obj.priority,
        'projects_upd':obj.project_id,
        'progress_upd':obj.Progress,
        'employee_upd':l1
        }
        print(data)
        return JsonResponse(data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)









def delete_tasks(request):
    if request.method=="POST":
        task_id = request.POST.get('task_id')

        print(task_id)
        obj = Tasks.objects.get(id=task_id)
        obj.delete()
        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)







def Add_company_policy_data(request):
    if request.method == 'POST':
        title_company_policy = request.POST.get('title_company_policy')
        description_company_policy = request.POST.get('description_company_policy')
        company_company_policy = request.POST.get('company_company_policy')

        print("Title:", title_company_policy)
        print("Description:", description_company_policy)
        print("Company:", company_company_policy)


        obj = Company_Policy.objects.create(
                name_id=company_company_policy,
                title=title_company_policy,
                description=description_company_policy
            )

        response_data = {'message': "Company Policy created successfully"}


        return JsonResponse(response_data)
    else:
        data15 = Company_Policy.objects.all()
        data22 = Company.objects.all()
        return render(request,'hr/company/add_company_policy.html',{'data15':data15,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)








def update_company_policy_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        company_policy_id=request.POST.get('company_policy_id')

        title_company_policy_upd = request.POST.get('title_company_policy_upd')
        description_company_policy_upd = request.POST.get('description_company_policy_upd')
        company_company_policy_upd = request.POST.get('company_company_policy_upd')



        print(company_policy_id,data_id,title_company_policy_upd,description_company_policy_upd,company_company_policy_upd)

        obj = Company_Policy.objects.get(id=company_policy_id)




        obj.title=title_company_policy_upd
        obj.description=description_company_policy_upd
        obj.name_id=company_company_policy_upd


        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def get_company_policy_data(request,id):


    if request.method == 'GET':
        obj = Company_Policy.objects.get(id=id)

        data= {
            'title_company_policy_upd':obj.title,
            'description_company_policy_upd':obj.description,
            'company_company_policy_upd':obj.name_id,



           }
        return JsonResponse(data)




def delete_company_policy_data(request):
    if request.method == 'POST':

        company_policy_id = request.POST.get('company_policy_id')
        #data_id = request.POST.get('data_id')

        #company = Company.objects.get(name__iexact=company_company_policy_upd)
        obj = Company_Policy.objects.get(id=company_policy_id)

        if obj:

            obj.delete()

            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)


def Add_announcements_data(request):
    if request.method == 'POST':

        title_announcements = request.POST.get('title_announcements')
        summary = request.POST.get('summary')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        description_announcements = request.POST.get('description_announcements')
        company_announcements = request.POST.get('company_announcements')
        department_announcements = request.POST.get('department_announcements')

        print("Title:", title_announcements)
        print("Summary:", summary)
        print("Start Date:", start_date)
        print("End Date:", end_date)
        print("Description:", description_announcements)
        print("company:", company_announcements)
        print("Department:", department_announcements)






        obj = Announcements.objects.create(


                title=title_announcements,
                summary=summary,
                start_date=start_date,
                end_date=end_date,
                description=description_announcements,
                name_id=company_announcements,
                department_id=department_announcements
            )

        response_data = {'message': "Designation created successfully"}


        return JsonResponse(response_data)
    else:
        data16 = Announcements.objects.all()
        data22 = Company.objects.all()
        data19 = Department.objects.all()
        return render(request, 'hr/company/add_announcements.html', {'data16': data16,'data19':data19,'data22':data22})

        return JsonResponse({'error': 'Invalid form data.'}, status=400)










def update_annoucements_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        announcements_id=request.POST.get('announcements_id')

        title_announcements_upd = request.POST.get('title_announcements_upd')
        summary_upd = request.POST.get('summary_upd')
        start_date_upd = request.POST.get('start_date_upd')
        end_date_upd = request.POST.get('end_date_upd')
        description_announcements_upd = request.POST.get('description_announcements_upd')
        company_announcements_upd = request.POST.get('company_announcements_upd')
        department_announcements_upd = request.POST.get('department_announcements_upd')

        print(announcements_id,data_id,title_announcements_upd,summary_upd,start_date_upd,end_date_upd,description_announcements_upd,company_announcements_upd,department_announcements_upd)


        obj = Announcements.objects.get(id=announcements_id)





        obj.title=title_announcements_upd
        obj.summary=summary_upd
        obj.start_date=start_date_upd
        obj.end_date = end_date_upd
        obj.description = description_announcements_upd
        obj.name_id = company_announcements_upd
        obj.department_id = department_announcements_upd
        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def get_announcements_data(request, id):
    if request.method == 'GET':
        obj = Announcements.objects.get(id=id)

        data = {
            'title_announcements_upd': obj.title,
            'summary_upd': obj.summary,
            'start_date_upd': obj.start_date,
            'end_date_upd': obj.end_date,
            'description_announcements_upd': obj.description,
            'company_announcements_upd': obj.name_id,
            'department_announcements_upd': obj.department_id,


        }
        return JsonResponse(data)


def delete_announcements_data(request):
    if request.method == 'POST':

        announcements_id = request.POST.get('announcements_id')
        #data_id = request.POST.get('data_id')

        #company = Company.objects.get(name__iexact=company_company_policy_upd)
        obj = Announcements.objects.get(id=announcements_id)

        if obj:

            obj.delete()

            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)







def Add_designation_data(request):
    if request.method == 'POST':



        designation_designation = request.POST.get('designation_designation')
        company_designation = request.POST.get('company_designation')
        department_dep = request.POST.get('department_dep')


        print("Designation:", designation_designation)
        print("Company:", company_designation)
        print("Department:", department_dep)




        obj = Designation.objects.create(

                designation=designation_designation,
                name_id=company_designation,
                department_id=department_dep
            )

        response_data = {'message': "Designation created successfully"}
        return JsonResponse(response_data)
    else:
        data17 = Designation.objects.all()
        data19 = Department.objects.all()
        data22 = Company.objects.all()

        return render(request, 'hr/company/add_designation.html', {'data17': data17,'data19':data19,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)


def update_designation_data(request):
    if request.method == 'POST':
        data_id = request.POST.get('data_id')
        designation_id = request.POST.get('designation_id')

        designation_designation_upd = request.POST.get('designation_designation_upd')
        company_designation_upd = request.POST.get('company_designation_upd')
        department_dep_upd = request.POST.get('department_dep_upd')

        print(designation_id,data_id, designation_designation_upd,company_designation_upd,department_dep_upd)


        obj = Designation.objects.get(id=designation_id)

        obj.designation = designation_designation_upd
        obj.name_id = company_designation_upd
        obj.department_id = department_dep_upd

        obj.save()

        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)




def get_designation_data(request, id):
    if request.method == 'GET':
        obj = Designation.objects.get(id=id)

        data = {
            'designation_designation_upd': obj.designation,
            'company_designation_upd': obj.name_id,
            'department_dep_upd': obj.department_id,



        }
        return JsonResponse(data)

def delete_designation_data(request):
    if request.method == 'POST':

        designation_id = request.POST.get('designation_id')
        #data_id = request.POST.get('data_id')

        #company = Company.objects.get(name__iexact=company_company_policy_upd)
        obj = Designation.objects.get(id=designation_id)

        if obj:

            obj.delete()

            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)





def Add_location_data(request):
    if request.method == 'POST':
        location_location = request.POST.get('location_location')
        location_head_location = request.POST.get('location_head_location')
        address_1_location = request.POST.get('address_1_location')
        address_2_location = request.POST.get('address_2_location')
        city_location = request.POST.get('city_location')
        state_location = request.POST.get('state_location')
        country_location = request.POST.get('country_location')
        zip_location = request.POST.get('zip_location')

        print("Location:", location_location)
        print("Location Head:", location_head_location)
        print("Address1:", address_1_location)
        print("Address2:", address_2_location)
        print("City:", city_location)
        print("State:", state_location)
        print("Country:", country_location)
        print("ZIP:", zip_location)




        obj = Location.objects.create(location_head_id=location_head_location,location=location_location,address_line_1=address_1_location,address_line_2=address_2_location,city=city_location,state=state_location,country=country_location,zip=zip_location)

        obj.save()

        response_data = {'message': "Company Policy created successfully"}
        return JsonResponse(response_data)

    else:
        data1 = CustomUser.objects.all()
        data18 = Location.objects.all()
        return render(request, 'hr/company/add_location.html', {'data18': data18,'data1':data1})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)









def update_location_data(request):
    if request.method == 'POST':
        data_id = request.POST.get('data_id')
        location_id = request.POST.get('location_id')

        location_location_upd = request.POST.get('location_location_upd')
        location_head_location_upd = request.POST.get('location_head_location_upd')
        address_1_location_upd = request.POST.get('address_1_location_upd')
        address_2_location_upd = request.POST.get('address_2_location_upd')
        city_location_upd = request.POST.get('city_location_upd')
        state_location_upd = request.POST.get('state_location_upd')
        country_location_upd = request.POST.get('country_location_upd')
        zip_location_upd = request.POST.get('zip_location_upd')

        print(location_id, data_id, location_location_upd, location_head_location_upd, address_1_location_upd, address_2_location_upd, city_location_upd, state_location_upd, country_location_upd, zip_location_upd)

        obj = Location.objects.get(id=location_id)

        obj.location = location_location_upd
        obj.address_line_1 = address_1_location_upd
        obj.address_line_2 = address_2_location_upd
        obj.city = city_location_upd
        obj.state = state_location_upd
        obj.country = country_location_upd
        obj.zip = zip_location_upd


        obj.location_head_id = location_head_location_upd

        obj.save()

        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def get_location_data(request, id):
    if request.method == 'GET':
        obj = Location.objects.get(id=id)

        data = {
            'location_location_upd': obj.location,
            'address_1_location_upd': obj.address_line_1,
            'address_2_location_upd': obj.address_line_2,
            'city_location_upd': obj.city,
            'state_location_upd': obj.state,
            'country_location_upd': obj.country,
            'zip_location_upd': obj.zip,
            'location_head_location_upd': obj.location_head_id,

        }
        return JsonResponse(data)


def delete_location_data(request):
    if request.method == 'POST':

        location_id = request.POST.get('location_id')
        #data_id = request.POST.get('data_id')

        #company = Company.objects.get(name__iexact=company_company_policy_upd)
        obj = Location.objects.get(id=location_id)

        if obj:

            obj.delete()

            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)





def Add_department_data(request):
    if request.method== 'GET':
        data19 = Department.objects.all()
        data22 = Company.objects.all()
        return render(request, 'hr/company/add_department.html', {'data19': data19,'data22':data22})
    if request.method == 'POST':
        department_department = request.POST.get('department_department')
        company_department = request.POST.get('company_department')
        department_head_department = request.POST.get('department_head_department')



        print("Department",department_department)
        print("Company", company_department)

        obj = Department.objects.create(
                name_id=company_department,
                department=department_department,
                department_head=department_head_department
            )

        obj.save()

        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


            #return JsonResponse({'error': 'Invalid form data.'}, status=400)



def update_department_data(request):
    if request.method == 'POST':
        data_id = request.POST.get('data_id')
        department_id = request.POST.get('department_id')

        department_department_upd = request.POST.get('department_department_upd')
        company_department_upd = request.POST.get('company_department_upd')
        department_head_department_upd = request.POST.get('department_head_department_upd')

        print(department_id, data_id, department_department_upd, company_department_upd, department_head_department_upd)

        obj = Department.objects.get(id=department_id)




        obj.department = department_department_upd
        obj.name_id = company_department_upd
        obj.department_head = department_head_department_upd

        obj.save()

        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def get_department_data(request, id):
    if request.method == 'GET':
        obj = Department.objects.get(id=id)

        data = {
            'department_department_upd': obj.department,
            'company_department_upd': obj.name_id,
            'department_head_department_upd': obj.department_head,


        }
        return JsonResponse(data)



def delete_department_data(request):
    if request.method == 'POST':

        department_id = request.POST.get('department_id')
        #data_id = request.POST.get('data_id')

        #company = Company.objects.get(name__iexact=company_company_policy_upd)
        obj = Department.objects.get(id=department_id)

        if obj:

            obj.delete()

            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)






def Add_company_data(request):

    if request.method == 'POST':


        company_company = request.POST.get('company_company')
        trading_name = request.POST.get('trading_name')
        registration_number = request.POST.get('registration_number')
        phone = request.POST.get('phone')
        email_company = request.POST.get('email_company')

        print(company_company,trading_name,registration_number,phone,email_company)

        obj=Company.objects.create(name=company_company,trading_name=trading_name,registration_number=registration_number,phone=phone,email=email_company)

        obj.save()

        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        data20 = Company.objects.all()
        return render(request, 'hr/company/add_company.html',{'data20':data20})
        return JsonResponse({'error': 'Invalid form data.'}, status=400)









def update_company_data(request):
    if request.method == 'POST':
        data_id=request.POST.get('data_id')
        company_id=request.POST.get('company_id')

        company_company_upd = request.POST.get('company_company_upd')
        trading_name_upd = request.POST.get('trading_name_upd')
        registration_number_upd = request.POST.get('registration_number_upd')
        phone_upd = request.POST.get('phone_upd')
        email_company_upd = request.POST.get('email_company_upd')

        print(company_id,data_id,company_company_upd,trading_name_upd,registration_number_upd,phone_upd,email_company_upd)










        obj = Company.objects.get(id=company_id)




        obj.name=company_company_upd
        obj.trading_name=trading_name_upd
        obj.registration_number=registration_number_upd
        obj.phone = phone_upd
        obj.email = email_company_upd



        obj.save()


        response_data = {'first_name': "workingfine"}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)




def get_company_data(request, id):
    if request.method == 'GET':
        obj = Company.objects.get(id=id)

        data = {
            'company_company_upd': obj.name,
            'trading_name_upd': obj.trading_name,
            'registration_number_upd': obj.registration_number,
            'phone_upd': obj.phone,
            'email_company_upd': obj.email,


        }
        return JsonResponse(data)






def delete_company_data(request):
    if request.method == 'POST':

        company_id = request.POST.get('company_id')
        #data_id = request.POST.get('data_id')

        #company = Company.objects.get(name__iexact=company_company_policy_upd)
        obj = Company.objects.get(id=company_id)

        if obj:

            obj.delete()

            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)





def Add_promotions_data(request):
    if request.method == 'POST':



        company_promotions = request.POST.get('company_promotions')
        employee_promotions = request.POST.get('employee_promotions')
        title_promotions = request.POST.get('title_promotions')
        promotion_date = request.POST.get('promotion_date')
        description_promotions = request.POST.get('description_promotions')


        print("Company:", company_promotions)
        print("Employee:", employee_promotions)
        print("Title:", title_promotions)
        print("Date:", promotion_date)
        print("Description:", description_promotions)


        obj = Promotions.objects.create(title=title_promotions,
                promotion_date=promotion_date,
                description=description_promotions,
                company_id=company_promotions,
                employee_id=employee_promotions
            )



        response_data = {'message': "Promotions created successfully"}


        return JsonResponse(response_data)
    else:
        data1 = CustomUser.objects.all()
        data21 = Promotions.objects.all()
        data22 = Company.objects.all()
        return render(request, 'hr/corehr/add_promotions.html', {'data21': data21,'data1':data1,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)





def update_promotions_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        promotions_id = request.POST.get('promotions_id')

        company_promotions_upd = request.POST.get('company_promotions_upd')
        employee_promotions_upd = request.POST.get('employee_promotions_upd')
        title_promotions_upd = request.POST.get('title_promotions_upd')
        promotion_date_upd = request.POST.get('promotion_date_upd')
        description_promotions_upd = request.POST.get('description_promotions_upd')


        print(promotions_id,company_promotions_upd, employee_promotions_upd, title_promotions_upd,promotion_date_upd,description_promotions_upd)


        obj = Promotions.objects.get(id=promotions_id)

        obj.title = title_promotions_upd
        obj.promotion_date = promotion_date_upd
        obj.description = description_promotions_upd
        obj.company_id = company_promotions_upd
        obj.employee_id = employee_promotions_upd

        obj.save()

        response_data = {'message': "Promotions record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)






def get_promotions_data(request, id):
    if request.method == 'GET':
        obj = Promotions.objects.get(id=id)

        data = {
            'company_promotions_upd': obj.company_id,
            'title_promotions_upd': obj.title,
            'promotion_date_upd': obj.promotion_date,
            'description_promotions_upd': obj.description,
            'employee_promotions_upd': obj.employee_id,



        }
        return JsonResponse(data)

def delete_promotions_data(request):
    if request.method == 'POST':

        promotions_id = request.POST.get('promotions_id')
       # data_id = request.POST.get('data_id')
        print(promotions_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Promotions.objects.get(id=promotions_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)








def Add_awards_data(request):
    if request.method == 'POST':



        company_awards = request.POST.get('company_awards')
        department_awards = request.POST.get('department_awards')
        employee_awards = request.POST.get('employee_awards')
        award_type_awards = request.POST.get('award_type_awards')
        gift_awards = request.POST.get('gift_awards')
        cash_awards = request.POST.get('cash_awards')
        award_information = request.POST.get('award_information')
        award_date = request.POST.get('award_date')


        print("Company:", company_awards)
        print("Department:", department_awards)
        print("Employee:", employee_awards)
        print("Award Type:", award_type_awards)
        print("Gift:", gift_awards)
        print("Cash:", cash_awards)
        print("Information:", award_information)
        print("Date:", award_date)


        obj = Awards.objects.create(
                award_type=award_type_awards,
                gift=gift_awards,
                cash=cash_awards,
                awards_information=award_information,
                award_date=award_date,
                company_id=company_awards,
                department_id=department_awards,
                employee_id=employee_awards
            )



        response_data = {'message': "Awards created successfully"}


        return JsonResponse(response_data)
    else:
        data1 = CustomUser.objects.all()
        data23 = Awards.objects.all()
        data22 = Company.objects.all()
        data19 = Department.objects.all()
        return render(request, 'hr/corehr/add_awards.html', {'data23': data23,'data1':data1,'data22':data22,'data19':data19})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)





def update_awards_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        awards_id = request.POST.get('awards_id')

        company_awards_upd = request.POST.get('company_awards_upd')
        department_awards_upd = request.POST.get('department_awards_upd')
        employee_awards_upd = request.POST.get('employee_awards_upd')
        award_type_awards_upd = request.POST.get('award_type_awards_upd')
        gift_awards_upd = request.POST.get('gift_awards_upd')
        cash_awards_upd = request.POST.get('cash_awards_upd')
        award_information_upd = request.POST.get('award_information_upd')
        award_date_upd = request.POST.get('award_date_upd')


        print(awards_id,company_awards_upd, department_awards_upd, employee_awards_upd,award_type_awards_upd,gift_awards_upd,cash_awards_upd,award_information_upd,award_date_upd)


        obj = Awards.objects.get(id=awards_id)

        obj.award_type = award_type_awards_upd
        obj.gift = gift_awards_upd
        obj.cash = cash_awards_upd
        obj.awards_information = award_information_upd
        obj.award_date = award_date_upd
        obj.department_id = department_awards_upd
        obj.company_id = company_awards_upd
        obj.employee_id = employee_awards_upd

        obj.save()

        response_data = {'message': "Awards record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def get_awards_data(request, id):
    if request.method == 'GET':
        obj = Awards.objects.get(id=id)

        data = {
            'company_awards_upd': obj.company_id,
            'department_awards_upd': obj.department_id,
            'employee_awards_upd': obj.employee_id,
            'award_type_awards_upd': obj.award_type,
            'gift_awards_upd': obj.gift,
            'cash_awards_upd': obj.cash,
            'award_information_upd': obj.awards_information,
            'award_date_upd': obj.award_date,


        }
        return JsonResponse(data)



def delete_awards_data(request):
    if request.method == 'POST':

        awards_id = request.POST.get('awards_id')
       # data_id = request.POST.get('data_id')
        print(awards_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Awards.objects.get(id=awards_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)



def Add_travel_data(request):
    if request.method == 'POST':



        company_travel = request.POST.get('company_travel')
        employee_travel = request.POST.get('employee_travel')
        arrangement_type = request.POST.get('arrangement_type')
        purpose_of_visit = request.POST.get('purpose_of_visit')
        place_of_visit = request.POST.get('place_of_visit')
        description_travel = request.POST.get('description_travel')
        start_date_travel = request.POST.get('start_date_travel')
        end_date_travel = request.POST.get('end_date_travel')
        expected_budget = request.POST.get('expected_budget')
        actual_budget = request.POST.get('actual_budget')
        travel_mode = request.POST.get('travel_mode')
        status = request.POST.get('status')

        print("Company:", company_travel)
        print("Employee:", employee_travel)
        print("Arrangement:", arrangement_type)
        print("Purpose of Visit:", purpose_of_visit)
        print("Place of Visit:", place_of_visit)
        print("Description:", description_travel)
        print("Start Date:", start_date_travel)
        print("End Date:", end_date_travel)
        print("Expected Budget:", expected_budget)
        print("Actual Budget:", actual_budget)
        print("Travel Mode:", travel_mode)
        print("Status:", status)

        obj = Travel.objects.create(
                arrangement_type=arrangement_type,
                purpose_of_visit=purpose_of_visit,
                place_of_visit=place_of_visit,
                description=description_travel,
                start_date=start_date_travel,
                end_date=end_date_travel,
                expected_budget=expected_budget,
                actual_budget=actual_budget,
                travel_mode=travel_mode,
                status=status,
                company_id=company_travel,
                employee_id=employee_travel
            )



        response_data = {'message': "Travel created successfully"}


        return JsonResponse(response_data)
    else:
        data1 = CustomUser.objects.all()
        data24 = Travel.objects.all()
        data22 = Company.objects.all()

        return render(request, 'hr/corehr/add_travel.html', {'data24': data24,'data1':data1,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)




def update_travel_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        travel_id = request.POST.get('travel_id')

        company_travel_upd = request.POST.get('company_travel_upd')
        employee_travel_upd = request.POST.get('employee_travel_upd')
        arrangement_type_upd = request.POST.get('arrangement_type_upd')
        purpose_of_visit_upd = request.POST.get('purpose_of_visit_upd')
        place_of_visit_upd = request.POST.get('place_of_visit_upd')
        description_travel_upd = request.POST.get('description_travel_upd')
        start_date_travel_upd = request.POST.get('start_date_travel_upd')
        end_date_travel_upd = request.POST.get('end_date_travel_upd')
        expected_budget_upd = request.POST.get('expected_budget_upd')
        actual_budget_upd = request.POST.get('actual_budget_upd')
        travel_mode_upd = request.POST.get('travel_mode_upd')
        status_upd = request.POST.get('status_upd')

        print(travel_id,company_travel_upd, employee_travel_upd, arrangement_type_upd,purpose_of_visit_upd,place_of_visit_upd,description_travel_upd,start_date_travel_upd,end_date_travel_upd, expected_budget_upd,actual_budget_upd,travel_mode_upd,status_upd)


        obj = Travel.objects.get(id=travel_id)

        obj.arrangement_type = arrangement_type_upd
        obj.purpose_of_visit = purpose_of_visit_upd
        obj.place_of_visit = place_of_visit_upd
        obj.description = description_travel_upd
        obj.start_date = start_date_travel_upd
        obj.end_date = end_date_travel_upd
        obj.expected_budget = expected_budget_upd
        obj.actual_budget = actual_budget_upd
        obj.travel_mode = travel_mode_upd
        obj.status = status_upd
        obj.company_id = company_travel_upd
        obj.employee_id = employee_travel_upd

        obj.save()

        response_data = {'message': "Travel record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def get_travel_data(request, id):
    if request.method == 'GET':
        obj = Travel.objects.get(id=id)

        data = {
            'company_travel_upd': obj.company_id,
            'employee_travel_upd': obj.employee_id,
            'arrangement_type_upd': obj.arrangement_type,
            'purpose_of_visit_upd': obj.purpose_of_visit,
            'place_of_visit_upd': obj.place_of_visit,
            'description_travel_upd': obj.description,
            'start_date_travel_upd': obj.start_date,
            'end_date_travel_upd': obj.end_date,
            'expected_budget_upd': obj.expected_budget,
            'actual_budget_upd': obj.actual_budget,
            'travel_mode_upd': obj.travel_mode,
            'status_upd': obj.status



        }
        return JsonResponse(data)




def delete_travel_data(request):
    if request.method == 'POST':

        travel_id = request.POST.get('travel_id')
       # data_id = request.POST.get('data_id')
        print(travel_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Travel.objects.get(id=travel_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)






def Add_transfer_data(request):
    if request.method == 'POST':



        company_transfer = request.POST.get('company_transfer')
        employee_transfer = request.POST.get('employee_transfer')
        from_department = request.POST.get('from_department')
        to_department = request.POST.get('to_department')
        transfer_date = request.POST.get('transfer_date')
        description_transfer = request.POST.get('description_transfer')

        print("Company:", company_transfer)
        print("Employee:", employee_transfer)
        print("From Department:", from_department)
        print("To Department:", to_department)
        print("Transfer Date:", transfer_date)
        print("Description:", description_transfer)



        obj = Transfer.objects.create(
                from_department=from_department,
                to_department=to_department,
                transfer_date=transfer_date,
                description=description_transfer,
                company_id=company_transfer,
                employee_id=employee_transfer
            )



        response_data = {'message': "Transfer created successfully"}


        return JsonResponse(response_data)
    else:
        data1 = CustomUser.objects.all()
        data25 = Transfer.objects.all()
        data22 = Company.objects.all()

        return render(request, 'hr/corehr/add_transfer.html', {'data25': data25,'data1':data1,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)







def update_transfer_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        transfer_id = request.POST.get('transfer_id')

        company_transfer_upd = request.POST.get('company_transfer_upd')
        employee_transfer_upd = request.POST.get('employee_transfer_upd')
        from_department_upd = request.POST.get('from_department_upd')
        to_department_upd = request.POST.get('to_department_upd')
        transfer_date_upd = request.POST.get('transfer_date_upd')
        description_transfer_upd = request.POST.get('description_transfer_upd')

        print(transfer_id,company_transfer_upd, employee_transfer_upd, from_department_upd,
              to_department_upd, transfer_date_upd,description_transfer_upd)


        obj = Transfer.objects.get(id=transfer_id)

        obj.from_department = from_department_upd
        obj.to_department = to_department_upd
        obj.transfer_date = transfer_date_upd
        obj.description = description_transfer_upd
        obj.company_id = company_transfer_upd
        obj.employee_id = employee_transfer_upd

        obj.save()

        response_data = {'message': "Transfer record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def get_transfer_data(request, id):
    if request.method == 'GET':
        obj = Transfer.objects.get(id=id)

        data = {
            'from_department_upd': obj.from_department,
            'to_department_upd': obj.to_department,
            'transfer_date_upd': obj.transfer_date,
            'description_transfer_upd': obj.description,
            'company_transfer_upd': obj.company_id,
            'employee_transfer_upd': obj.employee_id



        }
        return JsonResponse(data)



def delete_transfer_data(request):
    if request.method == 'POST':

        transfer_id = request.POST.get('transfer_id')
       # data_id = request.POST.get('data_id')
        print(transfer_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Transfer.objects.get(id=transfer_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)







def Add_resignation_data(request):
    if request.method == 'POST':



        company_resignation = request.POST.get('company_resignation')
        department_resignation = request.POST.get('department_resignation')
        employee_resignation = request.POST.get('employee_resignation')
        notice_date = request.POST.get('notice_date')
        resignation_date = request.POST.get('resignation_date')
        description_resignation = request.POST.get('description_resignation')



        print("Company:", company_resignation)
        print("Department:", department_resignation)
        print("Employee:", employee_resignation)
        print("Notice Date:", notice_date)
        print("Resignation Date:", resignation_date)
        print("Description:", description_resignation)


        obj = Resignation.objects.create(
                notice_date=notice_date,
                resignation_date=resignation_date,
                description=description_resignation,
                company_id=company_resignation,
                department_id=department_resignation,
                employee_id=employee_resignation
            )



        response_data = {'message': "Resignation created successfully"}


        return JsonResponse(response_data)
    else:
        data1 = CustomUser.objects.all()
        data26 = Resignation.objects.all()
        data22 = Company.objects.all()
        data19 = Department.objects.all()
        return render(request, 'hr/corehr/add_registration.html', {'data26': data26,'data1':data1,'data22':data22,'data19':data19})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)






def update_resignation_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        resignation_id = request.POST.get('resignation_id')
        employee_id_upd = request.POST.get('employee_resignation_upd')

        company_resignation_upd = request.POST.get('company_resignation_upd')
        department_resignation_upd = request.POST.get('department_resignation_upd')
        employee_resignation_upd = request.POST.get('employee_resignation_upd')
        notice_date_upd = request.POST.get('notice_date_upd')
        resignation_date_upd = request.POST.get('resignation_date_upd')
        description_resignation_upd = request.POST.get('description_resignation_upd')

        print(resignation_id,company_resignation_upd, department_resignation_upd, employee_resignation_upd,
              notice_date_upd, resignation_date_upd,description_resignation_upd)


        obj = Resignation.objects.get(id=resignation_id)

        obj.notice_date = notice_date_upd
        obj.resignation_date = resignation_date_upd
        obj.description = description_resignation_upd
        obj.company_id = company_resignation_upd
        obj.department_id = department_resignation_upd
        obj.employee_id = employee_resignation_upd  # Use the correct employee ID field

        obj.save()

        response_data = {'message': "Resignation record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def get_resignation_data(request, id):
    if request.method == 'GET':
        obj = Resignation.objects.get(id=id)

        data = {
            'notice_date_upd': obj.notice_date,
            'resignation_date_upd': obj.resignation_date,
            'description_resignation_upd': obj.description,
            'company_resignation_upd': obj.company_id,
            'department_resignation_upd': obj.department_id,
            'employee_resignation_upd': obj.employee_id



        }
        return JsonResponse(data)






def delete_resignation_data(request):
    if request.method == 'POST':

        resignation_id = request.POST.get('resignation_id')
       # data_id = request.POST.get('data_id')
        print(resignation_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Resignation.objects.get(id=resignation_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)





def Add_complains_data(request):
    if request.method == 'POST':



        company_complains = request.POST.get('company_complains')
        employee_complains = request.POST.get('employee_complains')
        complain_title = request.POST.get('complain_title')
        description_complain = request.POST.get('description_complain')
        complain_date = request.POST.get('complain_date')



        print("Company:", company_complains)
        print("Employee:", employee_complains)
        print("Title:", complain_title)
        print("Complain Date:", complain_date)
        print("Description:", description_complain)


        obj = Complains.objects.create(
                complain_title=complain_title,
                description=description_complain,
                complain_date=complain_date,
                company_id=company_complains,
                employee_id=employee_complains
            )



        response_data = {'message': "Complains created successfully"}


        return JsonResponse(response_data)
    else:
        data1 = CustomUser.objects.all()
        data27 = Complains.objects.all()
        data22 = Company.objects.all()
        return render(request, 'hr/corehr/add_complains.html', {'data27': data27,'data1':data1,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)




def update_complains_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        complains_id = request.POST.get('complains_id')

        company_complains_upd = request.POST.get('company_complains_upd')
        employee_complains_upd = request.POST.get('employee_complains_upd')
        complain_title_upd = request.POST.get('complain_title_upd')
        description_complain_upd = request.POST.get('description_complain_upd')
        complain_date_upd = request.POST.get('complain_date_upd')

        print(complains_id,company_complains_upd, employee_complains_upd, complain_title_upd,
              description_complain_upd, complain_date_upd)


        obj = Complains.objects.get(id=complains_id)

        obj.complain_title = complain_title_upd
        obj.description = description_complain_upd
        obj.complain_date = complain_date_upd
        obj.company_id = company_complains_upd
        obj.employee_id = employee_complains_upd

        obj.save()

        response_data = {'message': "Complains record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)




def get_complains_data(request, id):
    if request.method == 'GET':
        obj = Complains.objects.get(id=id)

        data = {
            'complain_title_upd': obj.complain_title,
            'description_complain_upd': obj.description,
            'complain_date_upd': obj.complain_date,
            'company_complains_upd': obj.company_id,
            'employee_complains_upd': obj.employee_id,



        }
        return JsonResponse(data)




def delete_complains_data(request):
    if request.method == 'POST':

        complains_id = request.POST.get('complains_id')
       # data_id = request.POST.get('data_id')
        print(complains_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Complains.objects.get(id=complains_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)





def Add_warnings_data(request):
    if request.method == 'POST':



        company_warnings = request.POST.get('company_warnings')
        employee_warnings = request.POST.get('employee_warnings')
        warning_type = request.POST.get('warning_type')
        subject_warnings = request.POST.get('subject_warnings')
        description_warnings = request.POST.get('description_warnings')
        warning_date = request.POST.get('warning_date')
        status_warnings = request.POST.get('status_warnings')



        print("Company:", company_warnings)
        print("Employee:", employee_warnings)
        print("Warning Type:", warning_type)
        print("Subject:", subject_warnings)
        print("Description:", description_warnings)
        print("Warning Date:", warning_date)
        print("Status:", status_warnings)


        obj = Warnings.objects.create(
                warning_type=warning_type,
                subject=subject_warnings,
                description=description_warnings,
                warning_date=warning_date,
                status=status_warnings,
                company_id=company_warnings,
                employee_id=employee_warnings
            )



        response_data = {'message': "Warning created successfully"}


        return JsonResponse(response_data)
    else:
        data1 = CustomUser.objects.all()
        data28 = Warnings.objects.all()
        data22 = Company.objects.all()
        return render(request, 'hr/corehr/add_warnings.html', {'data28': data28,'data1':data1,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)






def update_warnings_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        warnings_id = request.POST.get('warnings_id')

        company_warnings_upd = request.POST.get('company_warnings_upd')
        employee_warnings_upd = request.POST.get('employee_warnings_upd')
        warning_type_upd = request.POST.get('warning_type_upd')
        subject_warnings_upd = request.POST.get('subject_warnings_upd')
        description_warnings_upd = request.POST.get('description_warnings_upd')
        warning_date_upd = request.POST.get('warning_date_upd')
        status_warnings_upd = request.POST.get('status_warnings_upd')

        print(warnings_id,company_warnings_upd, employee_warnings_upd, warning_type_upd,
              subject_warnings_upd, description_warnings_upd, warning_date_upd,status_warnings_upd)


        obj = Warnings.objects.get(id=warnings_id)

        obj.warning_type = warning_type_upd
        obj.subject = subject_warnings_upd
        obj.description = description_warnings_upd
        obj.warning_date = warning_date_upd
        obj.status = status_warnings_upd
        obj.company_id = company_warnings_upd
        obj.employee_id = employee_warnings_upd

        obj.save()

        response_data = {'message': "Warning record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def get_warnings_data(request, id):
    if request.method == 'GET':
        obj = Warnings.objects.get(id=id)

        data = {
            'company_warnings_upd': obj.company_id,
            'employee_warnings_upd': obj.employee_id,
            'warning_type_upd': obj.warning_type,
            'subject_warnings_upd': obj.subject,
            'description_warnings_upd': obj.description,
            'warning_date_upd': obj.warning_date,
            'status_warnings_upd': obj.status,



        }
        return JsonResponse(data)



def delete_warnings_data(request):
    if request.method == 'POST':

        warnings_id = request.POST.get('warnings_id')
       # data_id = request.POST.get('data_id')
        print(warnings_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Warnings.objects.get(id=warnings_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)






def Add_terminations_data(request):
    if request.method == 'POST':



        company_terminations = request.POST.get('company_terminations')
        employee_terminations = request.POST.get('employee_terminations')
        termination_type = request.POST.get('termination_type')
        description_terminations = request.POST.get('description_terminations')
        termination_date = request.POST.get('termination_date')
        notice_date = request.POST.get('notice_date')




        print("Company:", company_terminations)
        print("Employee:", employee_terminations)
        print("Termination Type:", termination_type)
        print("Description:", description_terminations)
        print("Termination Date:", termination_date)
        print("Notice Date:", notice_date)


        obj = Terminations.objects.create(
                termination_type=termination_type,
                description=description_terminations,
                termination_date=termination_date,
                notice_date=notice_date,
                company_id=company_terminations,
                employee_id=employee_terminations
            )



        response_data = {'message': "Termination created successfully"}


        return JsonResponse(response_data)
    else:
        data1 = CustomUser.objects.all()
        data29 = Terminations.objects.all()
        data22 = Company.objects.all()
        return render(request, 'hr/corehr/add_terminations.html', {'data29': data29,'data1':data1,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)


def update_terminations_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        terminations_id = request.POST.get('terminations_id')

        company_terminations_upd = request.POST.get('company_terminations_upd')
        employee_terminations_upd = request.POST.get('employee_terminations_upd')
        termination_type_upd = request.POST.get('termination_type_upd')
        description_terminations_upd = request.POST.get('description_terminations_upd')
        termination_date_upd = request.POST.get('termination_date_upd')
        notice_date_upd = request.POST.get('notice_date_upd')

        print(terminations_id,company_terminations_upd, employee_terminations_upd, termination_type_upd,
              description_terminations_upd, termination_date_upd, notice_date_upd)


        obj = Terminations.objects.get(id=terminations_id)

        obj.termination_type = termination_type_upd
        obj.description = description_terminations_upd
        obj.termination_date = termination_date_upd
        obj.notice_date = notice_date_upd
        obj.company_id = company_terminations_upd
        obj.employee_id = employee_terminations_upd

        obj.save()

        response_data = {'message': "Termination record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def get_terminations_data(request, id):
    if request.method == 'GET':
        obj = Terminations.objects.get(id=id)

        data = {
            'termination_type_upd': obj.termination_type,
            'description_terminations_upd': obj.description,
            'termination_date_upd': obj.termination_date,
            'notice_date_upd': obj.notice_date,
            'company_terminations_upd': obj.company_id,
            'employee_terminations_upd': obj.employee_id



        }
        return JsonResponse(data)





def delete_terminations_data(request):
    if request.method == 'POST':

        terminations_id = request.POST.get('terminations_id')
       # data_id = request.POST.get('data_id')
        print(terminations_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Terminations.objects.get(id=terminations_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)










def Add_job_post_data(request):
    if request.method == 'POST':



        company_job_post = request.POST.get('company_job_post')
        job_title = request.POST.get('job_title')
        job_type = request.POST.get('job_type')
        job_category = request.POST.get('job_category')
        no_of_vacancy = request.POST.get('no_of_vacancy')
        date_of_closing = request.POST.get('date_of_closing')
        gender = request.POST.get('gender')
        experience = request.POST.get('experience')
        is_featured = request.POST.get('is_featured')
        status = request.POST.get('status')



        print(company_job_post,job_title,job_type,job_category,no_of_vacancy,date_of_closing,gender,experience,is_featured,status)




        obj = Job_Post.objects.create(
                job_title=job_title,
                job_type=job_type,
                job_category=job_category,
                no_of_vacancy=no_of_vacancy,
                date_of_closing=date_of_closing,
                gender=gender,
                minimum_experience=experience,
                is_featured=is_featured,
                status=status,
                company_id=company_job_post,

            )



        response_data = {'message': "Training List created successfully"}


        return JsonResponse(response_data)
    else:

        data22 = Company.objects.all()
        data37 = Job_Post.objects.all()
        return render(request, 'hr/recuritment/job_post.html', {'data37':data37,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)






def update_job_post_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        job_post_id = request.POST.get('job_post_id')

        company_job_post_upd = request.POST.get('company_job_post_upd')
        job_title_upd = request.POST.get('job_title_upd')
        job_type_upd = request.POST.get('job_type_upd')
        job_category_upd = request.POST.get('job_category_upd')
        no_of_vacancy_upd = request.POST.get('no_of_vacancy_upd')
        date_of_closing_upd = request.POST.get('date_of_closing_upd')
        gender_upd = request.POST.get('gender_upd')
        experience_upd = request.POST.get('experience_upd')
        is_featured_upd = request.POST.get('is_featured_upd')
        status_upd = request.POST.get('status_upd')

        print(job_post_id,company_job_post_upd, job_title_upd, job_type_upd,job_category_upd,no_of_vacancy_upd,date_of_closing_upd,gender_upd,experience_upd,is_featured_upd,status_upd)


        obj = Job_Post.objects.get(id=job_post_id)


        obj.job_title = job_title_upd
        obj.job_type = job_type_upd
        obj.job_category = job_category_upd
        obj.no_of_vacancy = no_of_vacancy_upd
        obj.date_of_closing = date_of_closing_upd
        obj.gender = gender_upd
        obj.minimum_experience = experience_upd
        obj.is_featured = is_featured_upd
        obj.status = status_upd
        obj.company_id = company_job_post_upd


        obj.save()

        response_data = {'message': "Training List record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def get_job_post_data(request, id):
    if request.method == 'GET':
        obj = Job_Post.objects.get(id=id)

        data = {
            'company_job_post_upd': obj.company_id,
            'job_title_upd': obj.job_title,
            'job_type_upd': obj.job_type,
            'job_category_upd': obj.job_category,
            'no_of_vacancy_upd': obj.no_of_vacancy,
            'date_of_closing_upd': obj.date_of_closing,
            'gender_upd': obj.gender,
            'experience_upd': obj.minimum_experience,
            'is_featured_upd': obj.is_featured,
            'status_upd': obj.status,

        }
        return JsonResponse(data)




def delete_job_post_data(request):
    if request.method == 'POST':

        job_post_id = request.POST.get('job_post_id')
       # data_id = request.POST.get('data_id')
        print(job_post_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Job_Post.objects.get(id=job_post_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)






def Add_job_candidate_data(request):
    if request.method == 'POST' and request.FILES.get('resume'):



        job_title = request.POST.get('job_title')
        candidate_name = request.POST.get('candidate_name')
        candidate_email = request.POST.get('candidate_email')
        resume = request.FILES['resume']
        status = request.POST.get('status')
        applied_date = request.POST.get('applied_date')




        print(job_title,candidate_name,resume,candidate_email,applied_date,status)




        obj = Job_Candidate.objects.create(
                candidate_name=candidate_name,
                candidate_email=candidate_email,
                resume=resume,
                status=status,
                apply_date=applied_date,
                job_title_id=job_title,

            )



        response_data = {'message': "Training List created successfully"}


        return JsonResponse(response_data)
    else:


        data37 = Job_Post.objects.all()
        data38 = Job_Candidate.objects.all()
        return render(request, 'hr/recuritment/job_candidate.html', {'data37':data37,'data38':data38})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)







def update_job_candidate_data(request):
    if request.method == 'POST'and request.FILES.get('resume_upd'):
        #data_id = request.POST.get('data_id')
        job_candidate_id = request.POST.get('job_candidate_id')

        job_title_upd = request.POST.get('job_title_upd')
        candidate_name_upd = request.POST.get('candidate_name_upd')
        candidate_email_upd = request.POST.get('candidate_email_upd')
        resume_upd = request.FILES['resume_upd']
        status_upd = request.POST.get('status_upd')
        applied_date_upd = request.POST.get('applied_date_upd')

        print(job_candidate_id,job_title_upd, candidate_name_upd, candidate_email_upd,resume_upd,status_upd,applied_date_upd)


        obj = Job_Candidate.objects.get(id=job_candidate_id)


        obj.candidate_name = candidate_name_upd
        obj.candidate_email = candidate_email_upd
        obj.resume = resume_upd
        obj.status = status_upd
        obj.apply_date = applied_date_upd
        obj.job_title_id = job_title_upd


        obj.save()

        response_data = {'message': "Training List record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)




def get_job_candidate_data(request, id):
    if request.method == 'GET':
        obj = Job_Candidate.objects.get(id=id)

        data = {
            'candidate_name_upd': obj.candidate_name,
            'job_title_upd': obj.job_title_id,
            'candidate_email_upd': obj.candidate_email,
            'status_upd': obj.status,
            'applied_date_upd': obj.apply_date,



        }
        print(data)
        return JsonResponse(data)





def delete_job_candidate_data(request):
    if request.method == 'POST':

        job_candidate_id = request.POST.get('job_candidate_id')
       # data_id = request.POST.get('data_id')
        print(job_candidate_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Job_Candidate.objects.get(id=job_candidate_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)




def Add_job_interview_data(request):
    if request.method == 'POST':



        job_title = request.POST.get('job_title')
        candidate_name = request.POST.get('candidate_name')
        interview_place = request.POST.get('interview_place')
        interview_date = request.POST.get('interview_date')
        interview_time = request.POST.get('interview_time')




        print(job_title,candidate_name,interview_place,interview_date,interview_time)




        obj = Job_Interview.objects.create(
                interview_place=interview_place,
                interview_date=interview_date,
                interview_time=interview_time,
                candidate_name_id=candidate_name,
                job_title_id=job_title

            )



        response_data = {'message': "Training List created successfully"}


        return JsonResponse(response_data)
    else:

        data37 = Job_Post.objects.all()
        data38 = Job_Candidate.objects.all()
        data39 = Job_Interview.objects.all()
        return render(request, 'hr/recuritment/job_interview.html', {'data37':data37,'data38':data38,'data39':data39})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)






def update_job_interview_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        job_interview_id = request.POST.get('job_interview_id')

        job_title_upd = request.POST.get('job_title_upd')
        candidate_name_upd = request.POST.get('candidate_name_upd')
        interview_place_upd = request.POST.get('interview_place_upd')
        interview_date_upd = request.POST.get('interview_date_upd')
        interview_time_upd = request.POST.get('interview_time_upd')

        print(job_interview_id,job_title_upd, candidate_name_upd, interview_place_upd,interview_date_upd,interview_time_upd)


        obj = Job_Interview.objects.get(id=job_interview_id)


        obj.interview_place = interview_place_upd
        obj.interview_date = interview_date_upd
        obj.interview_time = interview_time_upd
        obj.candidate_name_id = candidate_name_upd
        obj.job_title_id = job_title_upd


        obj.save()

        response_data = {'message': "Training List record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def get_job_interview_data(request, id):
    if request.method == 'GET':
        obj = Job_Interview.objects.get(id=id)

        data = {
            'job_title_upd': obj.job_title_id,
            'candidate_name_upd': obj.candidate_name_id,
            'interview_place_upd': obj.interview_place,
            'interview_date_upd': obj.interview_date,
            'interview_time_upd': obj.interview_time,



        }
        print(data)
        return JsonResponse(data)




def delete_job_interview_data(request):
    if request.method == 'POST':

        job_interview_id = request.POST.get('job_interview_id')
       # data_id = request.POST.get('data_id')
        print(job_interview_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Job_Interview.objects.get(id=job_interview_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)







def Add_trainer_data(request):
    if request.method == 'POST':



        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        company_trainer = request.POST.get('company_trainer')
        expertise = request.POST.get('expertise')
        experience = request.POST.get('experience')
        address = request.POST.get('address')


        print("Full Name:", full_name)
        print("Email:", email)
        print("Phone:", phone)
        print("Company:", company_trainer)
        print("Expertise:", expertise)
        print("Address:", address)



        obj = Trainer.objects.create(
                full_name=full_name,
                email=email,
                phone=phone,
                expertise=expertise,
                experience=experience,
                address=address,
                company_id=company_trainer,

            )



        response_data = {'message': "Trainer created successfully"}


        return JsonResponse(response_data)
    else:

        data30 = Trainer.objects.all()
        data22 = Company.objects.all()
        return render(request, 'hr/training/trainers.html', {'data30': data30,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)






def update_trainer_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        trainer_id = request.POST.get('trainer_id')

        full_name_upd = request.POST.get('full_name_upd')
        email_upd = request.POST.get('email_upd')
        phone_upd = request.POST.get('phone_upd')
        company_trainer_upd = request.POST.get('company_trainer_upd')
        expertise_upd = request.POST.get('expertise_upd')
        experience_upd = request.POST.get('experience_upd')
        address_upd = request.POST.get('address_upd')

        print(trainer_id,full_name_upd, email_upd, phone_upd,company_trainer_upd, expertise_upd,experience_upd, address_upd)


        obj = Trainer.objects.get(id=trainer_id)

        obj.full_name = full_name_upd
        obj.email = email_upd
        obj.phone = phone_upd
        obj.expertise = expertise_upd
        obj.experience = experience_upd
        obj.address = address_upd
        obj.company_id = company_trainer_upd

        obj.save()

        response_data = {'message': "Trainer record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def get_trainer_data(request, id):
    if request.method == 'GET':
        obj = Trainer.objects.get(id=id)

        data = {
            'full_name_upd': obj.full_name,
            'email_upd': obj.email,
            'phone_upd': obj.phone,
            'company_trainer_upd': obj.company_id,
            'expertise_upd': obj.expertise,
            'address_upd': obj.address,

        }
        print(data)
        return JsonResponse(data)





def delete_trainer_data(request):
    if request.method == 'POST':

        trainer_id = request.POST.get('trainer_id')
       # data_id = request.POST.get('data_id')
        print(trainer_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Trainer.objects.get(id=trainer_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)







def Add_training_type_data(request):
    if request.method == 'POST':



        training_type_trainer = request.POST.get('training_type_trainer')



        print("Training Type:", training_type_trainer)




        obj = Training_Type.objects.create(
                training_type=training_type_trainer,

            )



        response_data = {'message': "Training Type created successfully"}


        return JsonResponse(response_data)
    else:

        data31 = Training_Type.objects.all()
        return render(request, 'hr/training/training_tyep.html', {'data31': data31})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)






def update_training_type_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        training_type_id = request.POST.get('training_type_id')

        training_type_trainer_upd = request.POST.get('training_type_trainer_upd')

        print(training_type_id,training_type_trainer_upd)


        obj = Training_Type.objects.get(id=training_type_id)

        obj.training_type = training_type_id


        obj.save()

        response_data = {'message': "Training Type record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def get_training_type_data(request, id):
    if request.method == 'GET':
        obj = Training_Type.objects.get(id=id)

        data = {
            'training_type_trainer_upd': obj.training_type,


        }
        print(data)
        return JsonResponse(data)







def delete_training_type_data(request):
    if request.method == 'POST':

        training_type_id = request.POST.get('training_type_id')
       # data_id = request.POST.get('data_id')
        print(training_type_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Training_Type.objects.get(id=training_type_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)









def Add_training_list_data(request):
    if request.method == 'POST':



        company_training_list = request.POST.get('company_training_list')
        training_type_list = request.POST.get('training_type_list')
        full_name_list = request.POST.get('full_name_list')
        employee_list = request.POST.get('employee_list')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        training_cost = request.POST.get('training_cost')
        description = request.POST.get('description')



        print(company_training_list,training_type_list,full_name_list,employee_list,start_date,end_date,training_cost,description)




        obj = Training_List.objects.create(
                start_date=start_date,
                end_date=end_date,
                training_cost=training_cost,
                description=description,
                company_id=company_training_list,
                employee_id=employee_list,
                full_name_id=full_name_list,
                training_type_id=training_type_list,

            )



        response_data = {'message': "Training List created successfully"}


        return JsonResponse(response_data)
    else:

        data22 = Company.objects.all()
        data31 = Training_Type.objects.all()
        data30 = Trainer.objects.all()
        data1 = CustomUser.objects.all()
        data32 = Training_List.objects.all()
        return render(request, 'hr/training/training_list.html', {'data31': data31,'data32':data32,'data1':data1,'data30':data30,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)







def update_training_list_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        training_list_id = request.POST.get('training_list_id')

        company_training_list_upd = request.POST.get('company_training_list_upd')
        training_type_list_upd = request.POST.get('training_type_list_upd')
        full_name_list_upd = request.POST.get('full_name_list_upd')
        employee_list_upd = request.POST.get('employee_list_upd')
        start_date_upd = request.POST.get('start_date_upd')
        end_date_upd = request.POST.get('end_date_upd')
        training_cost_upd = request.POST.get('training_cost_upd')
        description_upd = request.POST.get('description_upd')

        print(training_list_id,company_training_list_upd, training_type_list_upd, full_name_list_upd,employee_list_upd,start_date_upd,end_date_upd,training_cost_upd,description_upd)


        obj = Training_List.objects.get(id=training_list_id)


        obj.start_date = start_date_upd
        obj.end_date = end_date_upd
        obj.training_cost = training_cost_upd
        obj.description = description_upd
        obj.company_id = company_training_list_upd
        obj.employee_id = employee_list_upd
        obj.full_name_id = full_name_list_upd
        obj.training_type_id = training_type_list_upd



        obj.save()

        response_data = {'message': "Training List record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)


def get_training_list_data(request, id):
    if request.method == 'GET':
        obj = Training_List.objects.get(id=id)

        data = {
            'company_training_list_upd': obj.company_id,
            'training_type_list_upd': obj.training_type_id,
            'full_name_list_upd': obj.full_name_id,
            'employee_list_upd': obj.employee_id,
            'start_date_upd': obj.start_date,
            'end_date_upd': obj.end_date,
            'training_cost_upd': obj.training_cost,
            'description_upd': obj.description,

        }
        print(data)
        return JsonResponse(data)


def delete_training_list_data(request):
    if request.method == 'POST':

        training_list_id = request.POST.get('training_list_id')
       # data_id = request.POST.get('data_id')
        print(training_list_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Training_List.objects.get(id=training_list_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)










def Add_events_data(request):
    if request.method == 'POST':



        company = request.POST.get('company')
        department = request.POST.get('department')
        event_title = request.POST.get('event_title')
        event_date = request.POST.get('event_date')
        event_time = request.POST.get('event_time')

        print(company,department,event_title,event_time,event_date)




        obj = Events.objects.create(
                event_title=event_title,
                event_date=event_date,
                event_time=event_time,
                company_id=company,
                department_id=department,


            )



        response_data = {'message': "Training List created successfully"}


        return JsonResponse(response_data)
    else:

        data41 = Events.objects.all()
        data19 = Department.objects.all()
        data22 = Company.objects.all()
        return render(request, 'hr/events&meetings/events.html', {'data41':data41,'data19':data19,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)




def update_events_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        events_id = request.POST.get('events_id')

        company_upd = request.POST.get('company_upd')
        department_upd = request.POST.get('department_upd')
        event_title_upd = request.POST.get('event_title_upd')
        event_date_upd = request.POST.get('event_date_upd')
        event_time_upd = request.POST.get('event_time_upd')

        print(events_id,company_upd, department_upd, event_title_upd,event_date_upd,event_time_upd)


        obj = Events.objects.get(id=events_id)


        obj.event_title = event_title_upd
        obj.event_date = event_date_upd
        obj.event_time = event_time_upd
        obj.company_id = company_upd
        obj.department_id = department_upd


        obj.save()

        response_data = {'message': "Events record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def get_events_data(request, id):
    if request.method == 'GET':
        obj = Events.objects.get(id=id)

        data = {
            'event_title_upd': obj.event_title,
            'event_date_upd': obj.event_date,
            'event_time_upd': obj.event_time,
            'company_upd': obj.company_id,
            'department_upd': obj.department_id,



        }
        print(data)
        return JsonResponse(data)




def delete_events_data(request):
    if request.method == 'POST':

        events_id = request.POST.get('events_id')
       # data_id = request.POST.get('data_id')
        print(events_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Events.objects.get(id=events_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)








def Add_meetings_data(request):
    if request.method == 'POST':



        company = request.POST.get('company')
        employee = request.POST.get('employee')
        meeting_title = request.POST.get('meeting_title')
        meeting_date = request.POST.get('meeting_date')
        meeting_time = request.POST.get('meeting_time')

        print(company,employee,meeting_title,meeting_date,meeting_time)




        obj = Meetings.objects.create(
                meeting_title=meeting_title,
                meeting_date=meeting_date,
                meeting_time=meeting_time,
                company_id=company,
                employee_id=employee,


            )



        response_data = {'message': "Training List created successfully"}


        return JsonResponse(response_data)
    else:

        data42 = Meetings.objects.all()
        data1 = CustomUser.objects.all()
        data22 = Company.objects.all()
        return render(request, 'hr/events&meetings/meetings.html', {'data42':data42,'data1':data1,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)




def update_meetings_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        meetings_id = request.POST.get('meetings_id')

        company_upd = request.POST.get('company_upd')
        employee_upd = request.POST.get('employee_upd')
        meeting_title_upd = request.POST.get('meeting_title_upd')
        meeting_date_upd = request.POST.get('meeting_date_upd')
        meeting_time_upd = request.POST.get('meeting_time_upd')

        print(meetings_id,company_upd, employee_upd, meeting_title_upd,meeting_date_upd,meeting_time_upd)


        obj = Meetings.objects.get(id=meetings_id)


        obj.meeting_title = meeting_title_upd
        obj.meeting_date = meeting_date_upd
        obj.meeting_time = meeting_time_upd
        obj.company_id = company_upd
        obj.employee_id = employee_upd


        obj.save()

        response_data = {'message': "meetings record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def get_meetings_data(request, id):
    if request.method == 'GET':
        obj = Meetings.objects.get(id=id)

        data = {
            'meeting_title_upd': obj.meeting_title,
            'meeting_date_upd': obj.meeting_date,
            'meeting_time_upd': obj.meeting_time,
            'company_upd': obj.company_id,
            'employee_upd': obj.employee_id,



        }
        print(data)
        return JsonResponse(data)




def delete_meetings_data(request):
    if request.method == 'POST':

        meetings_id = request.POST.get('meetings_id')
       # data_id = request.POST.get('data_id')
        print(meetings_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Meetings.objects.get(id=meetings_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)

















def Add_category_data(request):
    if request.method == 'POST':



        category_name = request.POST.get('category_name')



        print("Category Name:", category_name)




        obj = Assets_Category.objects.create(
                category=category_name,

            )



        response_data = {'message': "Trainer created successfully"}


        return JsonResponse(response_data)
    else:

        data35 = Assets_Category.objects.all()
        return render(request, 'hr/assets/category.html', {'data35': data35})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)








def update_category_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        category_id = request.POST.get('category_id')

        category_name_upd = request.POST.get('category_name_upd')

        print(category_id,category_name_upd)


        obj = Assets_Category.objects.get(id=category_id)


        obj.category = category_name_upd



        obj.save()

        response_data = {'message': "Training List record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def get_category_data(request, id):
    if request.method == 'GET':
        obj = Assets_Category.objects.get(id=id)

        data = {
            'category_name_upd': obj.category,




        }
        return JsonResponse(data)



def delete_category_data(request):
    if request.method == 'POST':

        category_id = request.POST.get('category_id')
       # data_id = request.POST.get('data_id')
        print(category_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Assets_Category.objects.get(id=category_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)









def Add_assets_data(request):
    if request.method == 'POST':



        asset_name = request.POST.get('asset_name')
        company_asset_code = request.POST.get('company_asset_code')
        category = request.POST.get('category')
        is_working = request.POST.get('is_working')
        company_assets = request.POST.get('company_assets')
        employee_assets = request.POST.get('employee_assets')
        purchase_date = request.POST.get('purchase_date')
        warranty_date = request.POST.get('warranty_date')
        manufacturer = request.POST.get('manufacturer')
        invoice_number = request.POST.get('invoice_number')
        serial_number = request.POST.get('serial_number')



        print(asset_name,company_asset_code,category,is_working,company_assets,employee_assets,purchase_date,warranty_date,manufacturer,invoice_number,serial_number)




        obj = Assets.objects.create(
                asset_name=asset_name,
                company_asset_code=company_asset_code,
                is_working=is_working,
                purchase_date=purchase_date,
                warranty_end_date=warranty_date,
                manufacturer=manufacturer,
                invoice_number=invoice_number,
                serial_number=serial_number,
                category_id=category,
                company_id=company_assets,
                employee_id=employee_assets,

            )



        response_data = {'message': "Training List created successfully"}


        return JsonResponse(response_data)
    else:

        data22 = Company.objects.all()
        data1 = CustomUser.objects.all()
        data35 = Assets_Category.objects.all()
        data36 = Assets.objects.all()
        return render(request, 'hr/assets/assets.html', {'data35': data35,'data36':data36,'data1':data1,'data22':data22})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)






def update_assets_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        assets_id = request.POST.get('assets_id')

        asset_name_upd = request.POST.get('asset_name_upd')
        company_asset_code_upd = request.POST.get('company_asset_code_upd')
        category_upd = request.POST.get('category_upd')
        is_working_upd = request.POST.get('is_working_upd')
        company_assets_upd = request.POST.get('company_assets_upd')
        employee_assets_upd = request.POST.get('employee_assets_upd')
        purchase_date_upd = request.POST.get('purchase_date_upd')
        warranty_date_upd = request.POST.get('warranty_date_upd')
        manufacturer_upd = request.POST.get('manufacturer_upd')
        invoice_number_upd = request.POST.get('invoice_number_upd')
        serial_number_upd = request.POST.get('serial_number_upd')

        print(assets_id,asset_name_upd, company_asset_code_upd, category_upd,is_working_upd,company_assets_upd,employee_assets_upd,purchase_date_upd,warranty_date_upd,manufacturer_upd,invoice_number_upd,serial_number_upd)


        obj = Assets.objects.get(id=assets_id)


        obj.asset_name = asset_name_upd
        obj.company_asset_code = company_asset_code_upd
        obj.is_working = is_working_upd
        obj.purchase_date = purchase_date_upd
        obj.warranty_end_date = warranty_date_upd
        obj.manufacturer = manufacturer_upd
        obj.invoice_number = invoice_number_upd
        obj.serial_number = serial_number_upd
        obj.company_id = company_assets_upd
        obj.category_id = category_upd
        obj.employee_id = employee_assets_upd



        obj.save()

        response_data = {'message': "Training List record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)

def get_assets_data(request, id):
    if request.method == 'GET':
        obj = Assets.objects.get(id=id)

        data = {
            'asset_name_upd': obj.asset_name,
            'company_asset_code_upd': obj.company_asset_code,
            'category_upd': obj.category_id,
            'is_working_upd': obj.is_working,
            'company_assets_upd': obj.company_id,
            'employee_assets_upd': obj.employee_id,
            'purchase_date_upd': obj.purchase_date,
            'warranty_date_upd': obj.warranty_end_date,
            'manufacturer_upd': obj.manufacturer,
            'invoice_number_upd': obj.invoice_number,
            'serial_number_upd': obj.serial_number,



        }
        return JsonResponse(data)




def delete_assets_data(request):
    if request.method == 'POST':

        assets_id = request.POST.get('assets_id')
       # data_id = request.POST.get('data_id')
        print(assets_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Assets.objects.get(id=assets_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "workingfine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)


def Add_clients_data(request):
    if request.method == 'POST':



        name_clients = request.POST.get('name_clients')
        client_id = request.POST.get('client_id')
        mobile_no = request.POST.get('mobile_no')
        email = request.POST.get('email')

        print(name_clients,client_id,mobile_no,email)




        obj = Client.objects.create(
                name=name_clients,
                client_id=client_id,
                mobile_no=mobile_no,
                email=email,


            )



        response_data = {'message': "Training List created successfully"}


        return JsonResponse(response_data)
    else:

        data40 = Client.objects.all()
        return render(request, 'hr/project/clients.html', {'data40':data40})
    return JsonResponse({'error': 'Invalid form data.'}, status=400)




def update_clients_data(request):
    if request.method == 'POST':
        #data_id = request.POST.get('data_id')
        clients_id = request.POST.get('clients_id')

        name_clients_upd = request.POST.get('name_clients_upd')
        client_id_upd = request.POST.get('client_id_upd')
        mobile_no_upd = request.POST.get('mobile_no_upd')
        email_upd = request.POST.get('email_upd')

        print(Job_Interview,name_clients_upd, client_id_upd, mobile_no_upd,email_upd)


        obj = Client.objects.get(id=clients_id)


        obj.name = name_clients_upd
        obj.client_id = client_id_upd
        obj.mobile_no = mobile_no_upd
        obj.email = email_upd


        obj.save()

        response_data = {'message': "Training List record updated successfully."}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid form data.'}, status=400)



def get_clients_data(request, id):
    if request.method == 'GET':
        obj = Client.objects.get(id=id)

        data = {
            'name_clients_upd': obj.name,
            'client_id_upd': obj.client_id,
            'mobile_no_upd': obj.mobile_no,
            'email_upd': obj.email,



        }
        print(data)
        return JsonResponse(data)




def delete_clients_data(request):
    if request.method == 'POST':

        clients_id = request.POST.get('clients_id')
       # data_id = request.POST.get('data_id')
        print(clients_id)

     #   user = CustomUser.objects.get(id=data_id)
        obj = Client.objects.get(id=clients_id)
        if obj:
            obj.delete()
            response_data = {'first_name': "working fine"}
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Invalid form data.'}, status=400)









def faq(request):
    return render(request,'hr/faq.html')




def contacts_d(request):
    return render(request,'hr/contacts.html')














































