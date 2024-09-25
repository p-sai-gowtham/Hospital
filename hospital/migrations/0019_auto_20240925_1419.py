# Generated by Django 3.0.5 on 2024-09-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='address',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='admitDate',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='assignedDoctorId',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='mobile',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='symptoms',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='referred_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='report',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='test_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.CharField(blank=True, choices=[('to_do', 'To Do'), ('in_review', 'In Review'), ('done', 'Done')], default='to_do', max_length=20, null=True),
        ),
    ]
