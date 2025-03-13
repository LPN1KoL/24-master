# Generated by Django 5.1.1 on 2024-09-12 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0, verbose_name='Итоговая цена'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('1', 'Подан'), ('2', 'На рассмотрении'), ('3', 'Принят'), ('4', 'Выполняется'), ('5', 'Готов')], default='1', max_length=100, verbose_name='Статус заказа'),
        ),
        migrations.CreateModel(
            name='OrderElement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcount', models.PositiveIntegerField(verbose_name='Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.order', verbose_name='Заказ')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='shop.product', verbose_name='Продукт')),
            ],
        ),
    ]
