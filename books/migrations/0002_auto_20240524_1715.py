# Generated by Django 3.2.12 on 2024-05-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.URLField(default='null'),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(default='null', max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(default='null'),
        ),
    ]
