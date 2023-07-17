# Generated by Django 4.2.2 on 2023-07-17 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mainApp.models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Availability",
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
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("MON", "Lunes"),
                            ("TUE", "Martes"),
                            ("WED", "Miércoles"),
                            ("THR", "Jueves"),
                            ("FRI", "Viernes"),
                            ("SAT", "Sábado"),
                            ("SUN", "Domingo"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "shift",
                    models.CharField(
                        choices=[
                            ("MOR", "Mañanas"),
                            ("AFT", "Tardes"),
                            ("A_D", "Todo el día"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Origin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
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
                ("active", models.BooleanField(default=True)),
                ("extra", models.CharField(blank=True, max_length=255, null=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("descr", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Subject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "defaultPrice",
                    models.DecimalField(decimal_places=2, max_digits=5, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Teacher",
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
                ("active", models.BooleanField(default=True)),
                ("extra", models.CharField(blank=True, max_length=255, null=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("descr", models.CharField(blank=True, max_length=255, null=True)),
                ("phone", models.CharField(max_length=9, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("nid", models.CharField(max_length=9, unique=True)),
                ("bankAccount", models.CharField(blank=True, max_length=40, null=True)),
                ("bicSwift", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "contract",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=mainApp.models.MonetaryUser.file_upload_to,
                    ),
                ),
                ("yearBirth", models.PositiveSmallIntegerField(blank=True, null=True)),
                ("studies", models.CharField(blank=True, max_length=255, null=True)),
                ("xpYears", models.PositiveSmallIntegerField(default=0)),
                ("estHours", models.PositiveSmallIntegerField(default=0)),
                (
                    "academyEmail",
                    models.EmailField(
                        blank=True, max_length=254, null=True, unique=True
                    ),
                ),
                (
                    "profilePic",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=mainApp.models.Teacher.file_upload_to,
                    ),
                ),
                ("category", models.CharField(blank=True, max_length=40, null=True)),
                (
                    "nidPhoto1",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=mainApp.models.Teacher.file_upload_to,
                    ),
                ),
                (
                    "nidPhoto2",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to=mainApp.models.Teacher.file_upload_to,
                    ),
                ),
                (
                    "admin",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="administrator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("students", models.ManyToManyField(to="mainApp.student")),
                (
                    "subjects",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="mainApp.subject",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Client",
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
                ("active", models.BooleanField(default=True)),
                ("extra", models.CharField(blank=True, max_length=255, null=True)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("descr", models.CharField(blank=True, max_length=255, null=True)),
                ("phone", models.CharField(max_length=9, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                ("nid", models.CharField(max_length=9, unique=True)),
                ("bankAccount", models.CharField(blank=True, max_length=40, null=True)),
                ("bicSwift", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "contract",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=mainApp.models.MonetaryUser.file_upload_to,
                    ),
                ),
                ("origin", models.CharField(max_length=20)),
                (
                    "students",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="mainApp.student",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
