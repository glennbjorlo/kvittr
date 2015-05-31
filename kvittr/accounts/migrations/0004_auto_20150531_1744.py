# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150531_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updatepicture',
            name='user_picture',
            field=models.ImageField(upload_to=b'theme/user_images/'),
        ),
    ]
