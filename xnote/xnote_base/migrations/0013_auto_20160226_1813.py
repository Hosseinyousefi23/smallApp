# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-26 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xnote_base', '0012_superconductor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='follows',
            field=models.ManyToManyField(related_name='followers', through='xnote_base.Follow', to='xnote_base.SuperConductor'),
        ),
    ]
