# Generated by Django 3.2.15 on 2022-11-19 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0009_auto_20221120_0019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='materials',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cheque', 'cheque')], max_length=13),
        ),
        migrations.AlterField(
            model_name='task',
            name='materialsq',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cheque', 'cheque')], max_length=13),
        ),
        migrations.AlterField(
            model_name='task',
            name='materialss',
            field=models.CharField(choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cheque', 'cheque')], max_length=13),
        ),
    ]
