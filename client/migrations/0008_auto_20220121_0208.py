# Generated by Django 3.2 on 2022-01-21 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0007_alter_client_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='photo',
            field=models.ImageField(null=True, upload_to='client/image/'),
        ),
        migrations.AlterField(
            model_name='commande',
            name='statucommande',
            field=models.CharField(choices=[('EN ATTENTE', 'En Attente'), ('VALIDE', 'Validé'), ('ANNULE', 'Annulé')], max_length=100),
        ),
    ]
