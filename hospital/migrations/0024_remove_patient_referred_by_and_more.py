# Generated by Django 5.0.1 on 2024-09-26 05:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0023_remove_patient_assigneddoctorid_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='referred_by',
        ),
        migrations.AddField(
            model_name='patient',
            name='hospital_referred_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hospital_referred_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
