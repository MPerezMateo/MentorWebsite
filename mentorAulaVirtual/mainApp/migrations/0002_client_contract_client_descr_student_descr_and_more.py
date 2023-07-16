# Generated by Django 4.2.2 on 2023-07-12 20:30

from django.db import migrations, models
import mainApp.models


class Migration(migrations.Migration):
    dependencies = [
        ("mainApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="contract",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=mainApp.models.MonetaryUser.file_upload_to,
            ),
        ),
        migrations.AddField(
            model_name="client",
            name="descr",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="descr",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="contract",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to=mainApp.models.MonetaryUser.file_upload_to,
            ),
        ),
    ]