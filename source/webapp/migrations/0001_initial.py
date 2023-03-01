# Generated by Django 4.1.7 on 2023-03-01 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IssueStatus",
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
                ("name", models.CharField(max_length=30, verbose_name="Статус")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "edited_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время редактирования"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="IssueType",
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
                ("name", models.CharField(max_length=30, verbose_name="Тип")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "edited_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время редактирования"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Issue",
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
                    "summary",
                    models.CharField(max_length=50, verbose_name="Краткое описание"),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=2000,
                        null=True,
                        verbose_name="Полное описание",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата и время создания"
                    ),
                ),
                (
                    "edited_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата и время редактирования"
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="issue_statuses",
                        to="webapp.issuestatus",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        related_name="issue_types",
                        to="webapp.issuetype",
                        verbose_name="Тип",
                    ),
                ),
            ],
        ),
    ]