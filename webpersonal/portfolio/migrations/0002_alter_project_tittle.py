# Generated by Django 3.2.9 on 2021-12-07 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tittle',
            field=models.CharField(max_length=200),
        ),
    ]
