# Generated by Django 4.2.2 on 2025-03-25 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0007_alter_match_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='personalBest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
