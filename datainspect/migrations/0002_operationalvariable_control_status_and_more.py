# Generated by Django 5.1 on 2024-08-22 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datainspect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationalvariable',
            name='control_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='operationalvariable',
            name='error_rate',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='operationalvariable',
            name='response_time',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='operationalvariable',
            name='reward',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='operationalvariable',
            name='value',
            field=models.FloatField(default=0.0),
        ),
    ]
