# Generated by Django 4.2.6 on 2023-10-23 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('btest', '0004_rubric'),
    ]

    operations = [
        migrations.AddField(
            model_name='bb',
            name='rubric',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='btest.rubric', verbose_name='Рубрика'),
        ),
    ]
