# Generated by Django 4.2.4 on 2023-09-26 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.TextField(default=''),
        ),
    ]
