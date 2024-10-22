# Generated by Django 5.0.7 on 2024-10-15 17:48

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Parent", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="writemsg",
            name="date",
            field=models.DateField(
                default=django.utils.timezone.now, verbose_name="Date Sent"
            ),
        ),
    ]
