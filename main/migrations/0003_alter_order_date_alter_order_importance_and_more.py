# Generated by Django 4.1.1 on 2022-10-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order_importance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(verbose_name='дата и время'),
        ),
        migrations.AlterField(
            model_name='order',
            name='importance',
            field=models.CharField(max_length=12, verbose_name='очень срочно/срочно/не срочно '),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=159, verbose_name='название'),
        ),
    ]
