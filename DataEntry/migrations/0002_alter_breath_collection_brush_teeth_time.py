# Generated by Django 4.2.1 on 2023-08-25 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("DataEntry", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="breath_collection",
            name="brush_teeth_time",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="brush teeth time"
            ),
        ),
    ]
