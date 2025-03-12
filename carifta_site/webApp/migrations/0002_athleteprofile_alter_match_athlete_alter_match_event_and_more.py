# Generated by Django 4.2.2 on 2025-03-12 19:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthleteProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=6)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('height', models.DecimalField(decimal_places=2, max_digits=4)),
                ('dob', models.DateField()),
                ('biography', models.CharField(blank=True, max_length=1000, null=True)),
                ('smLinks', models.URLField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='match',
            name='athlete',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='match',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='matches', to='webApp.event'),
        ),
        migrations.DeleteModel(
            name='Athlete',
        ),
    ]
