from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from decimal import Decimal
from django.core.exceptions import ValidationError
#   from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
# Create your models here.
class CustomUser(AbstractUser):
    is_employee = models.BooleanField(default=False)
    is_hr = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
""""""
#class Student(models.Model):
#   user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Gender(models.Model):
    gender = models.CharField(max_length=12)

    def __str__(self):
        return self.gender


class MaratialStatus(models.Model):
    status = models.CharField(max_length=12)

    def __str__(self):
        return self.status


class EmployeeMaster(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    fullname=models.CharField(max_length=100)
    EmployeeID = models.CharField(max_length=200,null=True)
    EmployeeTypeId = models.CharField(max_length=200,null=True)
    EmployeeGradeId = models.CharField(max_length=200,null=True)
    DepartmentId = models.CharField(max_length=200,null=True)
    DesignationId = models.CharField(max_length=200,null=True)
    employee_type=models.CharField(max_length=20 ,choices=[('FullTime','FullTime'),('PartTime','PartTime')],default="FullTime")

    Department = models.CharField(max_length=100, choices=[('HR', 'HR'), ("IT", "IT"), ("ACCOUNTS", "ACCOUNTS"),("SALES","SALES"),("BA","BUSINESS ANALYST"),("Manager&CEO","Manager&CEO")])
    Role=models.CharField(max_length=200,null=True)
    ShiftId = models.CharField(max_length=200,null=True)
    Shift_time=models.CharField (max_length=20, choices=[('9:30 AM-7:00PM','9:30 AM-7:00PM'),('2:00 PM-10:00 PM','2:00 PM-10:00 PM'),('6:00 AM- 2:00PM','6:00 AM- 2:00PM')])
    #MiddleName = models.CharField(max_length=200)
    BirthDate = models.DateField(null=True )
    companyname=models.CharField (max_length=20, choices=[('PROGMENT','PROGMENT'),('SMARTNCODE','SMARTNCODE')])
    FatherName = models.CharField(max_length=200,null=True)
    Gender =models.CharField (max_length=20, choices=[('MALE','MALE'),('FEMALE','FEMALE'),('Others','Others')])
    MaratialStatus = models.CharField (max_length=20, choices=[('Single','SINGLE'),('Married','MARRIED')])
    #Cast = models.CharField(max_length=50,null=True)
    country = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=50,null=True)
    City = models.CharField(max_length=100,null=True)
    Address = models.TextField(default="HYD",null=True)
    PinCode = models.CharField(max_length=15,null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)  # Validators should be a list
    JoiningDate =  models.DateField(null=True)
   # EmployeeNo = models.CharField(max_length=20, default=False,null=True)
    #Email = models.EmailField(max_length=150, default=False)
  #  CreatedDate = models.DateField(auto_now_add=True, null=True)
    CreatedBy = models.CharField(max_length=100, default="HR",null=True)
    ModifiedBy = models.CharField(max_length=100,null=True)
   # ModifiedDate = models.DateField(auto_now = True, null=True)
    IsActive = models.BooleanField(default=True)
    IsLeave = models.BooleanField(default=False)
   # LeaveDate = models.DateField(default=False)
    PANNo = models.CharField(max_length=50, default=False)
    Desk_Number = models.CharField(max_length=100, default="snc_hyd_000",null=True)
    WorkLocation = models.CharField(max_length=150, default="Hyderbad",null=True)
    Worktype = models.CharField(max_length=150, default="full-time",null=True)

    Designation = models.CharField(max_length=100,choices=[('B.TECH', 'B.TECH'), ('DEGREE', 'DEGREE'), ('M.TECH', 'M.TECH'),
                                            ('Phd', 'Phd'), ('BCA', 'BCA'), ('BBA', 'BBA'), ('MBA', 'MBA'),
                                            ('MCA', 'MCA')])
    Branch = models.CharField(max_length=200)
    Education_type = models.CharField(max_length=20, choices=[('FullTime', 'FullTime'), ('PartTime', 'PartTime')],
                                     default="FullTime")
    university=models.CharField(max_length=200)
    passing_year=models.CharField(max_length=50)

    image = models.ImageField(upload_to='img/')

    class Meta:
        ordering = ['BirthDate']

    def __str__(self):
        return self.user.username




