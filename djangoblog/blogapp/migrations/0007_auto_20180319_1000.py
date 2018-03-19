# Generated by Django 2.0.3 on 2018-03-19 10:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='posted_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]