# Generated by Django 2.2.5 on 2019-09-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routemap', '0004_routelist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routelist',
            name='routes',
            field=models.ManyToManyField(null=True, to='routemap.Route'),
        ),
    ]
