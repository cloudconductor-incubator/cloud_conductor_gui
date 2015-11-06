# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui_app', '0004_auto_20151020_2155'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='nippou',
            table='nippou',
        ),
        migrations.AlterModelTable(
            name='t_project',
            table='t_project',
        ),
    ]
