# Generated by Django 3.2 on 2021-04-25 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TodoTask",
            fields=[
                ("todo_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("todo_title", models.CharField(max_length=200)),
                ("todo_start_date", models.DateTimeField()),
                ("todo_end_date", models.DateTimeField()),
                ("todo_status_is_finished", models.BooleanField(verbose_name=False)),
                ("todo_status_is_archived", models.BooleanField(verbose_name=False)),
                ("todo_status_success_rate", models.FloatField(verbose_name=0.0)),
            ],
        ),
        migrations.DeleteModel(
            name="Task",
        ),
        migrations.DeleteModel(
            name="TaskA",
        ),
    ]
