# Generated by Django 4.1.3 on 2023-02-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0014_rename_content_comment_msg_voyage_montant_and_more'),
    ]

    operations = [
       
        migrations.AlterField(
            model_name='comment',
            name='date_comment',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='heure_debut',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='voyage',
            name='heure_fin',
            field=models.CharField(max_length=30),
        ),
    ]