from django.shortcuts import render
from block.models import Block
from django.contrib.auth.models import User
import uuid
from activate.models import ActivateCode
from django.utils import timezone
from datetime import timedelta
from django.core.mail import send_mail
def index(request):
    block_info = Block.objects.filter(status=0).order_by("-id")
    return render(request,"index.html",{"blocks":block_info})

def register(request):
    error = ""
    if request.method =="GET":
           return render(request, "register.html")
    else:
        username = request.POST["username"].strip() #双引号单引号均可
        email = request.POST['email'].strip()
        password = request.POST['password'].strip()
        repassword = request.POST['re_password'].strip()
        if not username or not email or not password or not repassword:
            error = "任何字段都不能为空"
        if password != repassword:
            error = "两次输入密码不一致"
        if User.objects.filter(username=username).count()>=1:
            error = "用户已存在"
        if not error:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            new_code = str(uuid.uuid4()).replace("-","")
            expire_timestamp = timezone.now() + timedelta(days=3)
            user_activate_info = ActivateCode(owner = user, code = new_code, expire_timestamp = expire_timestamp)
            user_activate_info.save()

            activate_link = "http://%s/activate/%s" %(request.get_host(), new_code)
            activate_email = '''点击<a href="%s">这里激活</a>'''% activate_link
            send_mail(subject = '[MTIChina]激活邮件',
                      message='点击链接激活：%s'% activate_link,
                      html_message=activate_email,
                      from_email='635857462@qq.com',
                      recipient_list=[email],
                      fail_silently=False)

            return render(request, "success.html",{"msg":"您已注册，验证码已发至您所注册的邮箱，请前往邮箱进行最后一步验证。"})

        else:
            return render(request, "register.html",{"username":username,"email":email,"error":error})

