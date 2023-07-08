# Generated by Django 4.2.2 on 2023-07-08 21:17

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("mainApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("surnames", models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="teacher",
            name="nidPhoto1",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
        migrations.AddField(
            model_name="teacher",
            name="nidPhoto2",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
        migrations.AddField(
            model_name="teacher",
            name="profilePic",
            field=models.ImageField(blank=True, null=True, upload_to="uploads/"),
        ),
        migrations.AddField(
            model_name="teacher",
            name="students",
            field=models.ManyToManyField(to="mainApp.student"),
        ),
    ]
