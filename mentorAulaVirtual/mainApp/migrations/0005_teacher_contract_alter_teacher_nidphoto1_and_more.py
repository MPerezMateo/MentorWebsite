# Generated by Django 4.2.2 on 2023-07-09 19:12

from django.db import migrations, models
import mainApp.models


class Migration(migrations.Migration):
    dependencies = [
        ("mainApp", "0004_teacher_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="contract",
            field=models.FileField(
                blank=True, null=True, upload_to=mainApp.models.Teacher.file_upload_to
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="nidPhoto1",
            field=models.ImageField(
                blank=True, null=True, upload_to=mainApp.models.Teacher.file_upload_to
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="nidPhoto2",
            field=models.ImageField(
                blank=True, null=True, upload_to=mainApp.models.Teacher.file_upload_to
            ),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="profilePic",
            field=models.ImageField(
                blank=True, null=True, upload_to=mainApp.models.Teacher.file_upload_to
            ),
        ),
    ]
