# Generated by Django 4.1.1 on 2022-10-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_order_date_alter_order_importance_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=0, verbose_name='Номер'),
        ),
    ]
