# Generated by Django 4.2.6 on 2023-10-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bb',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
