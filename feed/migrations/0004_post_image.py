# Generated by Django 5.0.2 on 2024-02-13 14:44

import sorl.thumbnail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
