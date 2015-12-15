# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Switch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(blank=True, default=b'', help_text=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe5\xbc\x80\xe5\x85\xb3\xe5\x90\x8d\xe7\xa7\xb0', max_length=100)),
                ('pin', models.IntegerField(help_text=b'\xe8\xaf\xb7\xe8\xbe\x93\xe5\x85\xa5\xe8\xbe\x93\xe5\x87\xba\xe5\xbc\x95\xe8\x84\x9a\xe7\xbc\x96\xe5\x8f\xb7')),
                ('status', models.CharField(choices=[(b'active', b'\xe4\xbd\xbf\xe7\x94\xa8\xe4\xb8\xad'), (b'disabled', b'\xe5\xb7\xb2\xe5\xa4\xb1\xe6\x95\x88')], default=b'using', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
