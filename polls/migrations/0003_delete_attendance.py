# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_attendance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]
