# Generated by Django 4.0.2 on 2024-11-22 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='docID',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patID',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