#class LeaveCategoryMaster(models.Model):
  #  leave_categoryid=models.CharField(max_length=100)
  #  leave_category= models.CharField(max_length=100)
 #   createddate=models.DateTimeField(default=False)
#    createdby=models.CharField(max_length=100)
#    modified_by=models.CharField(max_length=100)
  #  modified_date=models.DateTimeField(default=False)
 #   is_active= models.BooleanField(default=True)
 #   def __str__(self):
 #       return self.leave_category


class Immegration(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=100)
    document_number=models.CharField(max_length=100)
    issue_date=models.DateField()
    expired_date=models.DateField()
    country=models.CharField(max_length=100)
    document_file = models.FileField(upload_to='files/')


class Emergency_Contacts(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    relation=models.CharField(max_length=100)
    email=models.EmailField()
    name=models.CharField(max_length=100)
    address=models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_no = models.CharField(validators=[phone_regex], max_length=17, blank=True,null=True)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zip_code=models.CharField(max_length=20)
    country = models.CharField(max_length=100)


class Social_Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    facebook_profile=models.CharField(max_length=100)
    linkedin_profile=models.CharField(max_length=100)
    skype_profile=models.CharField(max_length=100)
    twitter_profile=models.CharField(max_length=100)
    whatsapp_profile=models.CharField(max_length=100)


class Documents_All(models.Model):
    user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=50)
    title=models.CharField(max_length=100)
    expired_date=models.DateField()
    description=models.TextField()
    document_file=models.FileField()


class Qualifications(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name_of_university=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    from_date=models.DateField()
    to_date=models.DateField()
    languages=models.CharField(max_length=50)
    skills=models.CharField(max_length=50)
    description=models.TextField()



class Work_Experience(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    from_date = models.DateField()
    to_date = models.DateField()
    description = models.TextField()
    designation = models.CharField(max_length=80)
    document_file = models.FileField()

class Bank_Account(models.Model):
    user =  models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    account_title=models.CharField(max_length=100)
    account_number=models.CharField(max_length=100)
    bankname=models.CharField(max_length=100)
    ifsc_code=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)






class Basic_Salary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    month_year = models.DateField()
    payslip_type = models.CharField(max_length=100)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)



class Allowances(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    month_year = models.DateField()
    allowance_type = models.CharField(max_length=200)
    allowance_title = models.CharField(max_length=100)
    allowance_amount = models.DecimalField(max_digits=10, decimal_places=2)



class Commissions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    month_year = models.DateField()
    commission_title = models.CharField(max_length=100)
    commission_amount = models.DecimalField(max_digits=10, decimal_places=2)



class Loan(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    month_year = models.DateField()
    title = models.CharField(max_length=100)
    number_of_installments = models.PositiveIntegerField()
    loan_option = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=200)



class Statutory_Deduction(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    month_year = models.DateField()
    deduction_title = models.CharField(max_length=200)
    deduction_option = models.CharField(max_length=100)
    deduction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=200)




class Other_Payments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    month_year = models.DateField()
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)




