# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kv_messages', '0004_auto_20150602_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='umessage',
            field=models.TextField(max_length=140),
        ),
    ]
