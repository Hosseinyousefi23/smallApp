# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 17:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('xnote_base', '0003_post_post_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('conductor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_list', to='xnote_base.SuperConductor')),
                ('invited', models.ManyToManyField(related_name='invite_list', to='xnote_base.Person')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='related_tags',
            field=models.ManyToManyField(to='xnote_base.Tag'),
        ),
        migrations.AddField(
            model_name='event',
            name='places',
            field=models.ManyToManyField(to='xnote_base.Place'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='xnote_base.Tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='xnote_base.Event'),
        ),
    ]
