# Generated by Django 4.1.7 on 2023-03-10 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0005_remove_appointment_check_appointment_date_range_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='appointment',
            name='check_appointment_date_range',
        ),
        migrations.AddConstraint(
            model_name='appointment',
            constraint=models.CheckConstraint(check=models.Q(('date__lt', datetime.datetime(2023, 3, 27, 17, 19, 56, 190248))), name='check_appointment_date_range'),
        ),
    ]
