# Generated by Django 5.0.4 on 2024-05-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_sessiondata_session_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessiondata',
            name='arousal',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='sessiondata',
            name='attention',
            field=models.FloatField(),
        ),
    ]
