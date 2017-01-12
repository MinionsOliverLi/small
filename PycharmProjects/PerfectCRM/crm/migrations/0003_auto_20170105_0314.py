# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20170105_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='menus',
        ),
        migrations.AddField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(to='crm.Menu', blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(to='crm.Tag', blank=True),
        ),
    ]
