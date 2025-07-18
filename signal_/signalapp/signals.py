from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("--------------------------")
    print('Logged-in signal... run intro')
    print("sender",sender)
    print("request",request)
    print("user",user)
    print("user",user.password)
    print("user",user.username)
    print(f'"kwargs":{kwargs}')

# user_logged_in.connect(login_success,sender=User)

@receiver(user_logged_out,sender=User)
def log_out(sender,request,user,**kwargs):
    print("--------------------------")
    print('Log_out-in signal...')
    print("sender",sender)
    print("request",request)
    print("user",user)
    print(f'"kwargs":{kwargs}')

