# Generated by Django 5.0.7 on 2024-10-22 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Parent", "0004_leave_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="parent",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="profile_images/"),
        ),
    ]
