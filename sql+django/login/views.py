from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
fn=''
pwd=''

# Create your views here.
def login(request):
    global fn,pwd
    if request.method=='POST':
        m=sql.connect(host="localhost",user="root",password="Admin",database="website")
        cursor = m.cursor()
        d = request.POST   #data in variable d
        for key,value in d.items():
            if key=='first_name':
                fn=value
            if key=='password':
                pwd=value
            
        query="select * from users where first_name='{}' and password='{}'".format(fn,pwd)
        cursor.execute(query)
        t=cursor.fetchall()
        m.commit()
        if t==():
            return HttpResponse('error')
        else:
            return HttpResponse("welcome")

    return render(request,'login.html')
