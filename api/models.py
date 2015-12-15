# coding=utf-8
from django.db import models

# Create your models here.


# class API(models.Model):
#     API_TYPES = (('hardware', '硬件'), ('member', '人员'), ('none', '未知'))
#     created = models.DateTimeField(auto_now_add=True)
#     # name = models.CharField(max_length=100, blank=True, default='')
#     help_text = models.CharField(max_length=100, blank=True, default='')
#     api_type = models.CharField(choices=API_TYPES, default='', max_length=100)
#
#     class Meta:
#         abstract = True
#
#
# class Hardware(API):
#     class Meta:
#         ordering = ('created',)


class Switch(models.Model):
    STATUS_CHOICES = (('active', '使用中'), ('disabled', '已失效'))
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='', help_text="请输入开关名称")
    pin = models.IntegerField(blank=False, help_text="请输入输出引脚编号")
    status = models.CharField(choices=STATUS_CHOICES, default='using', max_length=100)
    # hardware = models.ForeignKey(Hardware, on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
