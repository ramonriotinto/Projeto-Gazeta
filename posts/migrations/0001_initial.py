# Generated by Django 4.2.5 on 2023-09-14 14:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Posts",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.CharField(max_length=150)),
                ("history", models.CharField(max_length=10000)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("img_card", models.CharField(max_length=300)),
                ("img_post_1", models.CharField(max_length=300)),
                ("img_post_2", models.CharField(max_length=300)),
            ],
        ),
    ]
