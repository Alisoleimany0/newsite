# Generated by Django 4.0.2 on 2023-09-21 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_different_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='different_id',
        ),
    ]
