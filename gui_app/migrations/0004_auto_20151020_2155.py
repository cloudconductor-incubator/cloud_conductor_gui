# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gui_app', '0003_t_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_project',
            name='created_at',
            field=models.DateTimeField(verbose_name='Create_at', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='t_project',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
        ),
        migrations.AlterField(
            model_name='t_project',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='t_project',
            name='updated_at',
            field=models.DateTimeField(verbose_name='Updated_at', auto_now=True),
        ),
    ]
