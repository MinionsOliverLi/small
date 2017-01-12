# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='menus',
            field=models.ManyToManyField(blank=True, to='crm.Menu'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(blank=True, to='crm.Role'),
        ),
    ]
