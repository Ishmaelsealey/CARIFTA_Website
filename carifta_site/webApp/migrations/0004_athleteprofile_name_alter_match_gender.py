# Generated by Django 4.2.2 on 2025-03-12 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_alter_match_event_delete_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='athleteprofile',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=6),
        ),
    ]
