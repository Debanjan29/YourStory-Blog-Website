# Generated by Django 4.2.2 on 2023-07-07 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_blog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="time",
            field=models.DateTimeField(blank=True),
        ),
    ]
