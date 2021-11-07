from datetime import date
from django.db import models
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count
from common.models import What_food, People
from datetime import datetime, timedelta


# Create your views here.

def day(k):
    a=str(k.year)
    if k.month<10:
        a=a+'0'+str(k.month)
    else:
        a+=str(k.month)
    if k.day<10:
        a=a+'0'+str(k.day)
    else:
        a+=str(k.day)
    to=What_food.objects.filter(date=int(a))
    to=to.count()
    return to



def index(request):
    Today= timezone.localtime().date
    
    todayy=timezone.localtime()
    yesterday = datetime.now() - timedelta(days=1)
    yesterday.strftime('%m%d%y')
    today_how={'to': day(todayy),'yes':day(yesterday),'Today':Today}

    month=What_food.objects.filter(month=todayy.month)
    people_list=People.objects.all()
    my_list={}
    my_list_ti=[]
    for pe in people_list:
        a=month.filter(who=pe)

        if a==None:
            pass
        elif a.count() in my_list:
            k=my_list[a.count()]
            k.append(pe.name)
            my_list[a.count()]=k
        else:
            my_list[a.count()]=[pe.name]
        my_list_ti.append(a.count())
        my_list_ti.sort(reverse=True)
        for a in range(len(my_list_ti)):
            if a==3:
                break
            today_how['n'+str(a+1)]=my_list.get(my_list_ti[a])
            today_how['s'+str(a+1)]=my_list_ti[a]
        for a in range(3):
            if 'n'+str(a+1) not in today_how:
                today_how['n'+str(a+1)]=['']
            elif 's'+str(a+1) not in today_how:
                today_how['s'+str(a+1)]=''

    
    return render(request, 'common/king.html',today_how)
