# Generated by Django 4.1.3 on 2022-11-19 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuser",
            old_name="end_at",
            new_name="end_date",
        ),
        migrations.RenameField(
            model_name="customuser",
            old_name="start_at",
            new_name="start_date",
        ),
    ]
