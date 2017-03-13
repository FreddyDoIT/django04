from django.shortcuts import render
from .models import ActivateCode
from django.utils import timezone

def activate(requste, code):
    query = ActivateCode.objects.filter(code=code, expire_timestamp__gte = timezone.now())
    if query.count()>0:
        user_activate_info = query[0]
        user_activate_info.owner.is_active = True
        user_activate_info.owner.save()
        return render(requste, "success.html", {"message":"激活成功"})
    else:
        return render(requste, "success.html", {"message":"激活失败"})








