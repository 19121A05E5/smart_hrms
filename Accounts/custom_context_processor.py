
from django import template
from .models import CustomUser,EmployeeMaster,Notification
register = template.Library()

@register.filter
def emp_render(request):
    t = ""
    if request.user.is_authenticated :
        if(request.user.id):
            user = CustomUser.objects.get(id=request.user.id)
            emp = EmployeeMaster.objects.filter(user_id=user.id)
            notification_msg = Notification.objects.filter(recipient=user,status=False).all()
            notifications = Notification.objects.filter(recipient=user,status=False).count()

        return {
            'ath_user':user,
          "emp": emp,
          "notifications": notifications,
          "notification_msg": notification_msg
          }
    else:
        return {
            "emp": "ok",
           }




