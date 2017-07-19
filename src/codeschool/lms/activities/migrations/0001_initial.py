# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-18 23:41
from __future__ import unicode_literals

import codeschool.lms.activities.models.mixins
import codeschool.lms.activities.validators
import decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import wagtail_model_tools.models.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0033_remove_golive_expiry_help_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('manual_grading', models.BooleanField(default=True, help_text='True if feedback was created manually by a human.')),
                ('given_grade_pc', models.DecimalField(blank=True, decimal_places=3, help_text='This grade is given by the auto-grader and represents the grade for the response before accounting for any bonuses or penalties.', max_digits=6, null=True, validators=[codeschool.lms.activities.validators.grade_validator], verbose_name='percentage of maximum grade')),
                ('final_grade_pc', models.DecimalField(blank=True, decimal_places=3, help_text="Similar to given_grade, but can account for additional factors such as delay penalties or for any other reason the teacher may want to override the student's grade.", max_digits=6, null=True, validators=[codeschool.lms.activities.validators.grade_validator], verbose_name='final grade')),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(codeschool.lms.activities.models.mixins.FromProgressAttributesMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('status', model_utils.fields.StatusField(choices=[('opened', 'opened'), ('closed', 'closed')], default='opened', max_length=100, no_check_for_status=True, verbose_name='status')),
                ('status_changed', model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='status changed')),
                ('final_grade_pc', models.DecimalField(decimal_places=3, default=decimal.Decimal, help_text='Final grade given to considering all submissions, penalties, etc.', max_digits=6, verbose_name='final score')),
                ('given_grade_pc', models.DecimalField(decimal_places=3, default=decimal.Decimal, help_text='Final grade before applying any modifier.', max_digits=6, verbose_name='grade')),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('points', models.IntegerField(default=0)),
                ('score', models.IntegerField(default=0)),
                ('stars', models.FloatField(default=0.0)),
                ('is_correct', models.BooleanField(default=bool)),
                ('has_submissions', models.BooleanField(default=bool)),
                ('has_feedback', models.BooleanField(default=bool)),
                ('has_post_tests', models.BooleanField(default=bool)),
                ('activity_page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Page')),
            ],
            options={
                'verbose_name': 'student progress',
                'verbose_name_plural': 'student progress list',
            },
            bases=(wagtail_model_tools.models.mixins.CopyMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('hash', models.CharField(max_length=32)),
                ('ip_address', models.CharField(blank=True, max_length=20)),
                ('num_recycles', models.IntegerField(default=0)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_activities.submission_set+', to='contenttypes.ContentType')),
                ('progress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='activities.Progress')),
            ],
            options={
                'verbose_name': 'submission',
                'verbose_name_plural': 'submissions',
            },
            bases=(codeschool.lms.activities.models.mixins.FromProgressAttributesMixin, wagtail_model_tools.models.mixins.CopyMixin, models.Model),
        ),
        migrations.AddField(
            model_name='progress',
            name='best_submission',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='activities.Submission'),
        ),
        migrations.AddField(
            model_name='progress',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_activities.progress_set+', to='contenttypes.ContentType'),
        ),
    ]
