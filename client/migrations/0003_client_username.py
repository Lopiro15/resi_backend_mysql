# Generated by Django 3.2 on 2022-01-13 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='username',
            field=models.CharField(default='root', max_length=100),
        ),
    ]
