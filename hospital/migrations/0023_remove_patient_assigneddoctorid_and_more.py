# Generated by Django 5.0.1 on 2024-09-25 17:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0022_auto_20240925_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='assignedDoctorId',
        ),
        migrations.AddField(
            model_name='patient',
            name='assigned_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='scans',
            field=models.TextField(blank=True, null=True),
        ),
    ]
