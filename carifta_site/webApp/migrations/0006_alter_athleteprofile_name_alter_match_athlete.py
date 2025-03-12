# Generated by Django 4.2.2 on 2025-03-12 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0005_alter_match_athlete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteprofile',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='match',
            name='athlete',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='webApp.athleteprofile'),
        ),
    ]
