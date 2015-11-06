# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui_app', '0006_auto_20151021_1123'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nippou',
            new_name='t_nippou',
        ),
    ]
