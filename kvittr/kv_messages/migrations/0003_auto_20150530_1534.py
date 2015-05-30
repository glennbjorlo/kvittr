# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kv_messages', '0002_auto_20150514_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='uname',
            field=models.CharField(max_length=30),
        ),
    ]
