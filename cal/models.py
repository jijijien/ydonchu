from django.db import models
from django.urls import reverse
from common.models import People
class Event(models.Model):
    start_time = models.DateTimeField("시작시간")
    title=models.IntegerField(default=1)
    who=models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)

    @property
    def get_html_url(self):
        wh_pic='f'+str(self.title)
        k='/static/cal/'+wh_pic+'.png'
        return '<img src='+k+' width="30px" height="auto">'
        #return f'<img src={pic} width="61px" height="auto">'

class who(models.Model):
    title=models.IntegerField(default=1)