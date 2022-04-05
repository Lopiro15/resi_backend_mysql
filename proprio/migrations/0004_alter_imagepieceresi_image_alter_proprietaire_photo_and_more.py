# Generated by Django 4.0.2 on 2022-04-03 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proprio', '0003_rename_disponibilité_residence_disponibilite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepieceresi',
            name='image',
            field=models.ImageField(upload_to='image/resi/'),
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='photo',
            field=models.ImageField(null=True, upload_to='image/profile/'),
        ),
        migrations.AlterField(
            model_name='proprietaire',
            name='piece_identite',
            field=models.ImageField(null=True, upload_to='image/profile/'),
        ),
        migrations.AlterField(
            model_name='residence',
            name='photocouverture',
            field=models.ImageField(null=True, upload_to='image/resi/'),
        ),
    ]