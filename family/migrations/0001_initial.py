# Generated by Django 4.1.7 on 2023-03-03 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Family",
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
                ("edad", models.IntegerField()),
                ("nombre", models.CharField(max_length=40)),
                ("nacimiento", models.DateField()),
            ],
        ),
    ]
