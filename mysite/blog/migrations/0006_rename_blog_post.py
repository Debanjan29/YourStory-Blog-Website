# Generated by Django 4.2.2 on 2023-07-07 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_blog_time"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="blog",
            new_name="Post",
        ),
    ]
