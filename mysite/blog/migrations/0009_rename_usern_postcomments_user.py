# Generated by Django 4.2.2 on 2023-07-16 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0008_alter_contact_time_alter_post_time_postcomments"),
    ]

    operations = [
        migrations.RenameField(
            model_name="postcomments",
            old_name="usern",
            new_name="user",
        ),
    ]
