# Generated by Django 3.2.11 on 2022-05-21 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0002_auto_20220521_0235'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportedcase',
            name='experiment',
            field=models.JSONField(default=dict),
        ),
    ]
