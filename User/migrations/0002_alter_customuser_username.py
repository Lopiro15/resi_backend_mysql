# Generated by Django 4.0.2 on 2022-04-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(max_length=255, null=True, unique=True),
        ),
    ]
