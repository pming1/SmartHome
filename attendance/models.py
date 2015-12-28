#coding=utf-8
from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Attendance(models.Model):
    # question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    checking_date_sys = models.DateTimeField('Checking in system time')
    remark_text = models.CharField(max_length=200)
    TYPE_CHOICES = (('morning', '早上'), ('noon', '中午'), ('afternoon', '下午'))
    type = models.CharField(choices=TYPE_CHOICES, default='morning', max_length=100)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # def __str__(self):
    #     return self.question_text

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class AttendanceParam(models.Model):
    more_min = models.IntegerField('More miniutes than true time')
