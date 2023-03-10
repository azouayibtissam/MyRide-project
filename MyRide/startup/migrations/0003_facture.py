# Generated by Django 4.1.3 on 2023-02-10 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startup', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
                ('montant', models.IntegerField(max_length=200)),
                ('voyage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startup.voyage')),
            ],
        ),
    ]
