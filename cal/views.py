from django.shortcuts import render, redirect, get_object_or_404, reverse
import datetime
from .models import Event, who
import calendar
from .calendar import Calendar
from django.utils.safestring import mark_safe
from .forms import EventForm
from django.utils import timezone
from common.models import What_food, People
from random import randint
from django.contrib.auth.decorators import login_required

def calendar_view(request):
    
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)
    username = request.user.username
    pe = People.objects.get(name=username)
    k=pe.id
    cal = Calendar(today.year, today.month)
    html_cal = cal.formatmonth(k,withyear=True)
    result_cal = mark_safe(html_cal)



    todayy=timezone.localtime()
    #month=What_food.objects.filter(month=todayy.month)
    
    a=What_food.objects.filter(who=pe)
    how_my=a.filter(month=todayy.month).count()
    date_list=[]
    for item in a:
        if item.date not in date_list:
            time=datetime.date(int(str(item.date)[0:4]),int(str(item.date)[4:6]),int(str(item.date)[6:8]))
            if Event.objects.filter(start_time=time,who=k).count()==0:
                instance = Event(start_time=time,title=randint(1,5),who=k)
                instance.save()
                date_list.append(item.date)

    context = {'zz' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var, 'how_my': how_my}
    return render(request, 'cal/events.html', context)

#현재 달력을 보고 있는 시점의 시간을 반환
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

#현재 달력의 이전 달 URL 반환
def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

#현재 달력의 다음 달 URL 반환
def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

#새로운 Event의 등록 혹은 수정
'''
def event(request, event_id=None):
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return redirect('cal:calendar')
    return render(request, 'cal/input.html', {'form': form})
'''
def event(request, event_id=None):
    
    todayy=timezone.localtime()
    month=What_food.objects.filter(month=todayy.month)
    username = request.user.username
    pe = {'people':People.objects.get(name=username)}
    a=month.filter(who=pe)
    k=[]
    for item in a:
        if item.date not in k:
            time=datetime.date(item.date[0:4],item.date[4:6],item.date[6:8])
            instance = Event(start_time=time)
            form = EventForm(request.POST or None, instance=instance)
            k.append(item.date)
            if form.is_valid():
                form.save()

    
