# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_delete_attendance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'verbose_name': '\u9009\u62e9'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': '\u95ee\u9898'},
        ),
    ]
