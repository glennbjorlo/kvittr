# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('kv_messages', '0003_auto_20150530_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='umessage',
            field=models.TextField(max_length=140, validators=[django.core.validators.RegexValidator(b'^[\\w.@+-]+$', b'Only letters and numbers allowed', b'invalid')]),
        ),
    ]
