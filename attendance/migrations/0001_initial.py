# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date published')),
                ('checking_date_sys', models.DateTimeField(verbose_name=b'Checking in system time')),
                ('remark_text', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[(b'morning', b'\xe6\x97\xa9\xe4\xb8\x8a'), (b'noon', b'\xe4\xb8\xad\xe5\x8d\x88'), (b'afternoon', b'\xe4\xb8\x8b\xe5\x8d\x88')], default=b'morning', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceParam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('more_min', models.IntegerField(verbose_name=b'More miniutes than true time')),
            ],
        ),
    ]
