# Generated by Django 4.1.4 on 2022-12-23 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='image_url',
            new_name='image',
        ),
    ]
