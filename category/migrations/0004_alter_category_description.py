# Generated by Django 4.2.6 on 2023-11-08 09:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0003_alter_category_slug_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
