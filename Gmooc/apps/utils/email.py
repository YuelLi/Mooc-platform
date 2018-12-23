from user.models import EmailVerifyRecord
from django.core.mail import send_mail

import string, random
from Gmooc.settings import EMAIL_FROM

def generate_random_code(length=16):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def send_email(email, type='r'):
    email_record= EmailVerifyRecord()
    code = generate_random_code()
    email_record.code= code
    email_record.email=email
    email_record.send_type= type
    email_record.save()

    subject=""
    message=""

    if(type=='r'):
        subject="Gmooc Account Activation"
        message="Click this link to activate your account: http://127.0.0.1:8000/activate/{0}.".format(code)

        send_status = send_mail(subject,message,EMAIL_FROM,[email])
        if send_status:
            pass

    if(type=='f'):
        subject="Gmooc Password Reset"
        message="Click this link to reset your account: http://127.0.0.1:8000/reset/password/{0}.".format(code)

        send_status = send_email(subject,message,EMAIL_FROM,[email])

        if send_status:
            pass