# Generated by Django 5.0.1 on 2024-01-06 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_invoice_invoiceid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='invoiceID',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='invoicedetail',
            old_name='detailsID',
            new_name='id',
        ),
    ]
