


from .models import EmployeeMaster,CustomUser,LeaveRequest
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
# forms.py
from django.core.exceptions import ValidationError
from django import forms
from django.core.validators import EmailValidator, MinLengthValidator, MaxLengthValidator

"""
class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2']


"""




class CustomSignupForm(UserCreationForm):
    is_manager = forms.BooleanField(required=False)
    is_employee = forms.BooleanField(required=False)
    is_hr = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'first_name','last_name','email', 'is_manager', 'is_employee', 'is_hr')


class CustomUpdateForm(UserCreationForm):
    is_manager = forms.BooleanField(required=False)
    is_employee = forms.BooleanField(required=False)
    is_hr = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'is_manager', 'is_employee', 'is_hr']








"""

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email', 'password1', 'password2',]

"""



class DateInput(forms.DateInput):
    input_type = 'date'


class EmployeeMasterForm(forms.ModelForm):
  # JoiningDate=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,widget = DateInput )
    # CreatedDate=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,widget = DateInput)
   #  ModifiedDate=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,widget = DateInput)

    class Meta:
        model= EmployeeMaster
        #fields= ('image','Role')
        fields=('EmployeeID','Role','JoiningDate' ,'phone_number','CreatedBy','Designation' ,'Role','Shift_time','BirthDate','Gender','companyname','MaratialStatus','Designation','Department','JoiningDate', 'image' )
        #exclude = ('user','BirthDate','JoiningDate',' CreatedDate','ModifiedDate','StateId','CountryId','Cast', 'ModifiedBy',' ModifiedBy','LeaveDate','IsLeave','PANNo','Desk_Number','Worktype','IsActive','name','EmployeeTypeId','EmployeeGradeId','DepartmentId','DesignationId','ShiftId'  )
        #fields="__all__"
       # Fields=['EmployeeID','DepartmentId','DesignationId','BirthDate','Gender','MaratialStatus','Cast','JoinDate','EmployeeNo','CreatedDate','phone_number','JoinDate','Desk_Number','WorkLocation','Worktype']
   #     widgets = {
    #        'my_date': DateInput()
    #    }






"""
class ApplyingLeaveForm(forms.ModelForm):
    class Meta:
        model = EmployeeLeaveMaster

        fields=('LeaveCategoryId','StartDate','EndDate','totalday','reason',)


"""
















class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['employee', 'LeaveCategory', 'StartDate', 'EndDate', 'totaldays','reason', 'comments']




def validate_username_characters(username):
    if not username.isalpha():
        raise ValidationError(('Username should contain only characters (no numbers or special characters).'), code='username_characters')
    if len(username) < 6:
        raise ValidationError(('Username must be at least 6 characters long.'), code='username_length')


# Custom username validator
def validate_username_characters(username):
    if not username.isalpha():
        raise ValidationError("Username should contain only characters (no numbers or special characters).")


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, validators=[validate_username_characters])
    email = forms.EmailField()

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username.isalpha():
            raise ValidationError("Username should contain only characters (no numbers or special characters).")
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password
 #   username = forms.CharField(max_length=150, validators=[MinLengthValidator(5)])
'''  username = forms.CharField(max_length=150, validators=[MinLengthValidator(5)])
    username = forms.CharField(max_length=150, validators=[MinLengthValidator(5)])
    password = forms.CharField(widget=forms.PasswordInput, validators=[MinLengthValidator(8)])
    conformpassword = forms.CharField(widget=forms.PasswordInput)
    fullname = forms.CharField(max_length=255)
    email = forms.EmailField(validators=[EmailValidator])
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])
    department = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100)
    worktype = forms.ChoiceField(choices=[('fulltime', 'Full-Time'), ('parttime', 'Part-Time')])
    dob = forms.DateField()
    employee = forms.CharField(max_length=10)
    dateofjoining = forms.DateField()
    role = forms.ChoiceField(choices=[('employee', 'Employee'), ('hr', 'HR'), ('manager', 'Manager')])
    shift = forms.CharField(max_length=100)
    phonenumber = forms.CharField(max_length=15, validators=[MinLengthValidator(10)])
    city = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10, validators=[MinLengthValidator(6)])
    designation = forms.ChoiceField(choices=[('employee', 'Employee'), ('hr', 'HR'), ('manager', 'Manager')])
    profile_photo = forms.ImageField()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        conformpassword = cleaned_data.get("conformpassword")

        if password != conformpassword:
            raise forms.ValidationError("Passwords do not match. Please try again.")
'''

