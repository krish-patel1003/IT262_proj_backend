# Generated by Django 4.1.7 on 2023-03-13 07:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0007_alter_appointment_options_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='appointment',
            name='check_appointment_date_range',
        ),
        migrations.AddConstraint(
            model_name='appointment',
            constraint=models.CheckConstraint(check=models.Q(('date__lt', datetime.datetime(2023, 3, 30, 12, 41, 34, 573043))), name='check_appointment_date_range'),
        ),
    ]
