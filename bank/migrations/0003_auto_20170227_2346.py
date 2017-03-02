# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-27 20:46
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('bank', '0002_auto_20170227_2344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_information',
            name='economic',
            field=models.ForeignKey(blank=True, default='Not Available', on_delete=django.db.models.deletion.CASCADE,
                                    to='loan.Economic'),
        ),
        migrations.AlterField(
            model_name='personal_information',
            name='loan_ac',
            field=models.ForeignKey(blank=True, default='Not Available', on_delete=django.db.models.deletion.CASCADE,
                                    to='loan.Loan'),
        ),
    ]