# Generated by Django 2.1.5 on 2019-01-20 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_type', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='bmdc',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='disease',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
