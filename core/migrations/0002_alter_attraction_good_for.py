# Generated by Django 4.0 on 2022-01-05 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attraction',
            name='good_for',
            field=models.CharField(choices=[('kids', 'Kids'), ('big_groups', 'Big Groups'), ('adrenaline_seekers', 'Adrenaline Seekers'), ('a_rainy_day', 'a Rainy Day'), ('couples', 'Couples')], max_length=64),
        ),
    ]