class Over_Time(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    month_year = models.DateField()
    title = models.CharField(max_length=200)
    number_of_days = models.PositiveIntegerField()
    total_hours = models.PositiveIntegerField()
    rate = models.CharField(max_length=100)
class Company(models.Model):

    name = models.CharField(max_length=100)
    trading_name = models.CharField(max_length=100)
    registration_number = models.PositiveIntegerField()
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

class Client(models.Model):
    name=models.CharField(max_length=200)
    client_id=models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_no = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    email=models.EmailField(max_length = 254)

class Projects(models.Model):
    title=models.CharField(max_length=200)
    client=models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date=models.DateField()
    end_date=models.DateField()
    priority=models.CharField(max_length=100)
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    Assigned_employees=models.ManyToManyField(CustomUser)
    summary=models.CharField(max_length=200)
    Progress=models.CharField(max_length=200)

class Tasks(models.Model):
    title=models.CharField(max_length=200)
    start_date=models.DateField(max_length=150)
    end_date=models.DateField(max_length=150)
    project=models.ForeignKey(Projects,on_delete=models.CASCADE)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    priority = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    employees=models.ManyToManyField(CustomUser)
    description=models.TextField()
    Progress = models.CharField(max_length=200)

class Department(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    department_head = models.CharField(max_length=100)
class Location(models.Model):
    location_head = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)

    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.PositiveIntegerField()

class Designation(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)

class Announcements(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    summary = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=100)

class Company_Policy(models.Model):
    name = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Promotions(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    promotion_date = models.DateField()
    description = models.CharField(max_length=100)



class Awards(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    award_type = models.CharField(max_length=100)
    gift = models.CharField(max_length=100)
    cash = models.CharField(max_length=100)
    awards_information = models.CharField(max_length=100)
    award_date = models.DateField()



class Travel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    arrangement_type = models.CharField(max_length=100)
    purpose_of_visit = models.CharField(max_length=100)
    place_of_visit = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    expected_budget = models.DecimalField(max_digits=10, decimal_places=2)
    actual_budget = models.DecimalField(max_digits=10, decimal_places=2)
    travel_mode = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Transfer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    from_department = models.CharField(max_length=100)
    to_department = models.CharField(max_length=100)
    transfer_date = models.DateField()
    description = models.CharField(max_length=100)



class Resignation(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    notice_date = models.DateField()
    resignation_date = models.DateField()
    description = models.CharField(max_length=100)




class Complains(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    complain_title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    complain_date = models.DateField()



class Warnings(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    warning_type = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    warning_date = models.DateField()
    status = models.CharField(max_length=100)


class Terminations(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    termination_type = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    termination_date = models.DateField()
    notice_date = models.DateField()




class Trainer(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    expertise = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    address = models.CharField(max_length=100)



class Training_Type(models.Model):
    training_type = models.CharField(max_length=100)



class Training_List(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    training_type = models.ForeignKey(Training_Type, on_delete=models.CASCADE)
    full_name = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    training_cost = models.CharField(max_length=15)
    description = models.CharField(max_length=100)




class Assets_Category(models.Model):
    category = models.CharField(max_length=100)



class Assets(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Assets_Category, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=100)
    company_asset_code = models.CharField(max_length=100)
    is_working = models.CharField(max_length=100)
    purchase_date = models.DateField()
    warranty_end_date = models.DateField()
    manufacturer = models.CharField(max_length=100)
    invoice_number = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)


class Job_Post(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    job_category = models.CharField(max_length=100)
    no_of_vacancy = models.CharField(max_length=100)
    date_of_closing = models.DateField()
    gender = models.CharField(max_length=100)
    minimum_experience = models.CharField(max_length=100)
    is_featured = models.CharField(max_length=100)
    status = models.CharField(max_length=100)


class Job_Candidate(models.Model):
    job_title = models.ForeignKey(Job_Post, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=100)
    candidate_email = models.CharField(max_length=100)
    resume = models.FileField(upload_to='files/')
    status = models.CharField(max_length=100)
    apply_date = models.DateField(max_length=100)






class Job_Interview(models.Model):
    job_title = models.ForeignKey(Job_Post, on_delete=models.CASCADE)
    candidate_name = models.ForeignKey(Job_Candidate, on_delete=models.CASCADE)
    interview_place = models.CharField(max_length=100)
    interview_date = models.DateField()
    interview_time = models.TimeField()






class Events(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    event_title = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()




class Meetings(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    meeting_title = models.CharField(max_length=100)
    meeting_date = models.DateField()
    meeting_time = models.TimeField()



class Leavecategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name


class LeaveBalance(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    leave_type = models.ForeignKey(Leavecategory, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=5, decimal_places=2)




class LeaveRequest(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   # EmployeeLeaveCategoryMapID=models.CharField(max_length=100)
   # EmployeeID=models.ForeignKey(EmployeeMaster, on_delete=models.CASCADE)
    LeaveCategory=models.ForeignKey(Leavecategory, on_delete=models.CASCADE)
    StartDate=models.DateField()
    EndDate=models.DateField()
    totaldays=models.FloatField()
    isfirst_halfday=models.BooleanField(default=False)
    islast_halfday=models.BooleanField(default=False)
    reason = models.TextField()
    comments = models.TextField()
    applydate=models.DateTimeField(auto_now=True)
    approvedby=models.CharField(max_length=100)
    modifiedBy=models.CharField(max_length=100)
    modifiedDate=models.DateTimeField(blank=True,null=True)
    IsActive=models.BooleanField(default=True)
    status=models.CharField(max_length=100,default="Pending")
    total_leave_days=models.DecimalField(max_digits=5, decimal_places=2,default=24)

    def __str__(self):
        return str(self.employee)


class LeaveApproval(models.Model):
    leave_request = models.ForeignKey(LeaveRequest, on_delete=models.CASCADE)
    approver = models.CharField(max_length=100)
    approval_status = models.CharField(max_length=50)
    comments = models.TextField()





class Notification(models.Model):
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    notification_type = models.CharField(max_length=50,choices=[('Leave', 'Leave'), ('Permission','Permision')])
    status=models.BooleanField(default=False)





class Permission(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    permission_category=models.CharField(max_length=100,choices=[('Early Login', 'Early Login'), ('Early Logout', 'Early Logout'), ('Late Login', 'Late Login'),('Late Logout', 'Late Logout'),('WFH', 'WFH')])
    StartDate = models.DateField()
    EndDate = models.DateField()
    start_time=models.TimeField(null=True)
    end_time=models.TimeField(null=True)
    Time_duration=models.CharField(max_length=5)
    location=models.CharField(max_length=50 ,default="Hyderbad")
    reason=models.CharField(max_length=100)
    status=models.BooleanField(default=True)

class PermissionApproval(models.Model):
    permission=models.ForeignKey(Permission, on_delete=models.CASCADE)
    approver = models.CharField(max_length=100)
    approval_status = models.CharField(max_length=50,default="Pending")
    comments = models.TextField()





class Attendance(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   # date = models.DateField()
    entry_type = models.CharField(max_length=10)  # Can be 'punch_in', 'punch_out', 'break_in', or 'break_out'
    timestamp = models.DateTimeField(max_length=50,null=True)
   # totalhours = models.CharField(max_length=50)




class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

class Public_holidays(models.Model):
    name= models.CharField(max_length=100)
    date= models.DateField()






class EmployeeLeaveMap(models.Model):
    EmployeeLeaveID=models.CharField(max_length=100)
    EmployeeId=models.CharField(max_length=100)
    leaveid=models.CharField(max_length=100)
    leavecount=models.PositiveIntegerField()






class Pro(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150,)




















class StateMaster(models.Model):
    stateid= models.CharField(max_length=100)
    countryid=models.CharField(max_length=100)
    statename=models.CharField(max_length=80)
    created_date=models.DateTimeField(default=False)
    Is_Active = models.BooleanField(default=True)



class ShiftMaster(models.Model):
    Shiftid=models.CharField(max_length=100)
    shift=models.CharField(max_length=100)
    from_time=models.CharField(max_length=50)
    to_time=models.CharField(max_length=50)
    created_date=models.DateTimeField(default=False)
    created_by=models.CharField(max_length=150)
    modified_by=models.CharField(max_length=150)

class RoleMaster(models.Model):
    roll_id=models.CharField(max_length=100)
    rool_name=models.CharField(max_length=150)
    created_date=models.DateTimeField(default=False)
    created_by=models.CharField(max_length=100)
    modified_by=models.CharField(max_length=100)
    modified_date=models.DateTimeField(default=False)
    reports_to=models.CharField(max_length=100)


class InterviewMasterAssigned(models.Model):
        interview_id=models.CharField(max_length=100)
        interview_no=models.CharField(max_length=100)
        name=models.CharField(max_length=100)
        assigned=models.DateTimeField(default=False)
        assigned_emp=models.CharField(max_length=100)
class InterviewMaster(models.Model):
    interview_no=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=150, default=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Validators should be a list
    educationaid=models.CharField(max_length=100)
    departmentid=models.CharField(max_length=100)
    designationid=models.CharField(max_length=100)
    currentsalary=models.CharField(max_length=100)
    expectedsalary=models.FloatField(max_length=100)
    experience_year=models.IntegerField()
    experience_month=models.IntegerField()
    isjoin_days=models.IntegerField()
    JoinAfterDaysOrMonth=models.IntegerField()
    PersonalDetail=models.TextField(default=False)
    InterviewStatusId=models.CharField(max_length=100)
    InterviewDate=models.DateField(default=False)
    InterviewTime=models.TextField()
    JoinDate=models.DateField(default=False)
    Reason=models.CharField(max_length=100)
    CreatedDate=models.DateTimeField(default=False)
    CreatedBy=models.CharField(max_length=100)
    ModifiedBy=models.CharField(max_length=100)
    ModifiedDate=models.DateTimeField(default=False)
    IsActive=models.BooleanField(default=True)
    Assignedid=models.CharField(max_length=100)
    AssignedEmp=models.CharField(max_length=100)

class InterviewAttachment(models.Model):
    InterviewAttachmentMapID=models.CharField(max_length=100)
    InterviewId=models.CharField(max_length=100)
    Name=models.CharField(max_length=100)
    AttachmentType=models.CharField(max_length=100)
    CreatedDate=models.DateTimeField(default=False)
    CreatedBy=models.CharField(max_length=100)
    ModifiedBy=models.CharField(max_length=100)
    ModifiedDate=models.DateTimeField(default=False)
    IsActive=models.BooleanField(default=True)

class HolidayMaster(models.Model):
    Holidayid=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=250)
    startdate=models.DateTimeField(default=False)
    enddate=models.DateTimeField(default=False)
    CreatedDate=models.DateTimeField(default=False)
    CreatedBy=models.CharField(max_length=100)
    ModifiedBy=models.CharField(max_length=100)
    ModifiedDate=models.DateTimeField(default=False)
    IsActive=models.BooleanField(default=True)

class EmployeeWorkingDay(models.Model):
    EmployeeWorkingDayMapID=models.CharField(max_length=100)
    EmployeeId=models.CharField(max_length=100)
    dayname=models.CharField(max_length=100)
    createddate=models.DateTimeField(default=False)
    CreatedBy=models.CharField(max_length=100)
    ModifiedBy=models.CharField(max_length=100)
    ModifiedDate=models.DateTimeField(default=False)
    IsActive=models.BooleanField(default=True)


class EmployeeTypeMaster(models.Model):
    EmployeeTypeID=models.CharField(max_length=100)
    EmployeeType=models.CharField(max_length=100)
    NoOfLeavePerMonth=models.FloatField()
    CreatedDate=models.DateTimeField()
    CreatedBy=models.CharField(max_length=100)
    ModifiedBy=models.CharField(max_length=100)
    ModifiedDate=models.DateTimeField()
    IsActive=models.BooleanField(default=True)


class EmployeeRoleMaster(models.Model):
    EmployeeRoleID=models.CharField(max_length=100)
    EmployeeRole=models.CharField(max_length=100)
    CreatedDate=models.DateTimeField()
    CreatedBy=models.CharField(max_length=100)
    ModifiedBy=models.CharField(max_length=100)
    ModifiedDate=models.DateTimeField()
    IsActive=models.BooleanField(default=True)

class EmployeeLeaveMap(models.Model):
    EmployeeLeaveID=models.CharField(max_length=100)
    EmployeeId=models.CharField(max_length=100)
    leaveid=models.CharField(max_length=100)
    leavecount=models.PositiveIntegerField()






class EmployeeGradeMaster(models.Model):
    EmployeeGradeID=models.CharField(max_length=100)
    EmployeeGrade=models.CharField(max_length=100)
    CreatedDate=models.DateTimeField()
    CreatedBy=models.CharField(max_length=100)
    ModifiedDate=models.DateTimeField()
    ModifiedBy=models.CharField(max_length=100)
    IsActive=models.BooleanField(default=False)








