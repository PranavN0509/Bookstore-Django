# Generated by Django 4.2.4 on 2023-11-02 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_method',
        ),
    ]
