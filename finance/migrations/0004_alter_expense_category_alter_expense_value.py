# Generated by Django 4.1 on 2022-08-25 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_alter_expense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('Other', 'Other'), ('Food', 'Food'), ('Health', 'Health'), ('Dwelling', 'Dwelling'), ('Transportation', 'Transportation'), ('Education', 'Education'), ('Entertainment', 'Entertainment'), ('Unexpected', 'Unexpected')], default='Other', max_length=128),
        ),
        migrations.AlterField(
            model_name='expense',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=32),
        ),
    ]
