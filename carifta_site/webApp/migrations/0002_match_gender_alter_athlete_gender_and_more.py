# Generated by Django 4.2.2 on 2025-03-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='MALE', max_length=6),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='smLinks',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='coach',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='match',
            name='eventName',
            field=models.CharField(choices=[('60', '60'), ('100', '100'), ('200', '200'), ('400', '400'), ('800', '800'), ('1500', '1500'), ('3000', '3000'), ('5000', '5000'), ('10000', '10000'), ('60H', '60 Hurdles'), ('100H', '100 Hurdles'), ('110H', '110 Hurdles'), ('400H', '400 Hurdles'), ('3000SC', '3000 SC'), ('4100R', '4×100 Relay'), ('4400R', '4×400 Relay'), ('HM', 'Half Marathon'), ('M', 'Marathon'), ('20KW', '20K Walk'), ('PENT', 'Pentathlon'), ('HEPT', 'Heptathlon'), ('OCTA', 'Octathlon'), ('DECA', 'Decathlon'), ('HJ', 'High Jump'), ('LJ', 'Long Jump'), ('TRJ', 'Triple Jump'), ('PV', 'Pole Vault'), ('DISCUS', 'Discus'), ('JAVE', 'Javelin'), ('HAM', 'Hammer'), ('SHOT', 'Shot Put'), ('80', '80 Metres'), ('1000', '1000 Metres'), ('1200', '1200 Metres'), ('80H', '80 Hurdles'), ('BT', 'Ball Throw')], max_length=200),
        ),
        migrations.AlterField(
            model_name='match',
            name='mark',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='match',
            name='season',
            field=models.IntegerField(choices=[(2025, '2025'), (2024, '2024'), (2023, '2023'), (2022, '2022'), (2021, '2021'), (2020, '2020'), (2019, '2019')]),
        ),
    ]
