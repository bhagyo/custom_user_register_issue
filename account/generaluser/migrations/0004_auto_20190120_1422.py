# Generated by Django 2.1.5 on 2019-01-20 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generaluser', '0003_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]