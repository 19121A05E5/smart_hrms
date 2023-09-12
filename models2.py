# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountsEmployeegrademaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    employeegradeid = models.CharField(db_column='EmployeeGradeID', max_length=100)  # Field name made lowercase.
    employeegrade = models.CharField(db_column='EmployeeGrade', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_employeegrademaster'


class AccountsEmployeeleavecategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    employeeleavecategorymapid = models.CharField(db_column='EmployeeLeaveCategoryMapID', max_length=100)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeId', max_length=100)  # Field name made lowercase.
    leavecategoryid = models.CharField(db_column='LeaveCategoryId', max_length=100)  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
    totalday = models.FloatField()
    isfirst_halfday = models.IntegerField()
    islast_halfday = models.IntegerField()
    reason = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    applydate = models.DateTimeField()
    approvedby = models.CharField(max_length=100)
    modifiedby = models.CharField(db_column='modifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.
    isapprove = models.IntegerField(db_column='IsApprove')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_employeeleavecategory'


class AccountsEmployeeleavemap(models.Model):
    id = models.BigAutoField(primary_key=True)
    employeeleaveid = models.CharField(db_column='EmployeeLeaveID', max_length=100)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeId', max_length=100)  # Field name made lowercase.
    leaveid = models.CharField(max_length=100)
    leavecount = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_employeeleavemap'


class AccountsEmployeemaster(models.Model):
    name = models.OneToOneField('AccountsUser', models.DO_NOTHING, primary_key=True)
    employeeid = models.CharField(db_column='EmployeeID', unique=True, max_length=200,null=True)  # Field name made lowercase.
    employeetypeid = models.CharField(db_column='EmployeeTypeId', unique=True, max_length=200,null=True)  # Field name made lowercase.
    employeegradeid = models.CharField(db_column='EmployeeGradeId', unique=True, max_length=200,null=True)  # Field name made lowercase.
    departmentid = models.CharField(db_column='DepartmentId', unique=True, max_length=200,null=True)  # Field name made lowercase.
    designationid = models.CharField(db_column='DesignationId', max_length=200,null=True)  # Field name made lowercase.
    shiftid = models.CharField(db_column='ShiftId', max_length=200,null=True)  # Field name made lowercase.
    birthdate = models.DateField(db_column='BirthDate',null=True)  # Field name made lowercase.
    fathername = models.CharField(db_column='FatherName', max_length=200,null=True)  # Field name made lowercase.
    cast = models.CharField(db_column='Cast', max_length=50,null=True)  # Field name made lowercase.
    countryid = models.CharField(db_column='CountryId', max_length=50,null=True)  # Field name made lowercase.
    stateid = models.CharField(db_column='StateId', max_length=50,null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=100,null=True)  # Field name made lowercase.
    pincode = models.CharField(db_column='PinCode', max_length=15,null=True)  # Field name made lowercase.
    phone_number = models.CharField(max_length=17,null=True)
    employeeno = models.CharField(db_column='EmployeeNo', max_length=20,null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate',null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100,null=True)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100,null=True)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate',null=True)  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.
    isleave = models.IntegerField(db_column='IsLeave')  # Field name made lowercase.
    leavedate = models.DateField(db_column='LeaveDate')  # Field name made lowercase.
    panno = models.CharField(db_column='PANNo', max_length=50)  # Field name made lowercase.
    desk_number = models.CharField(db_column='Desk_Number', max_length=100)  # Field name made lowercase.
    worklocation = models.CharField(db_column='WorkLocation', max_length=150)  # Field name made lowercase.
    worktype = models.CharField(db_column='Worktype', max_length=150)  # Field name made lowercase.
    gender = models.ForeignKey('AccountsGender', models.DO_NOTHING, db_column='Gender_id')  # Field name made lowercase.
    maratialstatus = models.ForeignKey('AccountsMaratialstatus', models.DO_NOTHING, db_column='MaratialStatus_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_employeemaster'


class AccountsEmployeerolemaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    employeeroleid = models.CharField(db_column='EmployeeRoleID', max_length=100)  # Field name made lowercase.
    employeerole = models.CharField(db_column='EmployeeRole', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_employeerolemaster'


class AccountsEmployeetypemaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    employeetypeid = models.CharField(db_column='EmployeeTypeID', max_length=100)  # Field name made lowercase.
    employeetype = models.CharField(db_column='EmployeeType', max_length=100)  # Field name made lowercase.
    noofleavepermonth = models.FloatField(db_column='NoOfLeavePerMonth')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_employeetypemaster'


class AccountsEmployeeworkingday(models.Model):
    id = models.BigAutoField(primary_key=True)
    employeeworkingdaymapid = models.CharField(db_column='EmployeeWorkingDayMapID', max_length=100)  # Field name made lowercase.
    employeeid = models.CharField(db_column='EmployeeId', max_length=100)  # Field name made lowercase.
    dayname = models.CharField(max_length=100)
    createddate = models.DateTimeField()
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_employeeworkingday'


class AccountsGender(models.Model):
    id = models.BigAutoField(primary_key=True)
    gender = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'accounts_gender'


class AccountsHolidaymaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    holidayid = models.CharField(db_column='Holidayid', max_length=100)  # Field name made lowercase.
    title = models.CharField(max_length=100)
    description = models.TextField()
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_holidaymaster'


class AccountsInterviewattachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    interviewattachmentmapid = models.CharField(db_column='InterviewAttachmentMapID', max_length=100)  # Field name made lowercase.
    interviewid = models.CharField(db_column='InterviewId', max_length=100)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    attachmenttype = models.CharField(db_column='AttachmentType', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_interviewattachment'


class AccountsInterviewmaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    interview_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=17)
    educationaid = models.CharField(max_length=100)
    departmentid = models.CharField(max_length=100)
    designationid = models.CharField(max_length=100)
    currentsalary = models.CharField(max_length=100)
    expectedsalary = models.FloatField()
    experience_year = models.IntegerField()
    experience_month = models.IntegerField()
    isjoin_days = models.IntegerField()
    joinafterdaysormonth = models.IntegerField(db_column='JoinAfterDaysOrMonth')  # Field name made lowercase.
    personaldetail = models.TextField(db_column='PersonalDetail')  # Field name made lowercase.
    interviewstatusid = models.CharField(db_column='InterviewStatusId', max_length=100)  # Field name made lowercase.
    interviewdate = models.DateField(db_column='InterviewDate')  # Field name made lowercase.
    interviewtime = models.TextField(db_column='InterviewTime')  # Field name made lowercase.
    joindate = models.DateField(db_column='JoinDate')  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=100)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=100)  # Field name made lowercase.
    modifiedby = models.CharField(db_column='ModifiedBy', max_length=100)  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='ModifiedDate')  # Field name made lowercase.
    isactive = models.IntegerField(db_column='IsActive')  # Field name made lowercase.
    assignedid = models.CharField(db_column='Assignedid', max_length=100)  # Field name made lowercase.
    assignedemp = models.CharField(db_column='AssignedEmp', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_interviewmaster'


class AccountsInterviewmasterassigned(models.Model):
    id = models.BigAutoField(primary_key=True)
    interview_id = models.CharField(max_length=100)
    interview_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    assigned = models.DateTimeField()
    assigned_emp = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accounts_interviewmasterassigned'


class AccountsLeavecategorymaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    leave_categoryid = models.CharField(max_length=100)
    leave_category = models.CharField(max_length=100)
    createddate = models.DateTimeField()
    createdby = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)
    modified_date = models.DateTimeField()
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_leavecategorymaster'


class AccountsMaratialstatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'accounts_maratialstatus'


class AccountsRolemaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    roll_id = models.CharField(max_length=100)
    rool_name = models.CharField(max_length=150)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=100)
    modified_by = models.CharField(max_length=100)
    modified_date = models.DateTimeField()
    reports_to = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'accounts_rolemaster'


class AccountsShiftmaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    shiftid = models.CharField(db_column='Shiftid', max_length=100)  # Field name made lowercase.
    shift = models.CharField(max_length=100)
    from_time = models.CharField(max_length=50)
    to_time = models.CharField(max_length=50)
    created_date = models.DateTimeField()
    created_by = models.CharField(max_length=150)
    modified_by = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'accounts_shiftmaster'


class AccountsStatemaster(models.Model):
    id = models.BigAutoField(primary_key=True)
    stateid = models.CharField(max_length=100)
    countryid = models.CharField(max_length=100)
    statename = models.CharField(max_length=80)
    created_date = models.DateTimeField()
    is_active = models.IntegerField(db_column='Is_Active')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts_statemaster'


class AccountsUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    is_employee = models.IntegerField()
    is_hr = models.IntegerField()
    is_manager = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_user'


class AccountsUserGroups(models.Model):
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    group = models.ForeignKey('AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_groups'
        unique_together = (('user', 'group'),)


class AccountsUserUserPermissions(models.Model):
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AccountsUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
