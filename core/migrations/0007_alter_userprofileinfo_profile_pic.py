# Generated by Django 4.0 on 2022-01-08 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_userprofileinfo_first_name_userprofileinfo_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
