# Generated by Django 4.1.7 on 2023-07-27 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DATA', '0002_remove_pulang_hari_penginapan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tamu',
            name='Alamat',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tamu',
            name='NIK',
            field=models.CharField(max_length=18),
        ),
    ]