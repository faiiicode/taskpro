# Generated by Django 3.2.15 on 2022-11-20 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0013_auto_20221120_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='materials',
            field=models.CharField(choices=[('C', 'Credit Card'), ('D', 'Debit Card'), ('Ch', 'cheque')], default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='task',
            name='materialsq',
            field=models.CharField(choices=[('C', 'Credit Card'), ('D', 'Debit Card'), ('Ch', 'cheque')], default=None, max_length=2),
        ),
        migrations.AlterField(
            model_name='task',
            name='materialss',
            field=models.CharField(choices=[('C', 'Credit Card'), ('D', 'Debit Card'), ('Ch', 'cheque')], default=None, max_length=2),
        ),
    ]