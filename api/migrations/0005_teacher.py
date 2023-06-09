# Generated by Django 4.2 on 2023-05-07 13:28

import api.models.teachers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_attachment_remove_ad_description_user_surname_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, help_text="Time of creation"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Last update time"),
                ),
                (
                    "full_name",
                    models.CharField(
                        help_text="Full name of the teacher.", max_length=528
                    ),
                ),
                ("job_title", models.CharField(help_text="Job title.", max_length=528)),
                (
                    "image",
                    models.ImageField(
                        upload_to=api.models.teachers.custom_upload_to_teacher_images
                    ),
                ),
            ],
            options={"abstract": False,},
        ),
    ]
