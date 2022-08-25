# Generated by Django 4.1 on 2022-08-18 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Food'), (2, 'Health'), (3, 'Dwelling'), (4, 'Transportation'), (5, 'Education'), (6, 'Entertainment'), (7, 'Unexpected'), (8, 'Other')], default=8),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='income',
            name='date',
            field=models.DateField(),
        ),
    ]
