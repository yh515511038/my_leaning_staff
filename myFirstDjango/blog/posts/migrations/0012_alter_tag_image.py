# Generated by Django 5.0.1 on 2024-02-16 04:05

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0011_tag_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="image",
            field=imagekit.models.fields.ProcessedImageField(
                null=True, upload_to="posts"
            ),
        ),
    ]
