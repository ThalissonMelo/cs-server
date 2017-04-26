# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-21 17:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceCheck',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('has_attended', models.BooleanField(default=bool)),
                ('attempts', models.SmallIntegerField(default=int)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('max_attempts', models.SmallIntegerField(default=3)),
                ('expiration_minutes', models.SmallIntegerField(default=5)),
                ('max_string_distance', models.SmallIntegerField(default=0)),
                ('max_number_of_absence', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created', models.DateTimeField()),
                ('expires', models.DateTimeField()),
                ('passphrase', models.CharField(max_length=100)),
                ('sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                            related_name='events', to='attendance.AttendanceSheet')),
            ],
        ),
        migrations.AddField(
            model_name='attendancesheet',
            name='last_event',
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.Event'),
        ),
        migrations.AddField(
            model_name='attendancesheet',
            name='owner',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='attendancecheck',
            name='event',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='attendance.Event'),
        ),
        migrations.AddField(
            model_name='attendancecheck',
            name='user',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
