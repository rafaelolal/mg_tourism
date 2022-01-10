# Generated by Django 4.0 on 2022-01-08 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0007_alter_userprofileinfo_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='user',
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='biography',
            field=models.TextField(max_length=512, null=True),
        ),
    ]
