# Generated by Django 5.0.1 on 2024-02-25 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0019_alter_post_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(unique=True),
        ),
    ]
