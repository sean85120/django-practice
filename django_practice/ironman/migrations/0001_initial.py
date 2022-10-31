# Generated by Django 4.1 on 2022-10-31 09:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Equipment",
            fields=[
                ("Site", models.CharField(max_length=20)),
                ("UserSite", models.CharField(max_length=20)),
                (
                    "EQP_ID",
                    models.CharField(
                        max_length=20, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("User_EQP_ID", models.CharField(max_length=20)),
                ("DESCRIPTION", models.CharField(max_length=200)),
                ("EQP_TYPE", models.CharField(max_length=20)),
                ("EQP_VENDOR", models.CharField(max_length=20)),
            ],
            options={
                "db_table": "equipment",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="People",
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
                ("name", models.CharField(max_length=20)),
                ("age", models.PositiveIntegerField()),
                ("power", models.BooleanField(default=False)),
                ("bio", models.TextField()),
                ("created_time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("phone", models.CharField(blank=True, max_length=10)),
                ("organization", models.CharField(blank=True, max_length=100)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
