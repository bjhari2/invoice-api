# Generated by Django 5.0.1 on 2024-01-06 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoiceID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='detailsID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]