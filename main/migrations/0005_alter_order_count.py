# Generated by Django 4.1.1 on 2022-10-12 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_order_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='count',
            field=models.CharField(default=0, max_length=1, verbose_name='Номер'),
        ),
    ]
