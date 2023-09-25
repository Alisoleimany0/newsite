# Generated by Django 4.0.2 on 2023-09-23 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0006_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Userwrite',
        ),
        migrations.AddField(
            model_name='comment',
            name='writer',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]