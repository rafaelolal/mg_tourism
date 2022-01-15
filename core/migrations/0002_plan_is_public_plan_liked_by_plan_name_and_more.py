# Generated by Django 4.0 on 2022-01-13 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='is_public',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to='core.UserProfile'),
        ),
        migrations.AddField(
            model_name='plan',
            name='name',
            field=models.CharField(default='Default Plan Name', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='outdoor',
            name='type',
            field=models.CharField(choices=[('Wildlife Exploration', 'Wildlife Exploration'), ('Hiking', 'Hiking'), ('Biking', 'Biking'), ('Zoo', 'Zoo'), ('River Rafting', 'River Rafting')], max_length=64),
        ),
        migrations.AlterField(
            model_name='shopping',
            name='type',
            field=models.CharField(choices=[('Gift Shop', 'Gift Shop'), ('Shopping Mall', 'Shopping Mall'), ('Antique Store', 'Antique Store'), ('Department Store', 'Department Store'), ('Factory Outlet', 'Factory Outlet')], max_length=64),
        ),
    ]