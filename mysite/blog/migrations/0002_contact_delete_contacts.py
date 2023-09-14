# Generated by Django 4.2.2 on 2023-07-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                ("SIno", models.AutoField(primary_key=True, serialize=False)),
                ("Name", models.TextField(max_length=70)),
                ("Phone", models.CharField(max_length=13)),
                ("Email", models.TextField(max_length=30)),
                ("Content", models.TextField(max_length=400)),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Contacts",
        ),
    ]